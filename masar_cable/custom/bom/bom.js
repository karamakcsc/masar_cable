frappe.ui.form.on("BOM Operation", "operation", function(frm, cdt, cdn) {
	var d = locals[cdt][cdn];
	if(!d.operation) return;

	frappe.call({
		"method": "frappe.client.get",
		args: {
			doctype: "Operation",
			name: d.operation
		},
		callback: function (data) {
			if(data.message.description) {
				frappe.model.set_value(d.doctype, d.name, "operation_rate", data.message.operation_rate);
			}
		}
	});
});


frappe.ui.form.on("BOM", "setup", function(frm) {
        frappe.call({
            method:"masar_cable.custom.bom.bom.execute_override",
            callback: function(r){
            }
        })

});
