# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors and contributors
# For license information, please see license.txt


from frappe.model.document import Document


class MonthlyDistributionPercentage(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		month: DF.Data
		parent: DF.Data
		parentfield: DF.Data
		parenttype: DF.Data
		percentage_allocation: DF.Float
	# end: auto-generated types

	pass
