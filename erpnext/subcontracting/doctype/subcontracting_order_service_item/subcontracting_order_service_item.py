# Copyright (c) 2022, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class SubcontractingOrderServiceItem(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		amount: DF.Currency
		fg_item: DF.Link
		fg_item_qty: DF.Float
		item_code: DF.Link
		item_name: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		purchase_order_item: DF.Data | None
		qty: DF.Float
		rate: DF.Currency
	# end: auto-generated types

	pass
