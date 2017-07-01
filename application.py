# Apartment_finder
from ziroomFinder import getMetaDataFromZiroom
from dataHandler import handle

pages = set()
apartment = dict()
def getApartment(site_url):
    if len(apartment) >= 10:
        return
    
    # get Data
    room_metadata, internalLinks = getMetaDataFromZiroom(site_url)
    if not room_metadata and not internalLinks:
        return
    
    # handle Data
    print(room_metadata)
    filteredData = handle(room_metadata)
    print(filteredData)
    if filteredData:
        apartment[filteredData['room_name']] = filteredData

    # handle internalLinks
    for link in internalLinks:
        if link not in pages:
            pages.add(link)
            getApartment(link)

getApartment('http://www.ziroom.com/z/vr/60224893.html')            
print('Apartment:')
print(apartment)
print('Pages:')
print(pages)
