import frappe
import erpnext
import math
from frappe.utils import flt, get_datetime, getdate, date_diff, cint, nowdate, get_link_to_form, time_diff_in_hours
from frappe import throw, msgprint, _
from erpnext.manufacturing.doctype.bom.bom import BOM

#
# def custom_set_work_order_operations(self):
# 		"""Fetch operations from BOM and set in 'Work Order'"""
# 		self.set('operations', [])
# 		if not self.bom_no:
# 			return
#
# 		if self.use_multi_level_bom:
# 			bom_list = frappe.get_doc("BOM", self.bom_no).traverse_tree()
# 		else:
# 			bom_list = [self.bom_no]
#
# 		operations = frappe.db.sql("""
# 			select
# 				operation, description, workstation, idx,
# 				base_hour_rate as hour_rate, operation_rate, time_in_mins,
# 				"Pending" as status, parent as bom, batch_size, sequence_id
# 			from
# 				`tabBOM Operation`
# 			where
# 				 parent in (%s) order by idx
# 		"""	% ", ".join(["%s"]*len(bom_list)), tuple(bom_list), as_dict=1)
#
# 		self.set('operations', operations)
#
# 		if self.use_multi_level_bom and self.get('operations') and self.get('items'):
# 			raw_material_operations = [d.operation for d in self.get('items')]
# 			operations = [d.operation for d in self.get('operations')]
#
# 			for operation in raw_material_operations:
# 				if operation not in operations:
# 					self.append('operations', {
# 						'operation': operation
# 					})
#
# 		self.calculate_time()
# def custom_calculate_operating_cost(self):
# 		self.planned_operating_cost, self.actual_operating_cost = 0.0, 0.0
#
# 		for d in self.get("operations"):
# 			d.planned_operating_cost = flt(d.hour_rate) * (flt(d.time_in_mins) / 60.0)
# 			d.actual_operating_cost = flt(d.operation_rate) * (flt(self.qty))
#
# 			self.planned_operating_cost += flt(d.planned_operating_cost)
# 			self.actual_operating_cost += flt(d.actual_operating_cost)
#
# 		variable_cost = self.actual_operating_cost if self.actual_operating_cost \
# 			else self.planned_operating_cost
# 		self.total_operating_cost = flt(self.additional_operating_cost) + flt(variable_cost)
#
# def override_work_order():
# 	WorkOrder.set_work_order_operations = custom_set_work_order_operations
# 	WorkOrder.calculate_operating_cost = custom_calculate_operating_cost

@frappe.whitelist()
def execute_override():
    frappe.throw("Ghoul")
	#override_BOM()
