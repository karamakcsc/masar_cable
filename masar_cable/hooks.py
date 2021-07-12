# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "masar_cable"
app_title = "Masar Cable"
app_publisher = "KCSC"
app_description = "Custom App for Cables Industry"
app_icon = "octicon octicon-file-directory"
app_color = "blue"
app_email = "info@kcsc.com.jo"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/masar_cable/css/masar_cable.css"
# app_include_js = "/assets/masar_cable/js/masar_cable.js"

# include js, css files in header of web template
# web_include_css = "/assets/masar_cable/css/masar_cable.css"
# web_include_js = "/assets/masar_cable/js/masar_cable.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "masar_cable.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "masar_cable.install.before_install"
# after_install = "masar_cable.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "masar_cable.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }



#doc_events = {
# 	"Work Order": {
# 		"onload": "masar_cable.custom.work_order.work_order.execute_override"
#		"before_insert": "masar_cable.custom.work_order.work_order.execute_override"
#	}
# }

doctype_js = {
    "BOM" : "custom/bom/bom.js",
    "Work Order" : "custom/work_order/work_order.js"
 }

#override_doctype_class = {
#	'Work Order': 'masar_cable.overrides.overrides.CustomWorkOrder'
#}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"masar_cable.tasks.all"
# 	],
# 	"daily": [
# 		"masar_cable.tasks.daily"
# 	],
# 	"hourly": [
# 		"masar_cable.tasks.hourly"
# 	],
# 	"weekly": [
# 		"masar_cable.tasks.weekly"
# 	]
# 	"monthly": [
# 		"masar_cable.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "masar_cable.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "masar_cable.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "masar_cable.task.get_dashboard_data"
# }

fixtures = [
    {"dt": "Custom Field", "filters": [
        [
            "name", "in", [
                "Item-size",
		"Item-rated_voltage",
		"Item-standard",
		"Workstation-machine_code",
		"Operation-operation_code",
                "Item-conductor_material",
                "Item-conductor_shape",
                "Item-conductor_no",
                "Item-actual_cross_secarea_mm2",
                "Item-conductor_dimension_height_mm_",
		"Item-conductor_dimension_width_mm_",
		"Item-insulation_material",
		"Item-insulation_color",
		"Item-insulation_core_sector_hight_mm",
		"Item-insulation_core_sector_width_approx_mm",
		"Item-cores_laidup_assem_dia",
		"Item-insulation_thickness_mm",
		"Item-binding_tape_material",
		"Item-binding_dimension_height",
		"Item-binding_dimension_width",
		"Item-binding_tape_diameter",
		"Item-binding_tape_total_cov",
		"Item-binding_material",
		"Item-binding_color",
		"Item-binding_diameter",
		"Item-binding_tolerance",
		"Item-binding_thickness_mm",
		"Item-armour_material",
		"Item-armour_construction",
		"Item-armour_wires_strips_no",
		"Item-armour_diameter_mm",
		"Item-armour_total_cov",
		"Item-sheathing_material",
		"Item-sheathing_color",
		"Item-sheathing_over_all_diameter",
		"Item-sheathing_thickness",
		"Item-conductor_weight",
		"Item-insulation_weight",
		"Item-binding_tape_weight",
		"Item-pol_tape_weight",
		"Item-drain_wire_weight",
		"Item-al_foil_weight",
		"Item-bedding_weight",
		"Item-armour_weight",
		"Item-sheathing_weight",
		"Item-cable_weight",
		"Item-cu",
		"Item-column_break_73",
		"Item-column_break_69",
		"Item-column_break_65",
		"Item-specification_cables_and_wires",
		"Item-bom",
		"Item-conductor",
		"Item-insulation",
		"Item-binding_tape",
		"Item-binding",
		"Item-armour",
		"Item-sheathing"
            ]
        ]
    ]}
]
