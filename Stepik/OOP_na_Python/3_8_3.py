class UnitedKingdom:

    @staticmethod
    def capital():
        print("London is the capital of Great Britain.")

    @staticmethod
    def language():
        print("English is the primary language of Great Britain.")    


class Spain:

    @staticmethod
    def capital():
        print("Madrid is the capital of Spain.")

    @staticmethod
    def language():
        print("Spanish is the primary language of Spain.")



obj_uk = UnitedKingdom()
obj_spa = Spain()
for country in (obj_spa, obj_uk):
    country.capital()
    country.language()
