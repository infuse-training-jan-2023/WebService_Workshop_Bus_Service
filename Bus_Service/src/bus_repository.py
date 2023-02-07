
import sqlite3


class BusRepository:
  def __init__(self) -> None:   
    self.db_path = './bus.db'
    self.connection = None


  def connect_db(self):
    if self.connection is None:
      self.connection =  sqlite3.connect(self.db_path, check_same_thread=False)


  def get_all_bus_details(self):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      rows = cursor.execute('select * from bus_details')
      return rows
    except Exception as e:
      raise Exception('Error: ', e)


  
  def add_bus(self,depart,arrive,from_location,to_destination,bus_number):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      insert_cursor = cursor.execute('insert into bus_details(departure_time,arrival_time,beginning,destination,bus_number) values(?,?,?,?,?)', (depart,arrive,from_location,to_destination,bus_number))
      self.connection.commit()
      cursor.execute('select * from bus_details')
      return {
    "Departure_time" : depart ,
    "Arrival_time" : arrive,
    "Beginning" : from_location,
    "Destination" : to_destination,
    "Bus_number" : bus_number 
      }
    except Exception as e:
      raise Exception('Error: ', e)



  def delete_bus(self,id):
    try:
      self.connect_db()
      cursor = self.connection.cursor()
      delete_cursor = cursor.execute('DELETE FROM  bus_details WHERE id= ?', (id,))
      self.connection.commit()
      return "BUS DETAIL DELETED SUCCESSFULLY"
    except Exception as e:
      raise Exception('Error: ', e)

