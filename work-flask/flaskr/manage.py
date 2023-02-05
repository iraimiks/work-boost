import datetime
from flask import (
    Blueprint, request, jsonify, render_template
)
from flaskr import db
from flaskr.customers.customer import Customer, Car, Order, ServiceCar, OrderData, PartCar, AddOrderData, CustomerType
from flaskr.users.user import User
from sqlalchemy import desc
from flask_weasyprint import HTML, render_pdf


bp = Blueprint('customer', __name__, url_prefix='/customer')
#pdf generate

@bp.route('/pdforder/<id>', methods=('GET', 'POST'))
def hello_pdf(id):
    time = datetime.datetime.now()

    if request.method == 'GET':
        order = OrderData.query.order_by(OrderData.id.desc()).first()
        parts = PartCar.query.filter_by(order_id=id).all()
        services = ServiceCar.query.filter_by(order_id=id).all()
        orderdata = AddOrderData.query.order_by(AddOrderData.id.desc()).first()
        html = render_template('orderpdf.html', order=order, parts=parts, services=services, orderdata=orderdata, today=time.strftime("%d/%m/%y"))
    return render_pdf(HTML(string=html))

@bp.route('/customerdel', methods=('GET', 'POST'))
def customer_delet():
    if request.method == 'POST':
        json_data = request.get_json()
        customerid = json_data['customer_id']
        customer = Customer.query.filter_by(id=int(customerid)).first()
        print(customer.id)
        customer_type = CustomerType.query.filter_by(customer_id=customer.id).first()
        car_exist = Car.query.filter_by(customer_id=str(customer.id)).first()
        if car_exist is None:
            if customer_type is not None:
                db.session.delete(customer_type)
                db.session.commit()
            else:
                db.session.delete(customer)
            db.session.delete(customer)
            db.session.commit()
            return jsonify(status="customer_delete")
        else:
            return jsonify(status="customer_exist_car")

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

@bp.route('/dataedit/<id>', methods=('GET', 'POST'))
def customer_edit(id):
    customer = Customer.query.get(id)
    customer_type = CustomerType.query.filter_by(customer_id=id).first()
    if request.method == 'POST':
        json_data = request.get_json()
        print(json_data)
        customer_name = json_data['edit_name']
        phone = json_data['edit_phone']
        customer_type_data = json_data['edit_customer_type']
        customer_number = json_data['edit_customer_number']
        customer_street = json_data['edit_customer_street']
        customer_bank_name = json_data['edit_customer_name']
        customer_bank_acc = json_data['edit_customer_bank_acc']
        customer_type.customer_type = customer_type_data
        customer_type.customer_number = customer_number
        customer_type.customer_street = customer_street
        customer_type.customer_bank_name = customer_bank_name
        customer_type.customer_bank_acc = customer_bank_acc
        customer.customer_name = customer_name
        customer.phone = phone
        db.session.commit()
        return jsonify(status="customer_edit")

@bp.route('/custtype/<id>', methods=('GET', 'POST'))
def customer_type_reg(id):
    if request.method == 'POST':
        json_data = request.get_json()
        customer_type = json_data['customer_type']
        customer_number = json_data['customer_number']
        customer_street = json_data['customer_street']
        customer_bank_name = json_data['customer_bank_name']
        customer_bank_acc = json_data['customer_bank_acc']
        customer = CustomerType.query.filter_by(customer_number=customer_number).first()
        if customer is None:
            new_cust_type = CustomerType(customer_type, customer_number, customer_street, customer_bank_name, customer_bank_acc, create_date=datetime.datetime.now(), customer_id=id)
            db.session.add(new_cust_type)
            db.session.commit()
            return jsonify(status="new_customer_type")
        else:
            return jsonify(status="customer_number_exist")

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


@bp.route('/cardel', methods=('GET', 'POST'))
def car_delet():
    if request.method == 'POST':
        json_data = request.get_json()
        carid = json_data['car_id']
        car = Car.query.get(int(carid))
        order_exist = Order.query.filter_by(car_id=str(car.id)).first()
        if  order_exist is None:
            db.session.delete(car)
            db.session.commit()
            return jsonify(status="car_delete")
        else:
            return jsonify(status="order_exist")


@bp.route('/caredit/<id>', methods=('GET', 'POST'))
def car_edit(id):
    car = Car.query.get(id)
    if request.method == 'POST':
        json_data = request.get_json()
        carbrand = json_data['car_brand']
        car_number = json_data['car_number']
        vinnumber = json_data['vinnumber']
        odometer = json_data['odometer']
        car.brand = carbrand
        car.number = car_number
        car.vinnumber = vinnumber
        car.odometer = odometer
        db.session.commit()
        return jsonify(status="car_edit")


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

@bp.route('/customerdata/<id>', methods=('GET', 'POST'))
def customer_data(id):
    if request.method == 'GET':
        customer = CustomerType.query.filter_by(customer_id=id).first()
        if customer is None:
            return jsonify({'customer_data': 'no_data'})
        else:
            return jsonify({'customer_data': [customer.serialized]})

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

