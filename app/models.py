from . import db

class PropertyProfile(db.Model):
    
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    pTitle = db.Column(db.String(80))
    description = db.Column(db.String(500))
    number_of_bedrooms=db.Column(db.String(80))
    number_of_bathrooms=db.Column(db.String(80))
    price=db.Column(db.String(80))
    property_type=db.Column(db.String(80))
    location=db.Column(db.String(80))
    photo=db.Column(db.String(80))

    def __init__(self, pTitle, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo ):
        self.pTitle = pTitle
        self.description = description
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.photo = photo
        


    def __repr__(self):
        return '<User %r>' % (self.username)