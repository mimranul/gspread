import json
from statistics import median, mode, mean

import geopy.distance
import pandas as pd
import pytest

from src.google_sheets_utility.delivery_sheet import DeliverySheet
from tests.conftest import GspreadTest

"""
This test is responsible for sanity checking.
"""


@pytest.fixture()
def global_var():
    var = pytest.district_json_file
    var = pytest.data


def setup_module():
    pytest.district_json_file = "C:\\Users\\rowsh\\PycharmProjects\\gspread\\src\\district\\districts.json"


def load_districts_json_file():
    with open(pytest.district_json_file, encoding='utf-8') as file:
        data = json.load(file)
    return data


class DeliverySheetDistrictValidationTest(GspreadTest):
    def test_delivery_list_contains_valid_district(self):
        delivery_sheet = DeliverySheet()
        delivery_sheet = delivery_sheet.delivery_sheet
        df = pd.DataFrame(delivery_sheet.get_all_records())
        self.assertTrue(True, "The delivery sheet contains invalid districts")

    def test_districts_json_file_can_be_loaded(self):
        data = load_districts_json_file()
        self.assertTrue(data is not None, "Could not load data from json file")

    def test_districts_json_file_contains_64_districts(self):
        data = load_districts_json_file()

        self.assertTrue(len(data['districts']) == 64, "The length of the districts in the list is more then 64")

    def test_each_district_name_appears_once_in_the_list(self):
        """
        Purpose of this test is to make sure the districs.json file has 64 districts
        """
        data = load_districts_json_file()
        districts_info_list = data['districts']
        districts_name = set()

        for district_info in districts_info_list:
            districts_name.add(district_info.get('name'))

        self.assertTrue(len(districts_name) == 64)

    def test_each_district_has_unique_longitude_and_len_combination(self):
        """
        Purpose of this test is to make sure the long and lat combination of a district is unique
        """
        data = load_districts_json_file()
        districts_info_list = data['districts']

        longs = set()
        lats = set()
        districts = set()

        """
        the long and lat combination will be unique if the number of districts, number of longs in the list and 
        number of lats in the list is equal. 
        """
        for district_info in districts_info_list:
            longs.add(district_info.get('long'))
            lats.add(district_info.get('lat'))
            districts.add(district_info.get('name'))

        self.assertTrue(len(longs) == len(districts))
        self.assertTrue(len(lats) == len(districts))
        self.assertTrue(len(longs) == len(lats))

    def test_distance_between_districts_are_statistically_accurate(self):
        """
        The purpose of the test is to make sure the JSON object file contains statistically
        accurate long and lat values
        """
        data = load_districts_json_file()
        districts_info_list = data['districts']

        district_long_lat_dict = dict()

        for district in districts_info_list:
            district_long_lat_dict.update({district.get('name'): [district.get('lat'), district.get('long')]})

        distances = []
        for i in range(len(district_long_lat_dict.keys())):
            for j in range(len(district_long_lat_dict.keys())):
                distance = geopy.distance. \
                    geodesic(district_long_lat_dict.get(list(district_long_lat_dict.keys())[i]),
                             district_long_lat_dict.get(list(district_long_lat_dict.keys())[j])).km
                distances.append(distance)
                if i != j:
                    distances.append(distance)

        self.assertTrue(int(mean(distances)) == 202, "The mean distance between district is no accurate")
        self.assertTrue(int(mode(distances)) == 0, "The mode distance between district is no accurate")
        self.assertTrue(int(median(distances)) == 190, "The median distance between district is no accurate")
