# Copyright (c) 2024, darthVader and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VehiclePrice(Document):
	def before_save(self):
    # Your logic here
		self.sale_price = self.company_price+self.customer_price  
