from pyspark.sql import SparkSession
from pyspark.sql.functions import regexp_extract


# Initialize Spark session
spark = SparkSession.builder.appName("AI-Log-Ingestion").master("local[*]").getOrCreate()

#read raw log files 
logs_df = spark.read.text("app.log")

parsed_df = logs_df.select(
    regexp_extract("value", r"^(.*?)\s", 1).alias("timestamp"),
    regexp_extract("value", r"level=([A-Z]+)", 1).alias("level"),
    regexp_extract("value", r"service=([a-zA-Z]+)", 1).alias("service"),
    regexp_extract("value", r"message=([A-Z_]+)", 1).alias("message"),
)
print("✅ Structured logs:")
parsed_df.show(truncate=False)

spark.stop()