// Copyright (c) 2026, shubh and contributors
// For license information, please see license.txt

 frappe.ui.form.on("Order", {
 	unit_price(frm) {
    frm.set_value('total_price', frm.doc.quantity * frm.doc.unit_price)
 	},
    quantity(frm) {
        frm.set_value('total_price', frm.doc.quantity * frm.doc.unit_price)
    }
 });
