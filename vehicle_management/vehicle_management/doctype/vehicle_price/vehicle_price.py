# Copyright (c) 2024, darthVader and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VehiclePrice(Document):
	def before_save(self):
		self.sale_price = self.company_price+self.customer_price
		total_quantity = 0
		total_amount = 0
		for row in self.other_vehicle_items:
			total_quantity += row.quantity
			total_amount += row.amount
		self.total_quantity = total_quantity
		self.total_amount = total_amount
		self.grand_total = self.sale_price + self.total_amount
