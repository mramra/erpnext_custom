import frappe
def execute():
    frappe.db.sql(""" update `tabBOM` set department= 'Accounts'  """)

#bench migrate