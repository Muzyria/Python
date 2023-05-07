class Postman:
    def __init__(self):
        self.delivery_data = []

    def add_delivery(self, street, house, apartment):
        self.delivery_data.append((street, house, apartment))

    def get_houses_for_street(self, street):
        res = []
        for item in self.delivery_data:
            if item[0] == street and item[1] not in res:
                res.append(item[1])
        return res

    def get_flats_for_house(self, street, house):
        res = []
        for item in self.delivery_data:
            if item[0] == street and item[1] == house and item[2] not in res:
                res.append(item[2])
        return res


postman = Postman()

postman.add_delivery('Советская', 151, 74)
postman.add_delivery('Советская', 151, 75)
postman.add_delivery('Советская', 90, 2)
postman.add_delivery('Советская', 151, 74)

print(postman.get_houses_for_street('Советская'))
print(postman.get_flats_for_house('Советская', 151))
