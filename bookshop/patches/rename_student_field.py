import frappe
from frappe.model.utils.rename_field import rename_field

def execute():
    rename_field("Student", "student", "student_name")