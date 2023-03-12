"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app
from flask import render_template, request, redirect, url_for,send_from_directory
from werkzeug.utils import secure_filename
from app.forms import AddPrpertyForm
from .models import PropertyProfile
from .forms import AddPrpertyForm

###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

###
# Added functions for project 1
###

@app.route('"/properties/create', methods=['GET','POST'])
def create_property():
    form = AddPrpertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            
            pTile=form.pTile.data
            description=form.description.data
            numBedrooms=form.numBedrooms.data
            numBathrooms=form.numBathrooms.data
            price=form.price.data
            pType=form.pType.data
            location=form.location.data
            
            photo=form.photo.data
            filename= secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            addedProperty= (pTile, description, numBedrooms, numBathrooms, price, pType, location, filename)
            db = connect_db()
            cur = db.cursor()
            cur.execute('insert into PropertyProfile(property_title, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo_name ) values (%s, %s, %s, %s, %s, %s, %s, %s)', addedProperty)
    
            db.commit()

            flash('Form Submitted Successfuly!', 'success')
            return render_template('properties.html', 
            pTile=pTile,
            description=description,
            numBedrooms=numBedrooms,
            numBathrooms=numBathrooms,
            price=price,
            pType=pType,
            location=location,
            filename=filename)

    flash_errors(form)
    return render_template('addProperty.html', form=form)

def get_property_images():
    pImage_dir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
    filenames = []
    for filename in os.listdir(uploads_dir):
        if os.path.isfile(os.path.join(uploads_dir, filename)):
            filenames.append(filename)
    return filenames 

#app.route('/uploads/<filename>')
def get_image(filename):

    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)


@app.route('/properties')
def properties():


    fileNames = get_property_images()
    property_images = [url_for('get_image', filename=filename) for filename in fileNames if filename.endswith(('.jpg', '.JPG', '.png', '.PNG'))]

    db = connect_db()
    cur = db.cursor()
    cur.execute('select property_title, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo_name from PropertyProfile order by
    id desc')
    eProperty = cur.fetchall()
    return render_template('properties.html', property_images=property_images, eProperty=eProperty)


# @app.route("/uploads/<filename>")
# def get_uploaded_file(filename):
#     root_dir = os.getcwd()

#     return send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
