import pytest
from src.google_sheets_utility.delivery_sheet import DeliverySheet
from tests.conftest import GspreadTest
import pandas as pd
import vcr
import json

"""
This test is responsible for sanity checking.
"""


class DeliverySheetDistrictValidationTest(GspreadTest):

    def test_delivery_list_contains_valid_district(self):
        delivery_sheet = DeliverySheet()
        delivery_sheet = delivery_sheet.delivery_sheet
        # To Do
        # Need to Load the Sheet
        # Pick up the col "District"
        # Iterate through and make sure all are valid
        df = pd.DataFrame(delivery_sheet.get_all_records())
        self.assertTrue(True)

    def test_xyz(self):
        file = open("C:\\Users\\rowsh\\PycharmProjects\\gspread\\src\\district\\districts.json"
                    , encoding='utf-8')
        data = json.load(file)
        print(data)
        self.assertTrue(True)




