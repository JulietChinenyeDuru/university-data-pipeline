Project overview

This document describes an independently designed and built data engineering project: a synthetic, university-wide dataset and an accompanying PySpark data processing pipeline, deployed with a public interactive dashboard. I undertook this project to demonstrate end-to-end data engineering capability across a realistic, multi-entity institutional dataset, going beyond processing a single flat file to model how data genuinely lives inside an organisation: spread across related tables that only produce meaningful insight once properly joined and aggregated.
I designed and generated the entire dataset myself, rather than using a pre-existing public dataset, so that I could model a realistic relational structure and practice the kind of multi-table join and aggregation logic used in professional data engineering work

What I built
2.1 Synthetic university dataset (generate_data.py)
Using the Faker Python library, I designed and generated ten related tables covering the operational scope of a university:
Table	Records	Description
Faculties	10	Top-level academic divisions
Departments	51	Departments nested under each faculty, including Information and Communication Technology under Engineering
Students	2,000	Undergraduate, Masters, and PhD students with GPA, attendance, tuition and scholarship data
Staff	300	Academic staff across ranks, from Teaching Assistant to Professor
Courses	255	Courses assigned to departments
Enrollments	11,043	Individual student-course enrollments with per-course grades
Buildings	51	Departmental buildings and capacity
Library usage	3,000	Student library visit records
Extracurricular activities	1,500	Student participation in clubs and societies
Seminar attendance	1,200	Student and staff attendance at university events
