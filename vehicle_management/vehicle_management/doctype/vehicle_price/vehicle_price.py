# Copyright (c) 2024, darthVader and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class VehiclePrice(Document):
	def before_save(doc, method):
    # Your logic here
		doc.sale_price = doc.company_price+doc.customer_price  
