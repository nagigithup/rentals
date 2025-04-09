# Copyright (c) 2025, nagi and Contributors
# See license.txt
import frappe
from frappe.tests import IntegrationTestCase, UnitTestCase


# On IntegrationTestCase, the doctype test records and all
# link-field test record dependencies are recursively loaded
# Use these module variables to add/remove to/from that list
EXTRA_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]
IGNORE_TEST_RECORD_DEPENDENCIES = []  # eg. ["User"]


class UnitTestDriver(UnitTestCase):
	"""
	Unit tests for Driver.
	Use this class for testing individual functions and methods.
	"""

	def test_full_name_correctly_set(self):
		test_driver=frappe.new_doc("Driver")
		test_driver.first_name="Joun"
		test_driver.last_name="Doe"
		test_driver.license_number="JUdff"
		test_driver.save()

		self.assertEqual(test_driver.full_name, "Joun Doe" )


class IntegrationTestDriver(IntegrationTestCase):
	"""
	Integration tests for Driver.
	Use this class for testing interactions between multiple components.
	"""

	pass
