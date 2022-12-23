-- Databricks notebook source
-- MAGIC %run ./jobs/includes/Setup_2

-- COMMAND ----------

-- MAGIC %python
-- MAGIC ## how you can move varibale between ptyhon and SQL
-- MAGIC print(DA.schema_name)
-- MAGIC spark.conf.set("var.lesson_name", lesson_name) # make sure you have "." in the variable name

-- COMMAND ----------

select * from "${DA.schema_name}."

-- COMMAND ----------

select * from 
