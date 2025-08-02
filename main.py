from opencage.geocoder import OpenCageGeocode


def get_coordinates(city, key):
    geocoder = OpenCageGeocode(key)
    query = city
    results = geocoder.geocode(query)

    if results:
        return results[0]['geometry']['lat'], results[0]['geometry']['lng']

    else:
        return "Город не найден"

key = 'eac1aeb8fa9d4bd0a86e7e7603dde609'
city = "Moscow"
coordinates = get_coordinates(city, key)
print(f'Координаты города {city}: {coordinates}')


