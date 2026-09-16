cat > README.md << 'EOF'
University Data Pipeline

A synthetic university-wide data pipeline simulating a full institution — faculties, departments, students, staff, courses, enrollments, and campus engagement — built to demonstrate multi-table data engineering with PySpark.

What it does

Generates a realistic synthetic dataset modeled on a typical Nigerian university structure, then processes it through a PySpark pipeline with multiple joins and aggregations to surface institution-wide insights. Results are visualized in an interactive dashboard.

Live dashboard

[View the deployed dashboard](https://your-app-url.streamlit.app) *(update this link once deployed)*

 Data generated

10 faculties, 51 departments (Engineering, Science, Management Sciences, Social Sciences, Arts, Law, Education, Agriculture, Environmental Sciences, Health Sciences)
2,000 students across Undergraduate, Masters, and PhD levels
300 staff across academic ranks
255 courses with over 11,000 enrollment and grade records
51 buildings, 3,000 library visit records, 1,500 extracurricular records, 1,200 seminar attendance records**

 Tech stack

PySpark — multi-table joins and aggregations
Faker  synthetic data generation
pandas output handling
Streamlit — interactive dashboard

Pipeline stages

1. Generate — synthetic data creation across all entities (`generate_data.py`)
2. Extract — load all CSVs into Spark DataFrames
3. Transform/Join — join students, staff, departments, faculties, courses, and enrollments
4. Aggregate — compute:
   Average GPA by faculty
   Dropout rate by degree level
   Student-to-staff ratio by department
   Average course grade by department

 Running it locally

bash
python -m venv venv
source venv/Scripts/activate
pip install faker pandas pyspark streamlit
python generate_data.py
python etl.py
streamlit run dashboard.py



 Author

Juliet Chinenye Duru
EOF
