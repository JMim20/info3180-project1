from . import db

class PropertyProfile(db.Model):
    
    __tablename__ = 'property_profiles'

    id = db.Column(db.Integer, primary_key=True)
    property_title = db.Column(db.String(80))
    description = db.Column(db.String(500))
    number_of_bedrooms=db.Column(db.String(80))
    number_of_bathrooms=db.Column(db.String(80))
    price=db.Column(db.String(80))
    property_type=db.Column(db.String(80))
    location=db.Column(db.String(80))
    photo_name=db.Column(db.String(80))

    def __init__(self, property_title, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo_name ):
        self.property_title = property_title
        self.description = description
        self.number_of_bedrooms = number_of_bedrooms
        self.number_of_bathrooms = number_of_bathrooms
        self.price = price
        self.property_type = property_type
        self.location = last_name
        self. photo_name =  photo_name


def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support

    def __repr__(self):
        return '<User %r>' % (self.username)