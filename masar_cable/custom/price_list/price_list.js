
frappe.ui.form.on ("Price List", "apply_vfcu", function(frm) {
  if(!frm.doc.current_lme) return;
  frm.set_value("lme2",frm.doc.lme1);
  frm.set_value("lme1",frm.doc.current_lme);
   frappe.call({
        method:"masar_cable.custom.price_list.price_list.apply_vfcu",
        args:{"doctype": "Price List","name":frm.doc.name,"lme1":frm.doc.lme1,"lme2":frm.doc.lme2},
        callback: function(r) {
          cur_frm.save();
          show_alert("Prices are changed",5);
        }
    });

  });
