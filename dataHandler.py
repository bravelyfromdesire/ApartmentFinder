# price conditions
MIN_PRICE = 800
MAX_PRICE = 1500

# area conditions
MIN_AREA = 8
MAX_AREA = 20

# direction condition
DIRECTION = '南'

# location condition

def handle(data):
    # filter status
    room_status = data['room_status']
    if not room_status:
        return False
    
    # filter price
    room_price = int(data['room_price'])
    if room_price < MIN_PRICE:
        return False
    elif room_price > MAX_PRICE:
        return False

    # filter area
    room_area = int(data['room_area'])
    if room_area < MIN_AREA:
        return False
    elif room_price > MAX_AREA:
        return False

    # filter direction
    room_direction = data['room_direction']
    if room_direction is not DIRECTION:
        return False

    # filter location
