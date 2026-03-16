# Copyright (c) 2026, shubh and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Order(Document):
	def validate(self):
		frappe.msgprint("Validation logic executed for Order")
		if not self.customer:
			frappe.throw("Customer name is required")
		
