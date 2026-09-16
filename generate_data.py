from faker import Faker
import pandas as pd
import random

fake = Faker()
Faker.seed(42)
random.seed(42)

# --- FACULTIES & DEPARTMENTS ---
departments_list = [
    ("Civil Engineering", "Faculty of Engineering"),
    ("Electrical/Electronic Engineering", "Faculty of Engineering"),
    ("Mechanical Engineering", "Faculty of Engineering"),
    ("Chemical Engineering", "Faculty of Engineering"),
    ("Agricultural Engineering", "Faculty of Engineering"),
    ("Petroleum Engineering", "Faculty of Engineering"),
    ("Information and Communication Technology", "Faculty of Engineering"),

    ("Computer Science", "Faculty of Science"),
    ("Physics", "Faculty of Science"),
    ("Chemistry", "Faculty of Science"),
    ("Biochemistry", "Faculty of Science"),
    ("Microbiology", "Faculty of Science"),
    ("Mathematics", "Faculty of Science"),
    ("Statistics", "Faculty of Science"),
    ("Geology", "Faculty of Science"),

    ("Business Administration", "Faculty of Management Sciences"),
    ("Accounting", "Faculty of Management Sciences"),
    ("Banking and Finance", "Faculty of Management Sciences"),
    ("Marketing", "Faculty of Management Sciences"),
    ("Public Administration", "Faculty of Management Sciences"),

    ("Economics", "Faculty of Social Sciences"),
    ("Political Science", "Faculty of Social Sciences"),
    ("Sociology", "Faculty of Social Sciences"),
    ("Psychology", "Faculty of Social Sciences"),
    ("Mass Communication", "Faculty of Social Sciences"),

    ("English Language", "Faculty of Arts"),
    ("History and International Studies", "Faculty of Arts"),
    ("Linguistics", "Faculty of Arts"),
    ("Theatre Arts", "Faculty of Arts"),
    ("Religious Studies", "Faculty of Arts"),

    ("Public and Private Law", "Faculty of Law"),
    ("Commercial and Property Law", "Faculty of Law"),
    ("International Law", "Faculty of Law"),

    ("Educational Foundations", "Faculty of Education"),
    ("Curriculum Studies", "Faculty of Education"),
    ("Guidance and Counselling", "Faculty of Education"),
    ("Vocational and Technical Education", "Faculty of Education"),

    ("Agricultural Economics", "Faculty of Agriculture"),
    ("Animal Science", "Faculty of Agriculture"),
    ("Crop Science", "Faculty of Agriculture"),
    ("Soil Science", "Faculty of Agriculture"),
    ("Forestry and Wildlife", "Faculty of Agriculture"),

    ("Architecture", "Faculty of Environmental Sciences"),
    ("Urban and Regional Planning", "Faculty of Environmental Sciences"),
    ("Estate Management", "Faculty of Environmental Sciences"),
    ("Quantity Surveying", "Faculty of Environmental Sciences"),

    ("Medicine and Surgery", "Faculty of Health Sciences"),
    ("Nursing Science", "Faculty of Health Sciences"),
    ("Pharmacy", "Faculty of Health Sciences"),
    ("Public Health", "Faculty of Health Sciences"),
    ("Medical Laboratory Science", "Faculty of Health Sciences"),
]

faculties_list = sorted(set(fac for _, fac in departments_list))

faculties_df = pd.DataFrame([
    {"faculty_id": f"FAC{i+1:03d}", "faculty_name": f, "dean": fake.name()}
    for i, f in enumerate(faculties_list)
])
faculty_id_map = dict(zip(faculties_df["faculty_name"], faculties_df["faculty_id"]))

departments_df = pd.DataFrame([
    {
        "department_id": f"DEPT{i+1:03d}",
        "department_name": name,
        "faculty_id": faculty_id_map[fac],
        "head_of_department": fake.name(),
    }
    for i, (name, fac) in enumerate(departments_list)
])
dept_id_map = dict(zip(departments_df["department_name"], departments_df["department_id"]))
dept_names = list(dept_id_map.keys())

# --- ACADEMIC LEVEL STRUCTURE ---
degree_levels = {
    "Undergraduate": ["100", "200", "300", "400", "500"],
    "Masters": ["MSc Year 1", "MSc Year 2"],
    "PhD": ["PhD Year 1", "PhD Year 2", "PhD Year 3", "PhD Year 4+"],
}
degree_weights = [0.80, 0.15, 0.05]  # most students are undergrads

semesters = ["First", "Second"]

# --- STUDENTS ---
student_records = []
for i in range(2000):
    dept = random.choice(dept_names)
    degree = random.choices(list(degree_levels.keys()), weights=degree_weights)[0]
    level = random.choice(degree_levels[degree])
    student_records.append({
        "student_id": f"STU{i+1:05d}",
        "name": fake.name(),
        "department_id": dept_id_map[dept],
        "degree_level": degree,
        "level": level,
        "gender": random.choice(["Male", "Female"]),
        "age": random.randint(17, 45) if degree != "Undergraduate" else random.randint(17, 30),
        "gpa": round(random.uniform(1.0, 5.0), 2),
        "attendance_rate": round(random.uniform(0.4, 1.0), 2),
        "enrollment_year": random.randint(2018, 2025),
        "status": random.choices(["Active", "Graduated", "Dropped Out"], weights=[0.6, 0.3, 0.1])[0],
        "tuition_status": random.choices(["Paid", "Outstanding"], weights=[0.8, 0.2])[0],
        "scholarship": random.choices(["Yes", "No"], weights=[0.15, 0.85])[0],
    })
