from booking_repository import bookingRepository

class bookingActions:
  def __init__(self) -> None:
    self.booking_repo = bookingRepository()

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
  
   

