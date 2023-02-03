from bus_repository import BusRepository


class BusActions:
  def __init__(self) -> None:
    self.bus_repo = BusRepository()


  def get_all_bus(self):
    try:
      bus = self.bus_repo.get_all_bus()
      res = []
      for bus in bus:
        res.append({
          'id': bus[0],
          'Departure_time': bus[1],
          'Arrival_time': bus[2],
          'Beginning': bus[3],
          'Destination' : bus[4],
          'Bus_number' : bus[5],

        })
      return res
    except Exception as e:
      print(e)
      return {}


  def add_bus(self,depart,arrive,fromdes,todes,number):
    try:
      bus = self.bus_repo.add_bus(depart,arrive,fromdes,todes,number)
      return bus
    except Exception as e:
      print(e)
      return {}


  def delete_bus(self,id):
    try:
      bus = self.bus_repo.delete_bus(id)
      return bus
    except Exception as e:
      print(e)
      return {}

