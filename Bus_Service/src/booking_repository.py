import sqlite3


class BookingRepository:

  
  def __init__(self) -> None:   
    self.db_path = './bus.db'
    self.connection = None


 
  def connect_db(self):
    if self.connection is None:
      self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)


 
  def add_booking(self,customer_id, bus_id, pay_status):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      insert_cursor = cursor.execute('insert into booking(customer_id, bus_id, payment_status) values(?,?,?)', (customer_id, bus_id, pay_status))
      self.connection.commit()
      return {
        'id': insert_cursor.lastrowid,
        'customer_id': customer_id,
        'bus_id': bus_id,
        'payment_status': pay_status,
      }
    except Exception as e:
      raise Exception('Error: ', e)


 
  def update_booking(self,booking_id, pay_status):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      insert_cursor = cursor.execute('update booking set payment_status=? where id=?', (pay_status,booking_id ))
      self.connection.commit()
      return {
        'id': booking_id,
        'payment_status' : pay_status   
      }
    except Exception as e:
      raise Exception('Error: ', e)



  def get_bookings(self):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      rows = cursor.execute('select * from booking')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)


  def delete_bookings(self,id):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      delete_cursor = cursor.execute('DELETE FROM booking WHERE id= ?', (id,))
      self.connection.commit()
      return "Delete action successful !!! "
    except Exception as e:
      raise Exception('Error: ', e)

  