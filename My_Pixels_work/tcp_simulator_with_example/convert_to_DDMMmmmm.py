
c = [
    '33.166625, -117.158398',
    '33.167037, -117.157515',
    '33.167482, -117.156817'
    ]


def convert_lat_lng_to_ddmm(lat_lng):
    degrees = int(float(lat_lng))
    hours = float(lat_lng) - degrees
    minutes = abs(hours * 60)

    if minutes < 10:
        minutes = f'0{minutes:.6f}'
    else:
        minutes = f'{minutes:.6f}'

    return f'{int(degrees)}{minutes}'

for item in c:
    lat, lng = item.split(',')
    result = convert_lat_lng_to_ddmm(lat) + ',' + convert_lat_lng_to_ddmm(lng)
    print(result)
