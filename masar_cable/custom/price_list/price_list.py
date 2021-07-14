import frappe
import erpnext
import math
from frappe.utils import flt, get_datetime, getdate, date_diff, cint, nowdate, get_link_to_form, time_diff_in_hours
from frappe import throw, msgprint, _

@frappe.whitelist()
def apply_vfcu(doctype,name,lme1,lme2):
    pl_doc = frappe.get_doc(doctype,name)

    for d in frappe.db.get_list('Item Price',filters={'price_list': name},fields=['name','item_code']):
        item_doc = frappe.get_doc("Item", d.item_code)
        item_price_doc = frappe.get_doc("Item Price", d.name)
        item_price_doc.price_list_rate = item_price_doc.price_list_rate + item_doc.vfcu * (flt(lme1) - flt(lme2))
        item_price_doc.save()
