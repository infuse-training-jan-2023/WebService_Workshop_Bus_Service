
import sqlite3


class BusRepository:
  NOT_STARTED = "Not Started"
  DBPATH = './bus.db'


  @staticmethod
  def connect_db():
    return sqlite3.connect(BusRepository.DBPATH)


  @staticmethod
  def get_all_bus():
    try:
      conn = BusRepository.connect_db()
      c = conn.cursor()
      rows = c.execute('select * from bus_details')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def add_bus(depart,arrive,fromdes,todes,number):
    try:
      conn = BusRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('insert into bus_details(Departure_time,Arrival_time,Beginning,Destination,Bus_number) values(?,?,?,?,?)', (depart,arrive,fromdes,todes,number))
      conn.commit()
      c.execute('select * from bus_details')
      return {
    "Departure_time" : depart ,
    "Arrival_time" : arrive,
    "Beginning" : fromdes,
    "Destination" : todes,
    "Bus_number" : number 
      }
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def delete_bus(id):
    try:
      conn = BusRepository.connect_db()
      c = conn.cursor()
      delete_cursor = c.execute('DELETE FROM  bus_details WHERE id= ?', (id,))
      conn.commit()
      return "BUS DETAIL DELETED SUCCESSFULLY"
    except Exception as e:
      raise Exception('Error: ', e)

