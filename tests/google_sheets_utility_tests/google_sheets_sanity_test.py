import os

import pytest

from src.google_sheets_utility import delivery_sheet
from src.google_sheets_utility.delivery_sheet import DeliverySheet
from src.mango.mango import Mango

from tests.conftest import GspreadTest

"""
This test is responsible for making sure
- Application can connect to the google sheet
- Some validation around the sheet is not empty
- The Sheet title bar
- 
"""


@pytest.fixture()
def global_var():
    pytest.delivery_sheet = 0


def setup_module():
    pytest.delivery_sheet = DeliverySheet()


def teardown_module():
    print("teardown_module")


class SpreadsheetSanityTest(GspreadTest):

    # @pytest.mark.google_sheets()
    # def test_secret_file_exists(self):
    #     self.assertTrue(os.path.exists(delivery_sheet.secret_file))
    #
    # @pytest.mark.google_sheets()
    # def test_spread_sheet_can_be_load(self):
    #     delivery_sheet = setup_before_test()
    #     self.assertTrue(delivery_sheet.title.__eq__(spread_sheet_delivery_sheet))

    @pytest.mark.google_sheets()
    def test_spread_sheet_has_file_name(self):
        self.assertTrue(
            pytest.delivery_sheet.spread_sheet_file_name.__eq__(pytest.delivery_sheet.spread_sheet_file_name))

    @pytest.mark.sanity()
    def test_file_does_not_have_zero_rows(self):
        self.assertTrue(pytest.delivery_sheet.delivery_sheet.row_count != 0)

    @pytest.mark.sanity()
    def test_file_does_not_have_zero_columns(self):
        self.assertTrue(pytest.delivery_sheet.delivery_sheet.col_count != 0)

    @pytest.mark.sanity()
    def test_file_does_not_have_zero_rows(self):
        self.assertTrue(pytest.delivery_sheet.delivery_sheet.row_count != 0)

    @pytest.mark.sanity()
    def test_file_has_more_than_four_columns(self):
        self.assertTrue(pytest.delivery_sheet.delivery_sheet.col_count > 4)

    @pytest.mark.sanity()
    def test_file_has_more_than_four_rows(self):
        self.assertTrue(pytest.delivery_sheet.delivery_sheet.row_count > 4)

    # To Do
    @pytest.mark.sanity()
    def test_the_sheet_title_has_name_of_mango_from_mango_common_list(self):
        # data = delivery_sheet.delivery_sheet.get_all_records()
        # print(data)
        # To Do:
        # Need to load the title bar and see if one of the cell contains a mango from the common mango
        # list
        mango = Mango()
        common_mango = mango.get_common_list_of_mango()

        self.assertTrue(True)

    # To Do
    @pytest.mark.sanity()
    def test_the_sheet_title_has_name_of_mango_from_mango_common_list(self):
        # data = delivery_sheet.delivery_sheet.get_all_records()
        # print(data)
        # To Do:
        # Need to load the title bar and see if one of the cell contains a mango from the common mango
        # list
        mango = Mango()
        common_mango = mango.get_common_list_of_mango()

        self.assertTrue(True)
