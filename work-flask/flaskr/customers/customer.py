from flaskr import db

class Customer(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(length=50))
    phone = db.Column(db.String(length=50))
    create_date = db.Column(db.DateTime)
    def __init__(self, customer_name, phone, create_date):
        self.customer_name = customer_name
        self.phone = phone
        self.create_date = create_date
    
    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.customer_name,
            'phone': self.phone,
            'create_date': self.create_date 
        }

class Car(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    brand = db.Column(db.String(length=50))
    number = db.Column(db.String(length=50))
    vinnumber = db.Column(db.String(length=50))
    odometer = db.Column(db.String(length=50))
    create_date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer(), db.ForeignKey('customer.id'), nullable=False)
    def __init__(self, brand, number, vinnumber, odometer, create_date, customer_id):
        self.brand = brand
        self.number = number
        self.vinnumber = vinnumber
        self.odometer = odometer
        self.create_date = create_date
        self.customer_id = customer_id
    @property
    def serialized(self):
        return {
            'id': self.id,
            'brand': self.brand,
            'number': self.number,
            'vinnumber': self.vinnumber,
            'odometer': self.odometer,
            'create_date': self.create_date,
            'customer_id': self.customer_id
        }

class Order(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name= db.Column(db.String(length=50))
    status = db.Column(db.String(length=50))
    work_name = db.Column(db.String(length=50))
    car_id = db.Column(db.String(length=50))
    cust_id = db.Column(db.String(length=50))
    create_date = db.Column(db.DateTime)
    def __init__(self, name, status, work_name, car_id, cust_id, create_date):
            self.name = name
            self.status = status
            self.work_name = work_name
            self.car_id = car_id
            self.cust_id = cust_id
            self.create_date = create_date
    @property
    def serialized(self):
        return {
            'id': self.id,
            'name': self.name,
            'status': self.status,
            'work_name': self.work_name,
            'car_id': self.car_id,
            'cust_id': self.cust_id,
            'create_date': self.create_date,
        }

class ServiceCar(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    work_type = db.Column(db.String(length=50))
    spend_time = db.Column(db.String(length=50))
    part_name = db.Column(db.String(length=50))
    part_count = db.Column(db.String(length=50))
    create_date = db.Column(db.DateTime)
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'), nullable=False)
    def __init__(self, work_type, spend_time, part_name, part_count, create_date, order_id):
        self.work_type = work_type
        self.spend_time = spend_time
        self.part_name = part_name
        self.part_count = part_count
        self.create_date = create_date
        self.order_id = order_id

    @property
    def serialized(self):
        return {
            'id': self.id,
            'work_type': self.work_type,
            'spend_time': self.spend_time,
            'part_name': self.part_name,
            'part_count': self.part_count,
            'create_date': self.create_date,
            'order_id': self.order_id
        }

class OrderData(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(length=50))
    phone = db.Column(db.String(length=50))
    brand = db.Column(db.String(length=50))
    number = db.Column(db.String(length=50))
    vinumber = db.Column(db.String(length=50))
    odometer = db.Column(db.String(length=50))
    create_in = db.Column(db.String(length=50))
    order_id = db.Column(db.Integer())
    create_out = db.Column(db.DateTime)
    def __init__(self, customer_name, phone, brand, number, vinumber, odometer, create_in, order_id, create_out):
        self.customer_name = customer_name
        self.phone = phone
        self.brand = brand
        self.number = number
        self.vinumber = vinumber
        self.odometer = odometer
        self.create_in = create_in
        self.create_out = create_out
        self.order_id = order_id
    @property
    def serialized(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'phone': self.phone,
            'brand': self.brand,
            'number': self.number,
            'vinumber': self.vinumber,
            'odometer': self.odometer,
            'create_in': self.create_in,
            'create_out': self.create_out,
            'order_id': self.order_id
        }
