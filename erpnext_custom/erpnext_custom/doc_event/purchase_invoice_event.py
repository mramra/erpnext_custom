import frappe
def creat_purchase_receipt(doc,method):
    purchase_receipt_doc=frappe.new_doc("Purchase Receipt")
    purchase_receipt_doc.supplier = doc.supplier
    for sales_invoice_item in doc.items :
        purchase_receipt_doc.append("items",{"item_code":sales_invoice_item.item_code,
                                             "received_qty": sales_invoice_item.qty})
    purchase_receipt_doc.insert(ignore_permissions=True)
    purchase_receipt_doc.submit()
       