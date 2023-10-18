const c = [
    '33.166625, -117.158398',
    '33.167037, -117.157515',
    '33.167482, -117.156817'
]

function convert_lat_lng_to_ddmm(lat_lng) {

    const degrees = parseInt(lat_lng, 10)
    const hours = parseFloat(lat_lng) - degrees
    let minutes = Math.abs(hours * 60);

    if (minutes < 10) {
        minutes = `0${minutes.toFixed(6)}`;
    } else {
        minutes = minutes.toFixed(6);
    }
    return `${degrees.toFixed(0)}${minutes}`;
}

c.map(_ => console.log(convert_lat_lng_to_ddmm(_.split(',')[0]) + ',' + convert_lat_lng_to_ddmm(_.split(',')[1])))
