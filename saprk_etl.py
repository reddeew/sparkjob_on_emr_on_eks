from pyspark.sql import SparkSession

if __name__ == "__main__":
    # Initialize SparkSession
    spark = SparkSession.builder \
        .appName("SparkETL") \
        .getOrCreate()

    try:
        # Load input data from S3
        input_path = "s3://aws-data-analytics-workshops/shared_datasets/tripdata/"
        df = spark.read.csv(input_path, header=True, inferSchema=True)

        # Perform some basic transformation (e.g., select columns, filter, etc.)
        transformed_df = df.select("VendorID", "tpep_pickup_datetime", "tpep_dropoff_datetime", "passenger_count", "trip_distance", "total_amount")

        # Write transformed data back to S3
        output_path = "s3://your-output-bucket/taxi-data/"
        transformed_df.write.mode("overwrite").csv(output_path)
    finally:
        # Stop SparkSession
        spark.stop()
