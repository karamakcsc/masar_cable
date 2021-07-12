import frappe
import erpnext
from frappe import throw, msgprint, _
from erpnext.manufacturing.doctype.work_order.work_order import WorkOrder


class CustomWorkOrder(WorkOrder):
	def onload(self):
		self.execute_override(self)
		super(WorkOrder, self).onload(self)

	def custom_set_work_order_operations(self):
			"""Fetch operations from BOM and set in 'Work Order'"""

			self.set('operations', [])

			if not self.bom_no:
				return

			if self.use_multi_level_bom:
				bom_list = frappe.get_doc("BOM", self.bom_no).traverse_tree()
			else:
				bom_list = [self.bom_no]

			operations = frappe.db.sql("""
				select
					operation, description, workstation, idx,
					base_hour_rate as hour_rate, operation_rate, time_in_mins,
					"Pending" as status, parent as bom, batch_size, sequence_id
				from
					`tabBOM Operation`
				where
					 parent in (%s) order by idx
			"""	% ", ".join(["%s"]*len(bom_list)), tuple(bom_list), as_dict=1)

			self.set('operations', operations)

			if self.use_multi_level_bom and self.get('operations') and self.get('items'):
				raw_material_operations = [d.operation for d in self.get('items')]
				operations = [d.operation for d in self.get('operations')]

				for operation in raw_material_operations:
					if operation not in operations:
						self.append('operations', {
							'operation': operation
						})

			self.calculate_time()

	def custom_calculate_operating_cost(self):
		self.planned_operating_cost, self.actual_operating_cost = 0.0, 0.0
		frappe.throw(("Original"))
		for d in self.get("operations"):
			d.planned_operating_cost = flt(d.hour_rate) * (flt(d.time_in_mins) / 60.0)
			d.actual_operating_cost = flt(d.hour_rate) * (flt(d.actual_operation_time) / 60.0)

			self.planned_operating_cost += flt(d.planned_operating_cost)
			self.actual_operating_cost += flt(d.actual_operating_cost)

		variable_cost = self.actual_operating_cost if self.actual_operating_cost \
			else self.planned_operating_cost
		self.total_operating_cost = flt(self.additional_operating_cost) + flt(variable_cost)

	def override_work_order(self,method):
		WorkOrder.set_work_order_operations = self.custom_set_work_order_operations
		WorkOrder.calculate_operating_cost = self.custom_calculate_operating_cost

	def execute_override(self,method):
		self.override_work_order(self)
		#frappe.throw(("Custom"))
