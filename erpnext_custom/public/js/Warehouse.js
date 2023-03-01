frappe.ui.form.on('Warehouse', {
refresh: function(frm) {
frm.add_custom_button("Show Target", function () {
	frappe.route_options = {
		to_warehouse : frm.doc.name
	},
	frappe.set_route("List", "Stock Entry");
});
frm.add_custom_button("Show Source", function () {
	frappe.route_options = {
		from_warehouse : frm.doc.name
	},
	frappe.set_route("List", "Stock Entry");
});
}
})