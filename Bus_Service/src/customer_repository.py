import sqlite3

class customerRepository:
  DBPATH = './bus.db'

  @staticmethod
  def connect_db():
    return sqlite3.connect(customerRepository.DBPATH)
  
  @staticmethod
  def get_all_customer():
    try:
      conn = customerRepository.connect_db()
      c = conn.cursor()
      rows = c.execute('select * from customer')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)

  @staticmethod
  def add_customer(name, contact, DOB):
    try:
      conn = customerRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('insert into customer(name, contact, DOB) values(?,?,?)', (name, contact, DOB))
      conn.commit()
      return {
        'id': insert_cursor.lastrowid,
        'name': name,
        'contact': contact,
        'DOB': DOB,
      }
    except Exception as e:
      raise Exception('Error: ', e)

  @staticmethod
  def delete_customer(id):
    try:
        # print(type(id))
        conn = customerRepository.connect_db()
        c = conn.cursor()
        deleted_row = c.execute('select * from customer where id=?',(id,))
        delete_cursor = c.execute('delete from customer where id=?',(id,))
        conn.commit()
        
        return deleted_row["id"]
    except Exception as e:
        raise Exception('Error: ', e)


