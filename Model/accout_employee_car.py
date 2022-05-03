class Account:
    def __init__(self, username, password):
        self.username= username
        self.password= password

class Employee(Account):
    def __init__(self,username, password, name, id, age, address, role, wage):
        Account.__init__(self, username, password)
        self.name= name
        self.id= id
        self.age= age
        self.address= address
        self.role= role
        self.wage= wage
        self.dsnv={}

class Car:
    def __init__(self,car_id, car_name, quantity, price_in, price_out):
        self.car_id= car_id
        self.car_name= car_name
        self.quantity= quantity
        self.price_in= price_in
        self.price_out= price_out
        self.dsxe={}