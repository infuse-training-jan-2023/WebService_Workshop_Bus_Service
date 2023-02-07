from flask import Flask, Response, request
import json
from bus_action import BusActions
from customer_action import CustomerActions
from booking_action import BookingActions
app = Flask(__name__)
customer_actions = CustomerActions()
booking_actions = BookingActions()
bus_action = BusActions()



@app.route('/customers', methods = ['GET'])
def get_all_customers():
  customers = customer_actions.get_all_customer_details()
  print(customers)
  return Response(json.dumps(customers), mimetype='application/json', status=200)


# create an api to add a new customer
@app.route('/customer', methods = ['POST'])
def add_new_customer():
  request_data = request.get_json()
  name = request_data['name']
  contact = request_data['contact']
  dob=request_data['DOB']
  added_customer = customer_actions.add_customer(name, contact, dob)
  if added_customer == {}:
    return Response("{'error': 'Erro addding the customer'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_customer), mimetype='application/json', status=201)


@app.route('/customer/<int:id>', methods = ['DELETE'])
def delete_customers(id):
  
  deleted_customer = customer_actions.delete_customer(id)
  if deleted_customer == {}:
    return Response("{'error': 'Erro deleting the customer'}", mimetype='application/json', status=500)
  return Response(json.dumps(deleted_customer), mimetype='application/json', status=201)


@app.route('/booking', methods = ['POST'])
def add_new_booking():
  request_data = request.get_json()
  customer_id = request_data['customer_id']
  bus_id = request_data['bus_id']
  pay_status=request_data['Payment_status']
  added_booking = booking_actions.add_booking(customer_id, bus_id, pay_status)
  if added_booking == {}:
    return Response("{'error': 'Erro addding the booking'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_booking), mimetype='application/json', status=201)


@app.route('/booking', methods = ['PUT'])
def update_booking():
  request_data = request.get_json()
  booking_id = request_data['booking_id']
  pay_status=request_data['Payment_status']
  updt_booking = booking_actions.update_booking(booking_id, pay_status)
  if updt_booking == {}:
    return Response("{'error': 'Erro addding the booking'}", mimetype='application/json', status=500)
  return Response(json.dumps(updt_booking), mimetype='application/json', status=201)




@app.route('/buses',methods=['GET'])
def get_all_bus_details():
   buses = bus_action.get_all_bus_details()
   print(buses)
   return Response(json.dumps(buses), mimetype='application/json', status=200)


# create an api to add a new item
@app.route('/bus', methods = ['POST'])
def add_new_bus():
  request_data = request.get_json()
  depart = request_data['Departure_time']
  arrive = request_data['Arrival_time']
  fromdes = request_data['Beginning']
  todes = request_data['Destination']
  number = request_data['Bus_number']
  added_bus = bus_action.add_bus(depart,arrive,fromdes,todes,number)
  if added_bus == {}:
    return Response("{'error': 'Erro addding the item'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_bus), mimetype='application/json', status=201)


@app.route('/bus', methods = ['DELETE'])
def delete_bus():
  request_data = request.get_json()
  id = request_data['id']
  added_bus = bus_action.delete_bus(id)
  if delete_bus == {}:
    return Response("{'error': 'Erro addding the item'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_bus), mimetype='application/json', status=201)


@app.route('/booking', methods = ['GET'])
def display_booking():
  bookings = booking_actions.get_bookings()
  print(bookings)
  return Response(json.dumps(bookings), mimetype='application/json', status=200)


@app.route('/booking', methods = ['DELETE'])
def delete_booking():
  request_data = request.get_json()
  id = request_data['id']
  delete_booking = booking_actions.delete_booking(id)
  print("in main")
  print(delete_booking)
  if delete_booking == {}:
    return Response("{'error': 'Erro deleting the item'}", mimetype='application/json', status=500)
  return Response(json.dumps(delete_booking), mimetype='application/json', status=201)




if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')
