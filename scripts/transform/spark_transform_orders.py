from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create Spark session
spark = SparkSession.builder \
    .appName("EcommerceOrdersTransform") \
    .getOrCreate()

# Read raw orders
orders_df = spark.read.option("header", True).csv("data/raw/orders.csv")

# Cast columns
orders_df = orders_df \
    .withColumn("quantity", col("quantity").cast("int")) \
    .withColumn("price", col("price").cast("double"))

# Create revenue column
orders_df = orders_df.withColumn(
    "revenue",
    col("quantity") * col("price")
)

# Show result
orders_df.show()

# Save processed data
orders_df.write.mode("overwrite").csv(
    "data/processed/orders",
    header=True
)

spark.stop()

