import frappe
def create_new_stock_entry(doc):
    if doc.material_request_type == 'Material Transfer':
        material_request_type = doc.material_request_type
        material_from_warehouse = doc.set_from_warehouse
        material_to_warehouse = doc.set_warehouse

        stock_entry_doc= frappe.new_doc("Stock Entry")
        stock_entry_doc.stock_entry_type = material_request_type
        stock_entry_doc.from_warehouse = material_from_warehouse
        stock_entry_doc.to_warehouse = material_to_warehouse

        for material_item in doc.items:
            stock_entry_doc.append("items", {
                "item_code":material_item.item_code,
                "qty": material_item.qty})
    stock_entry_doc.insert(ignore_permissions=True)
    stock_entry_doc.submit()