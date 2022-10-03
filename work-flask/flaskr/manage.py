import datetime
from flask import (
    Blueprint, request, jsonify
)
from flaskr import db
from flaskr.customers.customer import Customer, Car, Order, ServiceCar
from flaskr.users.user import User
from sqlalchemy import desc

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/reg', methods=('GET', 'POST'))
def customer_reg():
    if request.method == 'POST':
        json_data = request.get_json()
        client_name = json_data['customername']
        phone = json_data['phone']
        new_customer = Customer(client_name, phone, create_date=datetime.datetime.now())
        db.session.add(new_customer)
        db.session.commit()
        return jsonify(status="register")

@bp.route('/carreg/<id>', methods=('GET', 'POST'))
def customer_car_reg(id):
    if request.method == 'POST':
        json_data = request.get_json()
        brand = json_data['carbrand']
        number = json_data['carnumber']
        vinnumber = json_data['vinnumber']
        odometer = json_data['odometer']
        new_cust_car = Car(brand, number, vinnumber, odometer, create_date=datetime.datetime.now(), customer_id=id)
        db.session.add(new_cust_car)
        db.session.commit()
        return jsonify(status="carregister")

@bp.route('/list', methods=('GET', 'POST'))
def all_customers():
    if request.method == 'GET':
        customers = Customer.query.order_by(desc("id")).all()
        return jsonify({'customers': [customer.serialized for customer in customers]})

@bp.route('/cars/<id>', methods=('GET', 'POST'))
def customers_cars(id):
    if request.method == 'GET':
        cars = Car.query.filter_by(customer_id=id).all()
        return jsonify({'customerscars': [car.serialized for car in cars]})

@bp.route('/car/<id>', methods=('GET', 'POST'))
def customer_car(id):
    if request.method == 'GET':
        car = Car.query.filter_by(id=id).first()
        return jsonify({'customerscar': [car.serialized]})

@bp.route('/<id>', methods=('GET', 'POST'))
def customer(id):
    if request.method == 'GET':
        customer = Customer.query.filter_by(id=id).first()
        return jsonify({'customer': [customer.serialized]})

@bp.route('/workers', methods=('GET', 'POST'))
def workers():
    if request.method == 'GET':
        workers = User.query.filter_by(user_role="wo_user").all()
        return jsonify({'workers': [worker.serialized for worker in workers]})

@bp.route('/order', methods=('GET', 'POST'))
def order():
    if request.method == 'POST':
        date_as_id = datetime.datetime.now().strftime('%Y%m%d%H%M')
        order_name = "BT_" + date_as_id
        order_status = "Darbs Sākts"
        json_data = request.get_json()
        work_name = json_data['worker']
        car_id = json_data['carid']
        cust_id = json_data['custid']
 
        new_order = Order(order_name, order_status, work_name, car_id, cust_id, create_date=datetime.datetime.now())
        db.session.add(new_order)
        db.session.commit()
        return jsonify(status="orderregister")

@bp.route('/orders/<carid>', methods=('GET', 'POST'))
def car_orders(carid):
    if request.method == 'GET':
        orders = Order.query.filter_by(car_id=carid).all()
        return jsonify({'carorder': [order.serialized for order in orders]})

@bp.route('/order/<id>', methods=('GET', 'POST'))
def car_order(id):
    if request.method == 'GET':
        order = Order.query.filter_by(id=id).first()
        return jsonify({'order': [order.serialized]})

@bp.route('/service/<id>', methods=('GET', 'POST'))
def car_service(id):
    if request.method == 'POST':
        json_data = request.get_json()
        work_type = json_data['worktype']
        spend_time = json_data['spendtime']
        part_name = json_data['partname']
        part_count = json_data['partcount']
        new_service = ServiceCar(work_type, spend_time, part_name, part_count, create_date=datetime.datetime.now(), order_id=id)
        db.session.add(new_service)
        db.session.commit()
        return jsonify(status="carregister")

@bp.route('/services/<id>', methods=('GET', 'POST'))
def car_services(id):
    if request.method == 'GET':
        services = ServiceCar.query.filter_by(order_id=id).all()
        return jsonify({'servicecar': [service.serialized for service in services]})
