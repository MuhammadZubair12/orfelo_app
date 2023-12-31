from . import __version__ as app_version

app_name = "orfelo_app"
app_title = "Orfelo App"
app_publisher = "Muhammad Zubair"
app_description = "Country Indonasia orfelo.erpnext.com First contain Receivable accounts reports with custom field"
app_email = "experterp771@gmail.com"
app_license = "Orfelo"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/orfelo_app/css/orfelo_app.css"
# app_include_js = "/assets/orfelo_app/js/orfelo_app.js"
# app_include_js = "/assets/orfelo_app/js/controllers/transaction.js"

# include js, css files in header of web template
# web_include_css = "/assets/orfelo_app/css/orfelo_app.css"
# web_include_js = "/assets/orfelo_app/js/orfelo_app.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "orfelo_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

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

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "orfelo_app.utils.jinja_methods",
#	"filters": "orfelo_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "orfelo_app.install.before_install"
# after_install = "orfelo_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "orfelo_app.uninstall.before_uninstall"
# after_uninstall = "orfelo_app.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "orfelo_app.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
#	"*": {
#		"on_update": "method",
#		"on_cancel": "method",
#		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"orfelo_app.tasks.all"
#	],
#	"daily": [
#		"orfelo_app.tasks.daily"
#	],
#	"hourly": [
#		"orfelo_app.tasks.hourly"
#	],
#	"weekly": [
#		"orfelo_app.tasks.weekly"
#	],
#	"monthly": [
#		"orfelo_app.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "orfelo_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "orfelo_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "orfelo_app.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"orfelo_app.auth.validate"
# ]
