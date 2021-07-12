frappe.ui.form.on("Work Order", "setup", function(frm) {
        frappe.call({
            method:"masar_cable.custom.work_order.work_order.execute_override",
            callback: function(r){
            }
        })

});
