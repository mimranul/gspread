class District:
    DHAKA = "dhaka"
    RANGPUR = "rangpur"
    BOGRA = "bogra"
    GOPALGANJ = "gopalganj"
    CHANDPUR = "chandpur"
    NARAYANGANJ = "narayanganj"
    CHITTAGANG = "chittagang"

    def get_district_list(self):
        return [self.DHAKA, self.RANGPUR, self.BOGRA, self.GOPALGANJ, self.CHANDPUR,
                self.NARAYANGANJ]

    def get_districts_where_not_supported(self):
        return [self.CHITTAGANG]
