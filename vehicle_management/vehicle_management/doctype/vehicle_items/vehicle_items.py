# Copyright (c) 2024, darthVader and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VehicleItems(Document):
	def before_save(self):
		self.amount = self.quantity*self.rate  
	def validate(self):
			