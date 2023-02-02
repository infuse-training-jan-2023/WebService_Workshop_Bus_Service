import sqlite3

class bookingRepository:
  DBPATH = './bus.db'

  @staticmethod
  def connect_db():
    return sqlite3.connect(bookingRepository.DBPATH)

  @staticmethod
  def add_booking(customer_id, bus_id, pay_status):
    try:
      conn = bookingRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('insert into booking(customer_id, bus_id, Payment_status) values(?,?,?)', (customer_id, bus_id, pay_status))
      conn.commit()
      return {
        'id': insert_cursor.lastrowid,
        'customer_id': customer_id,
        'bus_id': bus_id,
        'Payment_Status': pay_status,
      }
    except Exception as e:
      raise Exception('Error: ', e)
  @staticmethod
  def update_booking(booking_id, pay_status):
    try:
      conn = bookingRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('update booking set Payment_status=? where id=?', (pay_status,booking_id ))
      conn.commit()
      return {
        'id': booking_id,
        'Payment_status' : pay_status   
      }
    except Exception as e:
      raise Exception('Error: ', e)
