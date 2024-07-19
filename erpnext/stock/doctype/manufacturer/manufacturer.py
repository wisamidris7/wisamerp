# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


from frappe.contacts.address_and_contact import load_address_and_contact
from frappe.model.document import Document


class Manufacturer(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		country: DF.Link | None
		full_name: DF.Data | None
		logo: DF.AttachImage | None
		notes: DF.SmallText | None
		short_name: DF.Data
		website: DF.Data | None
	# end: auto-generated types

	def onload(self):
		"""Load address and contacts in `__onload`"""
		load_address_and_contact(self)
