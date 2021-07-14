frappe.ui.form.on("Quotation", "apply_vfcu", function(frm) {
show_alert("Prices are changed",5);
if(!frm.doc.current_lme) return;

frm.set_value("lme2",frm.doc.lme1);
frm.set_value("lme1",frm.doc.current_lme);
$.each(frm.doc.items, function(i, d) {
        frappe.call({
          "method": "frappe.client.get",
          args: {
            doctype: "Item",
            name: d.item_code
          },
          callback: function (data) {
            if(data.message.vfcu) {

              d.rate = d.rate+ data.message.vfcu *(frm.doc.lme1-frm.doc.lme2);
            }
          }
        });
    });
    cur_frm.save();
});
