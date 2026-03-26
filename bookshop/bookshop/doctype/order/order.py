# Copyright (c) 2026, shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc


class Order(Document):
	def validate(self):
		if not self.customer:
			frappe.throw("Customer name is required")
		
@frappe.whitelist()
def make_todo(target_doc=None):
    referenceType = frappe.flags.args.referenceType
    source_name = frappe.flags.args.source_name
    try:
        target_doc = get_mapped_doc(
            referenceType,
            source_name,
            {
                referenceType: {
                    "doctype": "ToDo",
                    "field_map": {
                        "name": "reference_name",
                        "doctype": "reference_type"
                    },
                },
            },
            target_doc
        )
        return target_doc
    except Exception as e:
        frappe.throw(f"An error occurred while creating ToDo: {str(e)}")