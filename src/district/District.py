import json


class District(object):

    def __init__(self):
        # Initialize super class
        super(District, self).__init__()

        # District attributes
        self.id = 1
        self.division_id = 1
        self.name = ""
        self.bn_name = ""
        self.lat = 1
        self.long = 2

    @classmethod
    def load_districts_json_file(cls):
        district_json_file = "C:\\Users\\rowsh\\PycharmProjects\\gspread\\src\\district\\districts.json"
        with open(district_json_file, encoding='utf-8') as file:
            data = json.load(file)
        return data

    @classmethod
    def get_list_of_district_info_list(cls):
        data = cls.load_districts_json_file()
        districts_info = []
        for district in data['districts']:
            districts_info.append(district)
        return districts_info

    @classmethod
    def get_list_of_districts(cls):
        district_info = cls.get_list_of_district_info_list()
        district_list = []
        for district in district_info:
            district_list.append(district.get('name'))

        return district_list

    @classmethod
    def get_coordinates_of_district_by_name(cls, given_district="Dhaka"):
        data = cls.get_list_of_district_info_list()
        if given_district in cls.get_list_of_districts():
            for district in data:
                if district.get('name') == given_district:
                    return [district.get("lat"), district.get("long")]

    @classmethod
    def get_name_of_district_by_id(cls, given_id='1'):
        data = cls.get_list_of_district_info_list()
        if 64 >= int(given_id) >= 0:
            for district in data:
                if district.get('id') == given_id:
                    return district.get('name')
        else:
            return None

    @classmethod
    def get_bn_name_of_district_by_id(cls, given_id='1'):
        data = cls.get_list_of_district_info_list()
        if 64 >= int(given_id) >= 0:
            for district in data:
                if district.get('id') == given_id:
                    return district.get('bn_name')
        else:
            return None

    @classmethod
    def check_if_a_district_exists_by_name(cls, given_district="Dhaka"):
        data = cls.load_districts_json_file()
        districts = []
        for district in data['districts']:
            districts.append(district)

        return given_district in districts

    @classmethod
    def check_if_a_district_exists_by_bn_name(cls, given_district="মৌলভীবাজার"):
        data = cls.load_districts_json_file()
        districts = []
        for district in data['districts']:
            districts.append(district)

        return given_district in districts

