from statistics import median, mode, mean

import geopy.distance

import pytest

from src.division.Division import Division

from tests.conftest import GspreadTest

"""
This test is responsible for sanity checking.
"""


@pytest.fixture()
def global_var():
    var = pytest.data


def setup_module():
    pytest.division_json_file = ""


class DivisionJsonFileTest(GspreadTest):
    @pytest.mark.division()
    def test_make_division_object(self):
        # Create a division object from the test data
        division = Division()

        self.assertTrue(division.id == 1)
        self.assertTrue(division.name == "")
        self.assertTrue(division.bn_name == "")
        self.assertTrue(division.lat == 1)
        self.assertTrue(division.long == 2)

    @pytest.mark.division()
    def test_division_list_contains_8_division(self):
        division = Division()
        division_info_list = division.get_list_of_division_info_list()
        self.assertTrue(len(division_info_list) == 8)

    @pytest.mark.division()
    def test_division_list_contains_dhaka_division(self, given_division="Dhaka"):
        division = Division()
        division_list = division.get_list_of_divisions()
        self.assertTrue(given_division in division_list)

    @pytest.mark.division()
    def test_division_list_contains_division_spelling_error_corrections_april_2018(self):
        division_with_spelling_error_correction_april_2018 = ["Barishal", "Chattogram"]
        division = Division()
        divisions = division.get_list_of_divisions()

        excluded_from_correction = []
        for division_2018 in division_with_spelling_error_correction_april_2018:
            if not division_2018 in divisions:
                excluded_from_correction.append(division_2018)

        self.assertTrue(len(excluded_from_correction) == 0,
                        "The following Division needs to be updated "
                        + str(excluded_from_correction))

    @pytest.mark.division()
    def test_distance_between_divisions_statistics(self):
        division = Division()

        distances = []

        divisions = division.get_list_of_divisions()
        bn_divisions = division.get_list_of_divisions_bn_name()

        for i in range(len(divisions)):
            j = i
            for j in range(len(divisions)):
                coordinate_division_1 = division.get_coordinates_of_division_by_name(divisions[i])
                coordinate_division_2 = division.get_coordinates_of_division_by_name(divisions[j])

                bn_coordinate_division_1 = division.get_coordinates_of_division_by_bn_name(bn_divisions[i])
                bn_coordinate_division_2 = division.get_coordinates_of_division_by_bn_name(bn_divisions[j])

                self.assertEqual(coordinate_division_1, bn_coordinate_division_1, "Coordinates for queries aren't same")
                self.assertEqual(coordinate_division_2, bn_coordinate_division_2, "Coordinates for queries aren't same")

                distance = geopy.distance.geodesic(coordinate_division_1, coordinate_division_2).km
                if i != j:
                    distances.append(distance)

        self.assertEqual(int(mean(distances)), 234, "The mean distance between division is not accurate")
        self.assertEqual(int(median(distances)), 227, "The median distance between division is not accurate")
        self.assertEqual(int(mode(distances)), 151, "The mode distance between division is not accurate")

    @pytest.mark.division()
    def test_each_division_can_be_load_by_id(self):
        division = Division()
        divisions_en_names = set()
        divisions_bn_names = set()
        for i in range(9):
            division_en_name_found_by_id = division.get_name_of_division_by_id(str(i))
            division_bn_name_found_by_id = division.get_bn_name_of_division_by_id(str(i))
            if division_en_name_found_by_id is not None \
                    and not division.check_if_a_division_exists_by_bn_name(division_en_name_found_by_id):
                divisions_en_names.add(division_en_name_found_by_id)

            if division_bn_name_found_by_id is not None:
                divisions_bn_names.add(division_bn_name_found_by_id)

        self.assertEqual(len(divisions_en_names), 8, "Division could not be loaded with id")
        self.assertEqual(len(divisions_bn_names), 8, "Division could not be loaded with id")

    @pytest.mark.division()
    def test_division_can_not_be_load_by_invalid_id(self):
        division = Division()
        divisions = list()
        invalid_ids = ['-1', '-3', '-8', '65', '0', '9', '70', '100']
        for invalid_id in invalid_ids:
            division_name_found_by_id = division.get_name_of_division_by_id(invalid_id)
            divisions.append(division_name_found_by_id)

        self.assertEqual(len(divisions), len(invalid_ids), "Division could not be loaded with id")





