path = '-117.1587012382019,33.16645607424832,200.2293463260456 -117.1582998210703,33.16663807408465,201.8263721721011 -117.15772889729,33.16678675375711,205.2073269092919 -117.1573778806577,33.16719899506938,203.0890254826913 -117.1571429391361,33.16741337114964,204.095220247845 -117.156533075204,33.16753350644493,207.4763617497466 -117.1561679029564,33.16768411301182,208.6211179133939'

def convert_lat_lng_to_ddmm(lat_lng):
    degrees, minutes = divmod(abs(float(lat_lng)), 1)
    minutes, seconds = divmod(minutes * 60, 1)
    seconds = round(seconds * 60, 4)
    return f"{int(degrees):03d}{int(minutes):02d}{seconds:.4f}"

coordinates = path.split(' ')
for coordinate in coordinates:
    lng, lat, altitude = coordinate.split(',')
    result = convert_lat_lng_to_ddmm(lat) + ',' + convert_lat_lng_to_ddmm(lng)
    print(result)

