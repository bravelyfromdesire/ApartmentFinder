# price conditions
MIN_PRICE = 800
MAX_PRICE = 1500

# area conditions
MIN_AREA = 8.0
MAX_AREA = 20.0

# direction condition
DIRECTION = ['南', '北', '东', '西']

# location condition

def handle(data):
    if not data:
        return False
    
    # filter status
    room_status = data['room_status']
    print('room_status:')
    print(room_status)
    if not room_status:
        return False
    
    # filter price
    room_price = int(data['room_price'])
    print('room_price:')
    print(room_price)
    if room_price < MIN_PRICE:
        return False
    elif room_price > MAX_PRICE:
        return False

    # filter area
    room_area = float(data['room_area'])
    print('room_area:')
    print(room_area)
    if room_area < MIN_AREA:
        return False
    elif room_area > MAX_AREA:
        return False

    # filter direction
    room_direction = data['room_direction']
    print('room_direction:')
    print(room_direction)
    if room_direction not in DIRECTION:
        return False

    # filter location


    return data
