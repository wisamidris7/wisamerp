# Copyright (c) 2020, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt


# import frappe
from frappe.model.document import Document


class POSInvoiceReference(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		customer: DF.Link
		grand_total: DF.Currency
		is_return: DF.Check
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		pos_invoice: DF.Link
		posting_date: DF.Date
		return_against: DF.Link | None
	# end: auto-generated types

	pass
