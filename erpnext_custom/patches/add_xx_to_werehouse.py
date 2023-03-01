import frappe
def execute():
    frappe.db.sql("""
    update tabWarehouse set xx='0'
    """)

#bench migrate
