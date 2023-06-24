import os


import pytest

from src.google_sheets_utility.delivery_sheet import DeliverySheet

from .conftest import GspreadTest

class SpreadsheetTest(GspreadTest):

    @pytest.mark.vcr()
    def test_secret_file_exists(self):
        delivery_sheet = DeliverySheet()
        self.assertTrue(os.path.exists(delivery_sheet.secret_file))

    @pytest.mark.vcr()
    def test_spread_sheet_can_be_load(self):
        delivery_sheet = DeliverySheet()
        self.assertTrue(delivery_sheet.delivery_sheet.title.__eq__(delivery_sheet.spread_sheet_delivery_sheet))

    @pytest.mark.vcr()
    def test_spread_sheet_has_file_name(self):
        delivery_sheet = DeliverySheet()
        self.assertTrue(delivery_sheet.spread_sheet_file_name.__eq__(delivery_sheet.delivery_sheet.spreadsheet.title))

    @pytest.mark.vcr()
    def test_file_does_not_have_zero_rows(self):
        delivery_sheet = DeliverySheet()
        ## Need to add logic about rows
        self.assertTrue(True)

    @pytest.mark.vcr()
    def test_file_does_not_have_zero_coloumns(self):
        delivery_sheet = DeliverySheet()
        ## Need to add logic about coloumns
        self.assertTrue(True)

