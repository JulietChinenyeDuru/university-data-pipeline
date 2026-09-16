import streamlit as st
import pandas as pd

st.title("University Data Pipeline Dashboard")
st.caption("Synthetic university-wide data — faculties, departments, students, and staff")

gpa_by_faculty = pd.read_csv("output/gpa_by_faculty.csv")
dropout_by_level = pd.read_csv("output/dropout_by_level.csv")
ratio = pd.read_csv("output/student_staff_ratio.csv")
avg_grade_by_dept = pd.read_csv("output/avg_grade_by_dept.csv")

st.subheader("Average GPA by faculty")
st.dataframe(gpa_by_faculty)
st.bar_chart(gpa_by_faculty.set_index("faculty_name")["avg_gpa"])

st.subheader("Dropout rate by degree level")
st.dataframe(dropout_by_level)
st.bar_chart(dropout_by_level.set_index("degree_level")["dropout_rate_pct"])

st.subheader("Student-to-staff ratio by department")
st.dataframe(ratio)
st.bar_chart(ratio.set_index("department_name")["student_staff_ratio"].head(15))

st.subheader("Average course grade by department")
st.dataframe(avg_grade_by_dept)
st.bar_chart(avg_grade_by_dept.set_index("department_name")["avg_course_grade"].head(15))
