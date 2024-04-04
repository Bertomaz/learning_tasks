
class Location:
    def __init__(self, longitude, latitude):
        self.longitude = Location.normalize_longitude(longitude)
        self.latitude = Location.normalize_latitude(latitude)
    #static methods are often called by the class

    @staticmethod
    def normalize_latitude(latitude):
        if latitude > 90:
            return 90
        if latitude < -90:
            return -90
        return latitude


    @staticmethod
    def normalize_longitude(longitude):
        return ((longitude - 180) % -360) + 180




# A few default locations that we often visit
# Notice that we indicate them to be constants by naming them in UPPER_CASE
DRESDEN = Location(latitude=51.05089, longitude=13.73832)
GALAPAGOS = Location(latitude=-0.777259, longitude=-91.142578)
NORTH_POLE = Location(latitude=90, longitude=0)
NAURU = Location(latitude=-0.5284144, longitude=166.9342384)
##
