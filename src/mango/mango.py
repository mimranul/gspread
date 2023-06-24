class Mango:
    KHIRSHA = "khirsha"
    HARIBHANGA = "haribhanga"
    FAZLI = "fazli"
    LANGRA = "langra"
    NAGFAZLI = "nagfazli"

    """This method will return the common mangoes that are in the market"""
    def get_common_list_of_mango(self):
        return [self.KHIRSHA, self.HARIBHANGA, self.FAZLI, self.LANGRA]

    """This method will return the mango that are grade A1"""
    def get_common_list_of_mango_of_grade_a1(self):
        return [self.KHIRSHA, self.HARIBHANGA, self.FAZLI]

    """This method will return the mango that are grade A2"""
    def get_common_list_of_mango_of_grade_a2(self):
        return [self.KHIRSHA, self.NAGFAZLI]

    """This method will return the mango that are safe to travel"""
    def get_common_list_of_mango_that_are_safe_to_travel(self):
        return [self.KHIRSHA, self.FAZLI]


