# Databricks notebook source
# MAGIC %pip install \
# MAGIC git+https://github.com/databricks-academy/dbacademy@v1.0.2 \
# MAGIC --quiet --disable-pip-version-check

# COMMAND ----------

# MAGIC %run ./_dataset_index

# COMMAND ----------

from dbacademy import dbgems
from dbacademy.dbhelper import DBAcademyHelper, Paths, CourseConfig, LessonConfig

# The following attributes are externalized to make them easy
# for content developers to update with every new course.

course_config = CourseConfig(course_code = "delp",
                             course_name = "data-engineer-learning-path",
                             data_source_name = "data-engineer-learning-path",
                             data_source_version = "v01",
                             install_min_time = "2 min",
                             install_max_time = "10 min",
                             remote_files = remote_files,
                             supported_dbrs = ["11.3.x-scala2.12", "11.3.x-photon-scala2.12", "11.3.x-cpu-ml-scala2.12"],
                             expected_dbrs = "11.3.x-scala2.12, 11.3.x-photon-scala2.12, 11.3.x-cpu-ml-scala2.12")

# Defined here for the majority of lessons, 
# and later modified on a per-lesson basis.
lesson_config = LessonConfig(name = None,
                             create_schema = True,
                             create_catalog = False,
                             requires_uc = False,
                             installing_datasets = True,
                             enable_streaming_support = False)

# COMMAND ----------

@DBAcademyHelper.monkey_patch
def clone_source_table(self, table_name, source_path, source_name=None):
    start = self.clock_start()

    source_name = table_name if source_name is None else source_name
    print(f"Cloning the \"{table_name}\" table from \"{source_path}/{source_name}\".", end="...")
    
    spark.sql(f"""
        CREATE OR REPLACE TABLE {table_name}
        SHALLOW CLONE delta.`{source_path}/{source_name}`
        """)
    
    print(self.clock_stopped(start))

