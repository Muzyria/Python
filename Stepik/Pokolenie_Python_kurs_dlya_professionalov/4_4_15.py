import json

with open('food_services.json', encoding='UTF-8') as file:
    json_data = json.load(file)
    district, chain = {}, {}

    for entry in json_data:
        district[entry['District']] = district.get(entry['District'], 0) + 1
        if entry['IsNetObject'] == 'да':
            chain[entry['OperatingCompany']] = chain.get(entry['OperatingCompany'], 0) + 1

    max_district = max(district.items(), key=lambda x: x[1])
    max_chain = max(chain.items(), key=lambda x: x[1])

    print(f'{max_district[0]}: {max_district[1]}')
    print(f'{max_chain[0]}: {max_chain[1]}')
