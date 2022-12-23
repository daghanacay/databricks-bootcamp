-- Databricks notebook source
-- MAGIC %run ./jobs/includes/Setup_2

-- COMMAND ----------

-- MAGIC %python
-- MAGIC ## load the cutimer data from file
-- MAGIC customers_data_file  = f"{DA.paths.datasets}/retail-org/customers/"
-- MAGIC customer_data = spark.read.format('csv').option("header", True).load(customers_data_file)
-- MAGIC # export the file  data to SQL temporary view
-- MAGIC customer_data.createOrReplaceTempView("customer_temp_view")
-- MAGIC ## display EVent log data frame
-- MAGIC display(event_log)

-- COMMAND ----------

-- or show custome temp view in the SQL
select * from customer_temp_view

-- COMMAND ----------

-- MAGIC %python
-- MAGIC ## you can pass variables between ptyhon and SQL
-- MAGIC print(DA.schema_name)
-- MAGIC spark.conf.set("var.customersTable", f'{DA.schema_name}.customers') # make sure you have "." in the variable name

-- COMMAND ----------

-- Check the ingested customers table 
select * from ${var.customersTable}

-- COMMAND ----------

USE ${DA.schema_name};
-- lets check how our silver table generated by DLT looks
select * from sales_orders_cleaned

-- COMMAND ----------

-- lets check how our gold table generated by DLT looks
select * from sales_order_in_chicago