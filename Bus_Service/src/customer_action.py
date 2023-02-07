from customer_repository import customerRepository


class CustomerActions:
  def __init__(self) -> None:
    self.customer_repo = customerRepository()


  def get_all_customer_details(self):
    try:
      customer_list = self.customer_repo.get_all_customer_details()
      res = []
      for customer in customer_list:
        res.append({
          'id': customer[0],
          'name': customer[1],
          'contact': customer[2],
          'dob': customer[3],
        })
      return res
    except Exception as e:
      print(e)
      return {}


  def add_customer(self, name, contact, dob):
    try:
      customer = self.customer_repo.add_customer(name, contact, dob)
      return customer
    except Exception as e:
      print(e)
      return {}


  def delete_customer(self, id):
    try:
      print(id)
      customer = self.customer_repo.delete_customer(id)
      return customer
    except Exception as e:
      print(e)
      return {}


