from flaskr import db


class CustomerType(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    customer_type = db.Column(db.String(length=50))
    customer_number = db.Column(db.String(length=50))
    customer_street = db.Column(db.String(length=150))
    customer_bank_name = db.Column(db.String(length=150))
    customer_bank_acc = db.Column(db.String(length=150))
    customer_id = db.Column(db.Integer(), db.ForeignKey('customer.id'), nullable=False)
    create_date = db.Column(db.DateTime)
    def __init__(self, customer_type, customer_number, customer_street, customer_bank_name, customer_bank_acc, create_date, customer_id):
        self.customer_type = customer_type
        self.customer_number = customer_number
        self.customer_street = customer_street
        self.customer_bank_name = customer_bank_name
        self.customer_bank_acc = customer_bank_acc
        self.create_date = create_date
        self.customer_id = customer_id

    
    @property
    def serialized(self):
        return {
            'id': self.id,
            'customer_type': self.customer_type,
            'customer_number': self.customer_number,
            'customer_street': self.customer_street,
            'customer_bank_name': self.customer_bank_name,
            'customer_bank_acc': self.customer_bank_acc,
            'create_date': self.create_date,
            'customer_id': self.customer_id,
        }

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
    description = db.Column(db.String(length=50))
    work_price = db.Column(db.Float())
    create_date = db.Column(db.DateTime)
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'), nullable=False)
    def __init__(self, work_type, spend_time, work_price, description, create_date, order_id):
        self.work_type = work_type
        self.spend_time = spend_time
        self.work_price = work_price
        self.description = description
        self.create_date = create_date
        self.order_id = order_id

    @property
    def serialized(self):
        return {
            'id': self.id,
            'work_type': self.work_type,
            'spend_time': self.spend_time,
            'description': self.description,
            'work_price': format(float(self.work_price), '.2f'),
            'create_date': self.create_date,
            'order_id': self.order_id
        }

class PartCar(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    part_name = db.Column(db.String(length=50))
    part_count = db.Column(db.Integer())
    part_price = db.Column(db.Float())
    full_price = db.Column(db.Float())
    create_date = db.Column(db.DateTime)
    order_id = db.Column(db.Integer(), db.ForeignKey('order.id'), nullable=False)
    def __init__(self, part_name, part_count, part_price, full_price, create_date, order_id):
            self.part_name = part_name
            self.part_count = part_count
            self.part_price = part_price
            self.full_price = full_price
            self.create_date = create_date
            self.order_id = order_id

    @property
    def serialized(self):
        return {
            'id': self.id,
            'part_name': self.part_name,
            'part_count': self.part_count,
            'part_price': format(float(self.part_price),'.2f'),
            'full_price': format(float(self.full_price),'.2f'),
            'create_date': self.create_date,
            'order_id': self.order_id
        }
class AddOrderData(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    full_service_price = db.Column(db.String(length=50))
    full_part_price = db.Column(db.String(length=50))
    full_count = db.Column(db.String(length=50))
    full_tax = db.Column(db.String(length=50))
    pay_option = db.Column(db.String(length=50))
    full_price = db.Column(db.String(length=50))
    full_price_no_tax = db.Column(db.String(length=50))
    price_in_words = db.Column(db.String(length=400))
    order_id = db.Column(db.Integer())
    def __init__(self, full_service_price, full_part_price, pay_option, full_price_no_tax, full_count, full_tax, full_price, price_in_words, order_id):
        self.full_service_price = full_service_price
        self.full_part_price = full_part_price
        self.pay_option = pay_option
        self.full_price_no_tax = full_price_no_tax
        self.full_count = full_count
        self.full_tax = full_tax
        self.full_price = full_price
        self.price_in_words = price_in_words
        self.order_id = order_id
    @property
    def serialized(self):
        return {
            'id': self.id,
            'full_service_price': self.full_service_price,
            'full_part_price': self.full_part_price,
            'pay_option': self.pay_option,
            'full_price_no_tax': self.full_price_no_tax,
            'full_count': self.full_count,
            'full_tax': self.full_tax,
            'full_price': self.full_price,
            'price_in_words': self.price_in_words,
            'order_id': self.order_id,
        }

class OrderData(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    customer_name = db.Column(db.String(length=50))
    phone = db.Column(db.String(length=50))
    customer_number = db.Column(db.String(length=50))
    customer_street = db.Column(db.String(length=300))
    customer_bank_name = db.Column(db.String(length=50))
    customer_bank_acc = db.Column(db.String(length=50))
    brand = db.Column(db.String(length=50))
    number = db.Column(db.String(length=50))
    vinumber = db.Column(db.String(length=50))
    odometer = db.Column(db.String(length=50))
    create_in = db.Column(db.String(length=50))
    order_id = db.Column(db.Integer())
    order_name = db.Column(db.String(length=50))
    create_out = db.Column(db.DateTime)
    def __init__(self, customer_name, phone, brand, number, vinumber, odometer, create_in, order_id, order_name, customer_number, customer_street, customer_bank_name, customer_bank_acc, create_out):
        self.customer_name = customer_name
        self.phone = phone
        self.brand = brand
        self.number = number
        self.vinumber = vinumber
        self.odometer = odometer
        self.create_in = create_in
        self.create_out = create_out
        self.order_name = order_name
        self.order_id = order_id
        self.customer_number = customer_number
        self.customer_street = customer_street
        self.customer_bank_name = customer_bank_name
        self.customer_bank_acc = customer_bank_acc
    @property
    def serialized(self):
        return {
            'id': self.id,
            'customer_name': self.customer_name,
            'phone': self.phone,
            'customer_number': self.customer_number,
            'customer_street': self.customer_street,
            'customer_bank_name': self.customer_bank_name,
            'customer_bank_acc': self.customer_bank_acc,
            'brand': self.brand,
            'number': self.number,
            'vinumber': self.vinumber,
            'odometer': self.odometer,
            'create_in': self.create_in,
            'create_out': self.create_out,
            'order_name': self.order_name,
            'order_id': self.order_id
        }
