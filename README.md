Project overview

This document describes an independently designed and built data engineering project: a synthetic, university-wide dataset and an accompanying PySpark data processing pipeline, deployed with a public interactive dashboard. I undertook this project to demonstrate end-to-end data engineering capability across a realistic, multi-entity institutional dataset, going beyond processing a single flat file to model how data genuinely lives inside an organisation: spread across related tables that only produce meaningful insight once properly joined and aggregated.
I designed and generated the entire dataset myself, rather than using a pre-existing public dataset, so that I could model a realistic relational structure and practice the kind of multi-table join and aggregation logic used in professional data engineering work

What I built
2.1 Synthetic university dataset (generate_data.py)
Using the Faker Python library, I designed and generated ten related tables covering the operational scope of a university
<img width="777" height="516" alt="image" src="https://github.com/user-attachments/assets/500b23a6-eeeb-4a22-99dd-1459cc030f90" />

