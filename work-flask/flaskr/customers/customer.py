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
            'customer_name': self.customer_name,
            'phone': self.phone,
            'create_date': self.create_date 
        }