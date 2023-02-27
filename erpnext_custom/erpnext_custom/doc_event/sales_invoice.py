import frappe
@frappe.whitelist()
def allow_discount(customer):
	doc=frappe.get_doc('Customer', customer)
	return doc.allow_discount
	