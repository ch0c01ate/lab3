import folium
import geocoder

def create_location_map():
    return folium.Map()


def add_map_child(map, coordinates, user_name):
    '''
    str,str,str -> None
    This function gets figures and adds markers on a map.
    '''

    map.add_child(folium.Marker(location=coordinates,
                                popup=user_name,
                                icon=folium.Icon()))


def get_location(location):
    try:
        g = geocoder.arcgis(location)
        return g.latlng
    except:
        return "Not found"