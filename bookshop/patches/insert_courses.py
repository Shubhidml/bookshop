import frappe

def execute():
    courses = [
        {"name": "Python Basics", "description": "Intro to Python", "course_duration": "3 Months"},
        {"name": "Java", "description": "Core Java", "course_duration": "4 Months"},
        {"name": "Web Dev", "description": "HTML CSS JS", "course_duration": "2 Months"},
        {"name": "AI", "description": "Intro to AI", "course_duration": "6 Months"},
        {"name": "ML", "description": "Machine Learning", "course_duration": "6 Months"},
    ]

    for c in courses:
        if not frappe.db.exists("Course", c["name"]):
            frappe.get_doc({
                "doctype": "Course",
                **c
            }).insert()