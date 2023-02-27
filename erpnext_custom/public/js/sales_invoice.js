frappe.ui.form.on("Sales Invoice", {
    customer: function(frm) {
        frappe.call({
            method:"erpnext_custom.erpnext_custom.doc_event.sales_invoice.allow_discount",
            args:{customer:frm.doc.customer},
            callback: function(r){
                if (r.message == 0) {
                    frm.set_value("additional_discount_percentage",r.message);
                    frm.set_value("discount_amount",r.message);
                    frm.set_value("is_cash_or_non_trade_discount",r.message);
                    frm.set_df_property("additional_discount_percentage", 'read_only',1);
                    frm.set_df_property("discount_amount", 'read_only',1);
                    frm.set_df_property("is_cash_or_non_trade_discount", 'read_only',1);
                }
                else{
                    frm.set_df_property("additional_discount_percentage", 'read_only',0);
                    frm.set_df_property("discount_amount", 'read_only',0);
                    frm.set_df_property("is_cash_or_non_trade_discount", 'read_only',0);
                }
             
            }
        })
		
	},
});