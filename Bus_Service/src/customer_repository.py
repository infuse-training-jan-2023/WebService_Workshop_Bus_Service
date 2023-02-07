import sqlite3


class CustomerRepository:

  def __init__(self) -> None:   
    self.db_path = './bus.db'
    self.connection = None


  def connect_db(self):
    if self.connection is None:
      self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)
 

  def get_all_customer_details(self):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      rows = cursor.execute('select * from customer')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)

  def add_customer(self,name, contact, dob):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      insert_cursor = cursor.execute('insert into customer(name, contact, dob) values(?,?,?)', (name, contact, dob))
      self.connection.commit()
      return {
        'id': insert_cursor.lastrowid,
        'name': name,
        'contact': contact,
        'DOB': dob
      }
    except Exception as e:
      raise Exception('Error: ', e)


  def delete_customer(self,id):
    try:
       
      self.connect_db()
      cursor = self.connection.cursor()
      delete_cursor = cursor.execute('delete from customer where id=?',(id,))
      self.connection.commit()   
      return id
    except Exception as e:
        raise Exception('Error: ', e)


