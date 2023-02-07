
import sqlite3


class BusRepository:
  def __init__(self) -> None:   
    self.db_path = './bus.db'
    self.connection = None


  def connect_db(self):
    if self.connection is None:
      self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)



  @staticmethod
  def get_all_bus_details():
    try:
      conn = BusRepository.connect_db()
      c = conn.cursor()
      rows = c.execute('select * from bus_details')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)


  @staticmethod
  def add_bus(depart,arrive,from_location,to_destination,bus_number):
    try:
      conn = BusRepository.connect_db()
      c = conn.cursor()
      insert_cursor = c.execute('insert into bus_details(departure_time,arrival_time,beginning,destination,bus_number) values(?,?,?,?,?)', (depart,arrive,from_location,to_destination,bus_number))
      conn.commit()
      c.execute('select * from bus_details')
      return {
    "Departure_time" : depart ,
    "Arrival_time" : arrive,
    "Beginning" : from_location,
    "Destination" : to_destination,
    "Bus_number" : bus_number 
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

