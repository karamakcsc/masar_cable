import frappe
import erpnext
import math
from frappe.utils import flt, get_datetime, getdate, date_diff, cint, nowdate, get_link_to_form, time_diff_in_hours
from frappe import throw, msgprint, _

@frappe.whitelist()
def apply_vfcu(doctype,name):
	quotation_doc = frappe.get_doc(doctype, name)
	for d in quotation_doc.get("items"):
		item_doc = frappe.get_doc("Item", d.item_code)
		d.rate = d.rate+ item_doc.vfcu *(quotation_doc.lme1-quotation_doc.lme2);
		frappe.msgprint(str(d.rate))
