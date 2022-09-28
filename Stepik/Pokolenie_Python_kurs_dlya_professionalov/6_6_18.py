from collections import OrderedDict

data = OrderedDict({'Name': 'Брусника', 'IsNetObject': 'да', 'OperatingCompany': 'Брусника', 'TypeObject': 'кафе',
                    'AdmArea': 'Центральный административный округ', 'District': 'район Арбат',
                    'Address': 'город Москва, переулок Сивцев Вражек, дом 6/2', 'SeatsCount': '10'})

keys = list(data)
new_data = OrderedDict()


for i in range(len(keys)):
    elm = data.popitem(last=bool(i % 2))
    new_data[elm[0]] = elm[1]

print(new_data)
