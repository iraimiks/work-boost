import datetime
from flask import (
    Blueprint, request, jsonify, render_template
)
from flaskr import db
from flaskr.customers.customer import Customer, Car, Order, ServiceCar, OrderData, PartCar
from flaskr.users.user import User
from sqlalchemy import desc, or_
from flask_weasyprint import HTML, render_pdf


bp = Blueprint('customer', __name__, url_prefix='/customer')
#pdf generate

@bp.route('/hello_raims.pdf')
def hello_pdf():
    # Make a PDF straight from HTML in a string.
    html = render_template('orderpdf.html')
    return render_pdf(HTML(string=html))

@bp.route('/reg', methods=('GET', 'POST'))
def customer_reg():
    if request.method == 'POST':
        json_data = request.get_json()
        client_name = json_data['customername']
        phone = json_data['phone']
        customer_phone = Customer.query.filter_by(phone=phone).first()
        if customer_phone is None:
            new_customer = Customer(client_name, phone, create_date=datetime.datetime.now())
            db.session.add(new_customer)
            db.session.commit()
            customer = Customer.query.order_by(desc("id")).first()
            return jsonify(status="new_customer_register", redid=customer.id)
        else:
            return jsonify(status="exist_phone", customer_id=customer_phone.id)


@bp.route('/carreg/<id>', methods=('GET', 'POST'))
def customer_car_reg(id):
    if request.method == 'POST':
        json_data = request.get_json()
        brand = json_data['carbrand']
        number = json_data['carnumber']
        vinnumber = json_data['vinnumber']
        odometer = json_data['odometer']
        car_number = Car.query.filter_by(number=number).first()
        if car_number is None:
            new_cust_car = Car(brand, number, vinnumber, odometer, create_date=datetime.datetime.now(), customer_id=id)
            db.session.add(new_cust_car)
            db.session.commit()
            return jsonify(status="carregister")
        else:
            return jsonify(status="exist_car", car=car_number.number)

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
def get_car(id):
    if request.method == 'GET':
        car = Car.query.filter_by(id=id).first()
        return jsonify({'car':[car.serialized]})

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
        workers = User.query.filter_by(user_role="worker").all()
        return jsonify({'workers': [worker.serialized for worker in workers]})

@bp.route('/cars', methods=('GET','POST'))
def cars():
    if request.method == 'GET':
        cars = Car.query.order_by(desc("id")).all()
        return jsonify({'cars': [car.serialized for car in cars]})

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



@bp.route('/orderdata', methods=('GET', 'POST'))
def order_data():
    if request.method == 'POST':
        json_data = request.get_json()
        cust_id = json_data['cust_id']
        order_id = json_data['order_id']
        customer = Customer.query.filter_by(id=cust_id).first()
        car_order = Order.query.filter_by(id=order_id).first()
        customer_car = Car.query.filter_by(id=car_order.car_id).first()
        new_order_data = OrderData(
            customer.customer_name, 
            customer.phone, 
            customer_car.brand,
            customer_car.number,
            customer_car.vinnumber,
            customer_car.odometer,
            car_order.create_date,
            car_order.id,
            create_out=datetime.datetime.now(),
            )
        db.session.add(new_order_data)
        db.session.commit()
        return jsonify(status="orderdatarecive")

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


# service api
@bp.route('/service/<id>', methods=('GET', 'POST'))
def car_service(id):
    if request.method == 'POST':
        json_data = request.get_json()
        work_type = json_data['work_type']
        description = json_data['description']
        spend_time = json_data['spend_time']
        work_price = json_data['work_price']
        new_service = ServiceCar(work_type, spend_time, work_price, description, create_date=datetime.datetime.now(), order_id=id)
        db.session.add(new_service)
        db.session.commit()
        return jsonify(status="car_service_reg")

@bp.route('/part/<id>', methods=('GET', 'POST'))
def car_part(id):
    if request.method == 'POST':
        json_data = request.get_json()
        part_name = json_data['part_name']
        part_count = json_data['part_count']
        part_price = json_data['part_price']
        full_price = json_data['full_price']
        new_part = PartCar(part_name, part_count, part_price, full_price, create_date=datetime.datetime.now(), order_id=id)
        db.session.add(new_part)
        db.session.commit()
        return jsonify(status="part_car_reg")

@bp.route('/services/<id>', methods=('GET', 'POST'))
def car_services(id):
    if request.method == 'GET':
        services = ServiceCar.query.filter_by(order_id=id).all()
        return jsonify({'servicecar': [service.serialized for service in services]})

@bp.route('/parts/<id>', methods=('GET', 'POST'))
def car_parts(id):
    if request.method == 'GET':
        parts = PartCar.query.filter_by(order_id=id).all()
        return jsonify({'partscar': [part.serialized for part in parts]})

@bp.route('/orderdata/<id>', methods=('GET', 'POST'))
def get_order_data(id):
    if request.method == 'GET':
        order = OrderData.query.filter_by(order_id=id).first()
        services = ServiceCar.query.filter_by(order_id=id).all()
        return jsonify({'info': [order.serialized], 'service_car': [service.serialized for service in services]})