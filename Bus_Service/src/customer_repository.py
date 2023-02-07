import sqlite3


class CustomerRepository:

  def __init__(self) -> None:   
    self.db_path = './bus.db'
    self.connection = None


  def connect_db(self):
    if self.connection is None:
      self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)
 


  @staticmethod
  def get_all_customer_details():
    try:
      conn = CustomerRepository.connect_db()
      c = conn.cursor()
      rows = c.execute('select * from customer')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def add_customer(name, contact, dob):
    try:
      conn = CustomerRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('insert into customer(name, contact, dob) values(?,?,?)', (name, contact, dob))
      conn.commit()
      return {
        'id': insert_cursor.lastrowid,
        'name': name,
        'contact': contact,
        'DOB': dob
      }
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def delete_customer(id):
    try:
       
        conn = CustomerRepository.connect_db()
        c = conn.cursor()
        delete_cursor = c.execute('delete from customer where id=?',(id,))
        conn.commit()
        
        return id
    except Exception as e:
        raise Exception('Error: ', e)


