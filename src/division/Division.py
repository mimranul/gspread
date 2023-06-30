import json


class Division(object):

    def __init__(self):
        # Initialize super class
        super(Division, self).__init__()

        # District attributes
        self.id = 1
        self.name = ""
        self.bn_name = ""
        self.lat = 1
        self.long = 2

    @classmethod
    def load_division_json_file(cls):
        division_json_file = "C:\\Users\\rowsh\\PycharmProjects\\gspread\\src\\division\\divisions.json"
        with open(division_json_file, encoding='utf-8') as file:
            data = json.load(file)
        return data

    @classmethod
    def get_list_of_division_info_list(cls):
        data = cls.load_division_json_file()
        division_info = []
        for division in data['divisions']:
            division_info.append(division)
        return division_info

    @classmethod
    def get_list_of_divisions(cls):
        division_info = cls.get_list_of_division_info_list()
        division_list = []
        for division in division_info:
            division_list.append(division.get('name'))

        return division_list

    @classmethod
    def get_list_of_divisions_bn_name(cls):
        division_info = cls.get_list_of_division_info_list()
        division_list = []
        for division in division_info:
            division_list.append(division.get('bn_name'))

        return division_list

    @classmethod
    def get_coordinates_of_division_by_name(cls, given_division="Dhaka"):
        data = cls.get_list_of_division_info_list()
        if given_division in cls.get_list_of_divisions():
            for division in data:
                if division.get('name') == given_division:
                    return [division.get("lat"), division.get("long")]

    @classmethod
    def get_coordinates_of_division_by_bn_name(cls, given_division="চট্টগ্রাম"):
        data = cls.get_list_of_division_info_list()
        bn_list_of_divisions = cls.get_list_of_divisions_bn_name()
        if given_division in bn_list_of_divisions:
            for division in data:
                if division.get('bn_name') == given_division:
                    return [division.get("lat"), division.get("long")]

    @classmethod
    def get_name_of_division_by_id(cls, given_id='1'):
        data = cls.get_list_of_division_info_list()
        if 64 >= int(given_id) >= 0:
            for division in data:
                if division.get('id') == given_id:
                    return division.get('name')
        else:
            return None

    @classmethod
    def get_bn_name_of_division_by_id(cls, given_id='1'):
        data = cls.get_list_of_division_info_list()
        if 64 >= int(given_id) >= 0:
            for division in data:
                if division.get('id') == given_id:
                    return division.get('bn_name')
        else:
            return None

    @classmethod
    def check_if_a_division_exists_by_name(cls, given_division="Dhaka"):
        data = cls.load_division_json_file()
        divisions = []
        for division in data['divisions']:
            division.append(division)

        return given_division in divisions

    @classmethod
    def check_if_a_division_exists_by_bn_name(cls, given_division="চট্টগ্রাম"):
        data = cls.load_division_json_file()
        divisions = []
        for division in data['divisions']:
            divisions.append(division)

        return given_division in divisions