students_df = pd.DataFrame(student_records)
student_ids = students_df["student_id"].tolist()

# --- STAFF ---
staff_roles = ["Lecturer I", "Lecturer II", "Senior Lecturer", "Associate Professor",
               "Professor", "Head of Department", "Teaching Assistant", "Lab Technician"]
staff_records = []
for i in range(300):
    dept = random.choice(dept_names)
    staff_records.append({
        "staff_id": f"STF{i+1:05d}",
        "name": fake.name(),
        "department_id": dept_id_map[dept],
        "role": random.choice(staff_roles),
        "gender": random.choice(["Male", "Female"]),
        "years_of_service": random.randint(1, 30),
        "hire_year": random.randint(1995, 2025),
        "employment_type": random.choices(["Full-time", "Part-time", "Contract"], weights=[0.75, 0.15, 0.10])[0],
    })
staff_df = pd.DataFrame(staff_records)
staff_ids = staff_df["staff_id"].tolist()

# --- COURSES ---
course_records = []
for dept_name, dept_id in dept_id_map.items():
    for n in range(1, 6):
        code = f"{dept_name[:3].upper()}{100*random.choice([1,2,3,4,5]) + n}"
        course_records.append({
            "course_code": code,
            "title": f"{dept_name} Topic {n}",
            "department_id": dept_id,
            "credit_units": random.choice([2, 3, 4]),
            "semester": random.choice(semesters),
        })
courses_df = pd.DataFrame(course_records)
course_codes = courses_df["course_code"].tolist()

# --- ENROLLMENTS ---
enrollment_records = []
eid = 1
for student_id in student_ids:
    num_courses = random.randint(4, 7)
    for course_code in random.sample(course_codes, num_courses):
        enrollment_records.append({
            "enrollment_id": f"ENR{eid:06d}",
            "student_id": student_id,
            "course_code": course_code,
            "year": random.randint(2020, 2025),
            "semester": random.choice(semesters),
            "grade": round(random.uniform(0, 100), 1),
        })
        eid += 1
enrollments_df = pd.DataFrame(enrollment_records)

# --- BUILDINGS ---
building_records = []
for i, (dept_name, dept_id) in enumerate(dept_id_map.items()):
    building_records.append({
        "building_id": f"BLD{i+1:03d}",
        "building_name": f"{dept_name} Building",
        "department_id": dept_id,
        "capacity": random.randint(100, 600),
    })
buildings_df = pd.DataFrame(building_records)

# --- LIBRARY USAGE ---
library_records = []
for i in range(3000):
    library_records.append({
        "usage_id": f"LIB{i+1:06d}",
        "student_id": random.choice(student_ids),
        "visit_date": fake.date_between(start_date="-2y", end_date="today"),
        "hours_spent": round(random.uniform(0.5, 6.0), 1),
    })
library_df = pd.DataFrame(library_records)

# --- EXTRACURRICULAR ---
activities_list = ["Debate Club", "Football Team", "Drama Society", "Tech Hub", "Choir",
                    "Chess Club", "Volunteer Corps", "Entrepreneurship Club"]
extracurricular_records = []
for i in range(1500):
    extracurricular_records.append({
        "activity_id": f"ACT{i+1:06d}",
        "student_id": random.choice(student_ids),
        "activity_name": random.choice(activities_list),
        "semester": random.choice(semesters),
        "year": random.randint(2020, 2025),
    })
extracurricular_df = pd.DataFrame(extracurricular_records)

# --- SEMINAR / EVENT ATTENDANCE ---
seminar_list = ["Career Readiness Workshop", "AI in Industry Talk", "Research Methods Seminar",
                 "Entrepreneurship Bootcamp", "Cybersecurity Awareness Day"]
seminar_records = []
for i in range(1200):
    attendee_type = random.choice(["student", "staff"])
    attendee_id = random.choice(student_ids) if attendee_type == "student" else random.choice(staff_ids)
    seminar_records.append({
        "attendance_id": f"SEM{i+1:06d}",
        "attendee_id": attendee_id,
        "attendee_type": attendee_type,
        "seminar_name": random.choice(seminar_list),
        "date": fake.date_between(start_date="-2y", end_date="today"),
    })
seminar_df = pd.DataFrame(seminar_records)

# --- SAVE ALL ---
faculties_df.to_csv("data/faculties.csv", index=False)
departments_df.to_csv("data/departments.csv", index=False)
students_df.to_csv("data/students.csv", index=False)
staff_df.to_csv("data/staff.csv", index=False)
courses_df.to_csv("data/courses.csv", index=False)
enrollments_df.to_csv("data/enrollments.csv", index=False)
buildings_df.to_csv("data/buildings.csv", index=False)
library_df.to_csv("data/library_usage.csv", index=False)
extracurricular_df.to_csv("data/extracurricular.csv", index=False)
seminar_df.to_csv("data/seminar_attendance.csv", index=False)

print("Generated:")
print(f"  {len(faculties_df)} faculties")
print(f"  {len(departments_df)} departments")
print(f"  {len(students_df)} students (Undergrad/Masters/PhD)")
print(f"  {len(staff_df)} staff")
print(f"  {len(courses_df)} courses")
print(f"  {len(enrollments_df)} enrollments")
print(f"  {len(buildings_df)} buildings")
print(f"  {len(library_df)} library visits")
print(f"  {len(extracurricular_df)} extracurricular records")
print(f"  {len(seminar_df)} seminar attendance records")
