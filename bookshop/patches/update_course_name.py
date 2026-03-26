import frappe

def execute():
    frappe.db.sql("""
        UPDATE `tabCourse`
        SET name = 'C Foundation'
        WHERE name = 'Let Us C'
    """)