import json


json_string = '''
{
    "customers": [
        {
            "userid": 123456,
            "username": "Allie Hsu",
            "phone": [
                "000-001-0002",
                "000-002-0002"
            ],
            "is_vip": true
        },
        {
            "userid": 223678,
            "username": "Donald Duck",
            "phone": null,
            "is_vip": false
        }
    ]
}
'''

data = json.loads(json_string)
print(data['customers'][0]['username'])


