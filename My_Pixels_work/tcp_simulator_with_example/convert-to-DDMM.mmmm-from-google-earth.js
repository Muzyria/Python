const path = '-117.1587012382019,33.16645607424832,200.2293463260456 -117.1582998210703,33.16663807408465,201.8263721721011 -117.15772889729,33.16678675375711,205.2073269092919 -117.1573778806577,33.16719899506938,203.0890254826913 -117.1571429391361,33.16741337114964,204.095220247845 -117.156533075204,33.16753350644493,207.4763617497466 -117.1561679029564,33.16768411301182,208.6211179133939'

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

path.split(' ').map(_ => console.log(convert_lat_lng_to_ddmm(_.split(',')[1]) + ',' + convert_lat_lng_to_ddmm(_.split(',')[0])))
