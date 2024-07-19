# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


# import frappe
from frappe.model.document import Document


class ShipmentParcel(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		count: DF.Int
		height: DF.Int
		length: DF.Int
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		weight: DF.Float
		width: DF.Int
	# end: auto-generated types

	pass
