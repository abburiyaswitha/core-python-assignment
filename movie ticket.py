def book_seat(booked_seats, seat_number, total_seats):
    if seat_number in booked_seats:
        return False
    elif seat_number < 1 or seat_number > total_seats:
        return False
    else:
        booked_seats.append(seat_number)
        return True
def cancel_seat(booked_seats, seat_number):
    if seat_number in booked_seats:
        booked_seats.remove(seat_number)
        return True
    else:
        return False
def available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
total_seats = 10
booked_seats = [2, 5, 7]
seat_to_book = 3
seat_to_cancel = 5
book_seat(booked_seats, seat_to_book, total_seats)
cancel_seat(booked_seats, seat_to_cancel)
available = available_seats(total_seats, booked_seats)
print("Available seats:",available)
