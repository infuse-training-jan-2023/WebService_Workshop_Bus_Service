from flask import Flask, Response, request
import json

from customer_action import customerActions
from booking_action import bookingActions
app=Flask(__name__)
customer_actions=customerActions()
booking_actions=bookingActions()



@app.route('/allcustomers', methods = ['GET'])
def get_all_customers():
  customers = customer_actions.get_all_customer()
  print(customers)
  return Response(json.dumps(customers), mimetype='application/json', status=200)

# create an api to add a new customer
@app.route('/customer', methods = ['POST'])
def add_new_customer():
  request_data = request.get_json()
  name = request_data['name']
  contact = request_data['contact']
  DOB=request_data['DOB']
  added_customer = customer_actions.add_customer(name, contact, DOB)
  if added_customer == {}:
    return Response("{'error': 'Erro addding the customer'}", mimetype='application/json', status=500)
  return Response(json.dumps(added_customer), mimetype='application/json', status=201)

@app.route('/customerdelete/<int:id>', methods = ['GET'])
def delete_customers(id):
  print(id)
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

@app.route('/updatebookingpay', methods = ['POST'])
def update_booking():
  request_data = request.get_json()
  booking_id = request_data['booking_id']
  pay_status=request_data['Payment_status']
  updt_booking = booking_actions.update_booking(booking_id, pay_status)
  if updt_booking == {}:
    return Response("{'error': 'Erro addding the booking'}", mimetype='application/json', status=500)
  return Response(json.dumps(updt_booking), mimetype='application/json', status=201)


if __name__=='__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')