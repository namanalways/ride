# Copyright (c) 2025, Naman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class RideBooking(Document):
	def before_save(self):
		total = self.price_per_km * self.estimated_km
		for service in self.services:
			total += service.amount
		self.total_amount = total