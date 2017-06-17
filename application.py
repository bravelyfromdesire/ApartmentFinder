# Apartment_finder
from ziroomFinder import getMetaDataFromZiroom
from dataHandler import handle

# get Data
room_metadata = getMetaDataFromZiroom()

# handle Data
filteredData = handle(room_metadata)


