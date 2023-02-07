import sqlite3


class BookingRepository:

  
  def __init__(self) -> None:   
    self.db_path = './bus.db'
    self.connection = None


  @staticmethod
  def connect_db(self):
    if self.connection is None:
      self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)


  @staticmethod
  def add_booking(customer_id, bus_id, pay_status):
    try:
      conn = BookingRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('insert into booking(customer_id, bus_id, payment_status) values(?,?,?)', (customer_id, bus_id, pay_status))
      conn.commit()
      return {
        'id': insert_cursor.lastrowid,
        'customer_id': customer_id,
        'bus_id': bus_id,
        'payment_status': pay_status,
      }
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def update_booking(booking_id, pay_status):
    try:
      conn = BookingRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('update booking set payment_status=? where id=?', (pay_status,booking_id ))
      conn.commit()
      return {
        'id': booking_id,
        'payment_status' : pay_status   
      }
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def get_bookings():
    try:
      conn = BookingRepository.connect_db()
      c = conn.cursor()
      rows = c.execute('select * from booking')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def delete_bookings(id):
    try:
      conn = BookingRepository.connect_db()
      c = conn.cursor()
      delete_cursor = c.execute('DELETE FROM booking WHERE id= ?', (id,))
      conn.commit()
      return "Delete action successful !!! "
    except Exception as e:
      raise Exception('Error: ', e)

  