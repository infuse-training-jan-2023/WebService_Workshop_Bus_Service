from booking_repository import BookingRepository


class BookingActions:
  def __init__(self) -> None:
    self.booking_repo = BookingRepository()


  def add_booking(self, customer_id, bus_id, pay_status):
    try:
      booking = self.booking_repo.add_booking(customer_id, bus_id, pay_status)
      return booking
    except Exception as e:
      print(e)
      return {}

  def update_booking(self, booking_id, pay_status):
    try:
      booking = self.booking_repo.update_booking(booking_id, pay_status)
      return booking
    except Exception as e:
      print(e)
      return {}


  def get_bookings(self):
    try:
      booking = self.booking_repo.get_bookings()
      res = []
      for booking in booking:
        res.append({
          'id': booking[0],
          'customer_id': booking[1],
          'bus_id': booking[2],
          'Payment_status': booking[3],

        })
      return res
    except Exception as e:
      print(e)
      return {}


  def delete_booking(self,id):
    try:
      booking = self.booking_repo.delete_bookings(id)
      return booking
    except Exception as e:
      print(e)
      return {}  
  
   


