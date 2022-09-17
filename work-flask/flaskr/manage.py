import datetime
from flask import (
    Blueprint, request, jsonify
)
from flaskr import db
from flaskr.customers.customer import Customer

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

@bp.route('/list', methods=('GET', 'POST'))
def all_customers():
    if request.method == 'GET':
        customers = Customer.query.order_by(desc("id")).all()
        return jsonify({'customers': [customer.serialized for customer in customers]})