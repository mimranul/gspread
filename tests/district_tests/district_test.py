
from statistics import median, mode, mean

import geopy.distance

import pytest

from src.district.District import District

from tests.conftest import GspreadTest

"""
This test is responsible for sanity checking.
"""


@pytest.fixture()
def global_var():
    var = pytest.data


def setup_module():
    pytest.district_json_file = ""


class DivisionJsonFileTest(GspreadTest):
    @pytest.mark.district()
    def test_make_district_object(self):
        # Create a district object from the test data
        district = District()

        self.assertTrue(district.id == 1)
        self.assertTrue(district.division_id == 1)
        self.assertTrue(district.name == "")
        self.assertTrue(district.bn_name == "")
        self.assertTrue(district.lat == 1)
        self.assertTrue(district.long == 2)

    @pytest.mark.district()
    def test_districts_list_contains_64_districts(self):
        district = District()
        district_info_list = district.get_list_of_district_info_list()
        self.assertTrue(len(district_info_list) == 64)

    @pytest.mark.district()
    def test_districts_list_contains_dhaka_district(self, given_district="Dhaka"):
        district = District()
        district_list = district.get_list_of_districts()
        self.assertTrue(given_district in district_list)

    @pytest.mark.district()
    def test_districts_list_contains_district_spelling_error_corrections_april_2018(self):
        districts_with_spelling_error_correction_april_2018 = \
            ["Bogura", "Barishal", "Jashore", "Chattogram", "Cumilla"]
        district = District()
        districts = district.get_list_of_districts()

        excluded_from_correction = []
        for district_2018 in districts_with_spelling_error_correction_april_2018:
            if not district_2018 in districts:
                excluded_from_correction.append(district_2018)

        self.assertTrue(len(excluded_from_correction) == 0,
                        "The following Districts needs to be updated "
                        + str(excluded_from_correction))

    @pytest.mark.district()
    def test_distance_between_districts_statistics(self):
        district = District()

        distances = []
        bn_distances = []

        districts = district.get_list_of_districts()
        bn_districts = district.get_list_of_districts_bn_name()

        for i in range(len(districts)):
            j = i
            for j in range(len(districts)):
                coordinate_district_1 = district.get_coordinates_of_district_by_name(districts[i])
                coordinate_district_2 = district.get_coordinates_of_district_by_name(districts[j])

                bn_coordinate_district_1 = district.get_coordinates_of_district_by_bn_name(bn_districts[i])
                bn_coordinate_district_2 = district.get_coordinates_of_district_by_bn_name(bn_districts[j])

                self.assertEqual(coordinate_district_1, bn_coordinate_district_1, "Coordinates for queries aren't same")
                self.assertEqual(coordinate_district_2, bn_coordinate_district_2, "Coordinates for queries aren't same")

                distance = geopy.distance.geodesic(coordinate_district_1, coordinate_district_2).km
                if i != j:
                    distances.append(distance)

        self.assertTrue(int(mean(distances)) == 204, "The mean distance between district is not accurate")
        self.assertTrue(int(median(distances)) == 191, "The median distance between district is not accurate")
        self.assertTrue(int(mode(distances)) == 59, "The mode distance between district is not accurate")

    @pytest.mark.district()
    def test_each_district_can_be_load_by_id(self):
        district = District()
        districts_en_names = set()
        districts_bn_names = set()
        for i in range(65):
            district_en_name_found_by_id = district.get_name_of_district_by_id(str(i))
            district_bn_name_found_by_id = district.get_bn_name_of_district_by_id(str(i))
            if district_en_name_found_by_id is not None \
                    and not district.check_if_a_district_exists_by_name(district_en_name_found_by_id):
                districts_en_names.add(district_en_name_found_by_id)

            if district_bn_name_found_by_id is not None:
                districts_bn_names.add(district_en_name_found_by_id)

        self.assertEqual(len(districts_en_names), 64, "District could not be loaded with id")
        self.assertEqual(len(districts_bn_names), 64, "District could not be loaded with id")

    @pytest.mark.district()
    def test_district_can_not_be_load_by_invalid_id(self):
        district = District()
        districts = list()
        invalid_ids = ['-1', '-3', '-8', '65', '0', '70', '100']
        for invalid_id in invalid_ids:
            district_name_found_by_id = district.get_name_of_district_by_id(invalid_id)
            districts.append(district_name_found_by_id)

        self.assertEqual(len(districts), len(invalid_ids), "District could not be loaded with id")
