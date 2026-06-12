
from pyspark.sql import functions as F


# recommanded good practice : normalized table to simply the conditions 
# If your SCD table uses NULL for open‑ended rows, convert them to a sentinel (9999-12-31).

scd = scd.withColumn(
    "datetime_stop",
    F.coalesce("datetime_stop", F.lit("9999-12-31 23:59:59"))
)

def scd2_diagnostic_report(scd_df):
    """
    Build a full diagnostic report for a Type‑2 SCD table.
    Includes:
      - number of rows
      - number of columns
      - min/max datetime_start
      - min/max datetime_stop (NULLs handled)
      - number of changes per serial_number
      - serial with most changes
      - serial with least changes
      - mean number of changes
    """

    # --- Basic structure ---
    num_rows = scd_df.count()
    num_cols = len(scd_df.columns)

    # --- Normalize open-ended rows ---
    scd_norm = scd_df.withColumn(
        "datetime_stop_norm",
        F.coalesce("datetime_stop", F.lit("9999-12-31 23:59:59"))
    )

    # --- Date stats ---
    date_stats = scd_norm.agg(
        F.min("datetime_start").alias("min_start"),
        F.max("datetime_start").alias("max_start"),
        F.min("datetime_stop_norm").alias("min_stop"),
        F.max("datetime_stop_norm").alias("max_stop")
    ).collect()[0]

    # --- Changes per serial ---
    changes = (
        scd_norm.groupBy("serial_number")
                .count()
                .withColumnRenamed("count", "num_changes")
    )

    # Serial with most changes
    most_changes = changes.orderBy(F.col("num_changes").desc()).limit(1).collect()[0]

    # Serial with least changes
    least_changes = changes.orderBy(F.col("num_changes").asc()).limit(1).collect()[0]

    # Mean number of changes
    mean_changes = changes.agg(F.mean("num_changes")).collect()[0][0]

    # --- Build final report ---
    return {
        "num_rows": num_rows,
        "num_columns": num_cols,
        "min_datetime_start": date_stats["min_start"],
        "max_datetime_start": date_stats["max_start"],
        "min_datetime_stop": date_stats["min_stop"],
        "max_datetime_stop": date_stats["max_stop"],
        "serial_most_changes": {
            "serial_number": most_changes["serial_number"],
            "num_changes": most_changes["num_changes"]
        },
        "serial_least_changes": {
            "serial_number": least_changes["serial_number"],
            "num_changes": least_changes["num_changes"]
        },
        "mean_changes_per_serial": mean_changes
    }


# open ended stop
from pyspark.sql import functions as F

joined = (
    timeseries.alias("ts")
    .join(
        scd.alias("scd"),
        (
            (F.col("ts.serial_number") == F.col("scd.serial_number")) &
            (F.col("ts.datetime_record") >= F.col("scd.datetime_start")) &
            (
                (F.col("ts.datetime_record") < F.col("scd.datetime_stop")) |
                F.col("scd.datetime_stop").isNull()
            )
        ),
        "left"
    )
)

# broadcast the small scd table to all compute nodes to avoid shuffle (performance)

# A shuffle in Spark is what happens when Spark must move data across the cluster so that rows that need to be processed together end up on the same machine. It is one of the slowest and most expensive operations Spark can perform.


joined = (
    timeseries.alias("ts")
    .join(
        F.broadcast(scd).alias("scd"),
        (
            (F.col("ts.serial_number") == F.col("scd.serial_number")) &
            (F.col("ts.datetime_record") >= F.col("scd.datetime_start")) &
            (
                (F.col("ts.datetime_record") < F.col("scd.datetime_stop")) |
                F.col("scd.datetime_stop").isNull()
            )
        ),
        "left"
    )
)