from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count, round as spark_round, when

spark = SparkSession.builder.appName("UniversityDataPipeline").getOrCreate()

faculties = spark.read.csv("data/faculties.csv", header=True, inferSchema=True)
departments = spark.read.csv("data/departments.csv", header=True, inferSchema=True)
students = spark.read.csv("data/students.csv", header=True, inferSchema=True)
staff = spark.read.csv("data/staff.csv", header=True, inferSchema=True)
courses = spark.read.csv("data/courses.csv", header=True, inferSchema=True)
enrollments = spark.read.csv("data/enrollments.csv", header=True, inferSchema=True)
library = spark.read.csv("data/library_usage.csv", header=True, inferSchema=True)

print("=== Row counts ===")
for name, df in [("faculties", faculties), ("departments", departments), ("students", students), ("staff", staff), ("courses", courses), ("enrollments", enrollments), ("library", library)]:
    print(f"{name}: {df.count()}")

students_full = students.join(departments, on="department_id", how="left").join(faculties, on="faculty_id", how="left")

gpa_by_faculty = students_full.groupBy("faculty_name").agg(spark_round(avg("gpa"), 2).alias("avg_gpa"), count("student_id").alias("student_count")).orderBy(col("avg_gpa").desc())
print("=== Average GPA by faculty ===")
gpa_by_faculty.show(truncate=False)

dropout_by_level = students.groupBy("degree_level").agg(count("student_id").alias("total"), spark_round(avg(when(col("status") == "Dropped Out", 1).otherwise(0)) * 100, 1).alias("dropout_rate_pct"))
print("=== Dropout rate by degree level ===")
dropout_by_level.show()

students_per_dept = students.groupBy("department_id").agg(count("student_id").alias("num_students"))
staff_per_dept = staff.groupBy("department_id").agg(count("staff_id").alias("num_staff"))
ratio = students_per_dept.join(staff_per_dept, on="department_id", how="left").join(departments, on="department_id", how="left").withColumn("student_staff_ratio", spark_round(col("num_students") / col("num_staff"), 1)).select("department_name", "num_students", "num_staff", "student_staff_ratio").orderBy(col("student_staff_ratio").desc())
print("=== Student-to-staff ratio by department ===")
ratio.show(truncate=False)

enrollments_dept = enrollments.join(courses, on="course_code", how="left").join(departments, on="department_id", how="left")
avg_grade_by_dept = enrollments_dept.groupBy("department_name").agg(spark_round(avg("grade"), 1).alias("avg_course_grade"), count("enrollment_id").alias("num_enrollments")).orderBy(col("avg_course_grade").desc())
print("=== Average course grade by department ===")
avg_grade_by_dept.show(truncate=False)

gpa_by_faculty.toPandas().to_csv("output/gpa_by_faculty.csv", index=False)
dropout_by_level.toPandas().to_csv("output/dropout_by_level.csv", index=False)
ratio.toPandas().to_csv("output/student_staff_ratio.csv", index=False)
avg_grade_by_dept.toPandas().to_csv("output/avg_grade_by_dept.csv", index=False)

print("Saved aggregated outputs to /output")
spark.stop()
