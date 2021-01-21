import exifread

def _get_if_exist(data, key):
    for ii in range(len(data)):
        if data[ii]['name'] == key:
            return data[ii]['value']
    return None


def get_exif_dsc(exif_data):

    heading = 0

    gps_direction = _get_if_exist(exif_data, 'GPSImgDirection')
    #print(gps_direction)
    gps_direction_ref = _get_if_exist(exif_data, 'GPSImgDirectionRef')

    if str(gps_direction_ref) == "T": # Real North
        tab = str(gps_direction).split('/')
        print(tab)
        tab[0] = int(tab[0])
        tab[1] = int(tab[1])
        heading = tab[0]/tab[1]

    return heading