@bp.route('/statuswork', methods=('GET','POST'))
def status_work():
    if request.method == 'GET':
        cars = Car.query.order_by(desc("id")).all()
        car_ids = [str(car.id) for car in cars]
        orders = db.session.query(Order).filter(Order.car_id.in_(car_ids))
        return  jsonify({'orders':[order.serialized for order in orders]})

@bp.route('/finishwork/<id>', methods=('GET', 'POST'))
def finish_order(id):
    if request.method == 'POST':
        order = Order.query.get(id)
        json_data = request.get_json()
        work_done = json_data['order_status']
        order.status = work_done
        db.session.commit()
        return jsonify(status="finish_work")

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

@bp.route('/orderdel', methods=('GET', 'POST'))
def del_order():
    if request.method == 'POST':
        json_data = request.get_json()
        order_id = json_data['order_id']
        order = Order.query.get(int(order_id))
        service_exist = ServiceCar.query.filter_by(order_id=order.id).first()
        parts_exist = PartCar.query.filter_by(order_id=order.id).first()
        if parts_exist is None and service_exist is None:
            db.session.delete(order)
            db.session.commit()
            return jsonify(status="order_delete")
        else:
            return jsonify(status="service_or_part_exist")


@bp.route('/addorderdata', methods=('GET', 'POST'))
def add_Order_data():
    if request.method == 'POST':
        json_data = request.get_json()
        full_service_price = json_data['full_service_price']
        full_part_price = json_data['full_part_price']
        pay_option = json_data['pay_option']
        full_price_no_tax = json_data['full_price_no_tax']
        full_count = json_data['full_count']
        full_tax = json_data['full_tax']
        full_price = json_data['full_price']
        price_in_words = json_data['price_in_words']
        order_id = json_data['order_id']
        new_add_order_data = AddOrderData(
            full_service_price,
            full_part_price,
            pay_option,
            full_price_no_tax,
            full_count,
            full_tax,
            full_price,
            price_in_words,
            order_id
        )
        db.session.add(new_add_order_data)
        db.session.commit()
        return jsonify(status="orderdatarecive")

@bp.route('/orderdata', methods=('GET', 'POST'))
def order_data():
    if request.method == 'POST':
        json_data = request.get_json()
        cust_id = json_data['cust_id']
        order_id = json_data['order_id']
        customer = Customer.query.filter_by(id=cust_id).first()
        customer_type_data = CustomerType.query.filter_by(customer_id=cust_id).first()
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
            car_order.name,
            customer_type_data.customer_number,
            customer_type_data.customer_street,
            customer_type_data.customer_bank_name,
            customer_type_data.customer_bank_acc,
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

@bp.route('/serviceedit/<id>', methods=('GET', 'POST'))
def service_edit(id):
    service_car = ServiceCar.query.get(id)
    if request.method == 'POST':
        json_data = request.get_json()
        description = json_data['description']
        spend_time = json_data['spend_time']
        work_price = json_data['work_price']
        service_car.description = description
        service_car.spend_time = spend_time
        service_car.work_price = work_price
        db.session.commit()
        return jsonify(status="service_edit")

@bp.route('/partedit/<id>', methods=('GET', 'POST'))
def part_edit(id):
    part_car = PartCar.query.get(id)
    if request.method == 'POST':
        json_data = request.get_json()
        part_name = json_data['part_name']
        part_count = json_data['part_count']
        part_price = json_data['part_price']
        full_price = json_data['full_price']
        part_car.part_name = part_name
        part_car.part_count = part_count
        part_car.part_price = part_price
        part_car.full_price = full_price
        db.session.commit()
        return jsonify(status="part_edit")

# service api
@bp.route('/service/<id>', methods=('GET', 'POST'))
def car_service(id):
    if request.method == 'POST':
        json_data = request.get_json()
        description = json_data['description']
        spend_time = json_data['spend_time']
        work_price = json_data['work_price']
        new_service = ServiceCar(spend_time, work_price, description, create_date=datetime.datetime.now(), order_id=id)
        db.session.add(new_service)
        db.session.commit()
        return jsonify(status="car_service_reg")

# service api
@bp.route('/servicedel', methods=('GET', 'POST'))
def del_service():
    if request.method == 'POST':
        json_data = request.get_json()
        service_id = json_data['service_id']
        service = ServiceCar.query.get(int(service_id))
        db.session.delete(service)
        db.session.commit()
        return jsonify(status="service_delete")

@bp.route('/partdel', methods=('GET', 'POST'))
def del_part():
    if request.method == 'POST':
        json_data = request.get_json()
        part_id = json_data['part_id']
        part = PartCar.query.get(int(part_id))
        db.session.delete(part)
        db.session.commit()
        return jsonify(status="part_delete")

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
        order = OrderData.query.order_by(OrderData.id.desc()).first()
        services = ServiceCar.query.filter_by(order_id=id).all()
        return jsonify({'info': [order.serialized], 'service_car': [service.serialized for service in services]})