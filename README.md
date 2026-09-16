1. Project overview

This document describes an independently designed and built data engineering project: a synthetic, university-wide dataset and an accompanying PySpark data processing pipeline, deployed with a public interactive dashboard. I undertook this project to demonstrate end-to-end data engineering capability across a realistic, multi-entity institutional dataset, going beyond processing a single flat file to model how data genuinely lives inside an organisation: spread across related tables that only produce meaningful insight once properly joined and aggregated.

Designing a system architecture diagram for a data pipeline

<img width="1276" height="806" alt="image" src="https://github.com/user-attachments/assets/1c5bf220-ff7f-4b29-a3ca-76b0cf5e58f7" />


This is  the system architecture for the project: data generation feeding ten related CSV tables, through the PySpark ETL layer for joins and aggregations, into the deployed Streamlit dashboard


I designed and generated the entire dataset myself, rather than using a pre-existing public dataset, so that I could model a realistic relational structure and practice the kind of multi-table join and aggregation logic used in professional data engineering work

What I built

2.1 university dataset (generate_data.py)

Using the Faker Python library, I designed and generated ten related tables covering the operational scope of a university
<img width="777" height="516" alt="image" src="https://github.com/user-attachments/assets/500b23a6-eeeb-4a22-99dd-1459cc030f90" />

I modelled realistic population proportions rather than applying uniform randomness throughout. For example, and weighted student degree level so that 80% of 

students are Undergraduate, 15% Masters, and 5% PhD, reflecting typical university enrolment patterns. Ages, dropout probability, tuition status, and scholarship 

status were similarly weighted to reflect plausible real-world distributions rather than being evenly random.

2.2 PySpark ETL pipeline (etl.py)

I built a data pipeline using PySpark that extracts all ten datasets, joins them according to their real institutional relationships, and produces four aggregated analyses:
•	Average GPA by faculty — students joined through departments to faculties

•	Dropout rate by degree level — computed as a percentage of each degree level's student population

•	Student-to-staff ratio by department — two independently grouped counts (students per department, staff per department) joined together

•	Average course grade by department — enrollment records joined through courses to their parent department

This pipeline required working with genuine multi-table relational logic: resolving foreign keys between tables (department_id, faculty_id, course_code), grouping and aggregating at different levels of granularity, and joining previously independent aggregations back together (as in the student-to-staff ratio calculation).

2.3 Interactive dashboard (dashboard.py)

I used Streamlit to turn the pipeline's output into a live, publicly accessible dashboard, with tables and bar charts for each aggregation. This makes the pipeline's results reviewable by anyone with the link, without needing to run the code or inspect raw output files.

3. Results
Running the pipeline against the generated dataset produced the following findings


<img width="777" height="346" alt="image" src="https://github.com/user-attachments/assets/7316f83c-3d0c-4dc7-9b03-0a7d849a3ea1" />


. Technical skills demonstrated

•	Designing a normalised, multi-table relational data model from scratch, including primary/foreign key relationships across ten entities

•	Synthetic data generation using the Faker library, with weighted distributions reflecting realistic population proportions

•	Distributed data processing with PySpark, including multi-table joins, grouped aggregations, and derived metrics


•	End-to-end pipeline construction: extract, transform/join, aggregate, and load stages

•	Building and deploying a public, interactive data dashboard using Streamlit

•	Version control and public code hosting via Git and GitHub, including resolving merge conflicts and managing repository history

5. Relevance to this application

This project was undertaken independently, outside of any employment context, to demonstrate current, hands-on data engineering capability using industry-standard tools (PySpark, Python, Git, cloud-hosted deployment).


