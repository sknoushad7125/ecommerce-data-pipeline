# 🚀 E-Commerce Analytics Data Pipeline

An end-to-end **production-style Data Engineering pipeline** built using **Python, PySpark, PostgreSQL, and Apache Airflow**.  
This project simulates how real-world data teams ingest, transform, store, and automate analytics workflows.

---

## 📌 Project Overview

Modern companies rely on automated data pipelines to generate business insights.  
This project demonstrates a **complete batch ETL pipeline** for e-commerce order data, from raw ingestion to analytics-ready storage with orchestration and monitoring.

---

## 🏗️ Architecture

Raw Data (CSV / API)
↓
Python Ingestion
↓
PySpark ETL Transformations
↓
PostgreSQL Data Warehouse
↓
Apache Airflow (Scheduling & Monitoring)


---

## 🔧 Tech Stack

- **Python** – ingestion, loading, utilities  
- **PySpark** – scalable ETL and transformations  
- **PostgreSQL** – analytics data warehouse  
- **Apache Airflow** – workflow orchestration  
- **SQL** – data modeling & validation  

---

## 📂 Project Structure

```text
ecommerce_data_pipeline/
│
├── data/
│ ├── raw/ # Raw input data
│ └── processed/ # Spark output
│
├── scripts/
│ ├── ingestion/ # Python ingestion scripts
│ ├── transform/ # PySpark ETL jobs
│ └── load/ # PostgreSQL load scripts
│
├── airflow/
│ ├── dags/ # Airflow DAGs
│ ├── logs/
│ └── plugins/
│
├── config/
├── logs/
└── README.md
```

---

## 🗃️ Data Model

### Fact Table
**fact_orders**
- order_id  
- order_date  
- customer_id  
- product_id  
- quantity  
- price  
- revenue  

Designed for **analytics & reporting use cases**.

---

## ⚙️ Pipeline Workflow

1. **Ingestion**
   - Raw order data loaded using Python

2. **Transformation**
   - PySpark cleans data and calculates derived metrics (revenue)

3. **Loading**
   - Transformed data stored in PostgreSQL warehouse

4. **Orchestration**
   - Airflow DAG schedules and monitors the pipeline
   - Task dependencies, retries, and logging enabled

5. **Data Quality**
   - Post-load row count validation

---

## 🧪 Example Airflow DAG Tasks

- spark_transform_orders  
- load_to_postgres  
- check_row_count  

---


## ▶️ How to Run Locally

### 1. Clone Repository
```bash
git clone https://github.com/sknoushad7125/ecommerce-data-pipeline.git
cd ecommerce-data-pipeline
2. Create Virtual Environment
python3.10 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install pyspark psycopg2-binary apache-airflow
4. Run Spark Job
spark-submit scripts/transform/spark_transform_orders.py
5. Load to PostgreSQL
python scripts/load/load_to_postgres.py
6. Start Airflow
airflow webserver
airflow scheduler
Access UI at:
http://localhost:8080
```


Key Learnings:

Building scalable ETL pipelines using Spark
Orchestrating workflows with Apache Airflow
Debugging Spark, Java, and Airflow environment issues
Designing analytics-ready warehouse tables
Applying real-world data engineering best practices

Future Improvements:

Incremental data loading
Cloud migration (AWS S3, EMR, RDS)
Kafka-based streaming ingestion
dbt-based transformations
Dockerized deployment

Author

Noushad Sk

Aspiring AI-Powered Data Engineer

---
