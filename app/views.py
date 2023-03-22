"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""
import os
from app import app, db
from flask import render_template, request, redirect, url_for,flash,send_from_directory
from werkzeug.utils import secure_filename
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
    return render_template('about.html', name="Jamila McGowan")

@app.route('/properties/create', methods=['GET', 'POST'])
def create_property():
    form = AddPrpertyForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            photo_upld=form.photo.data
            filename= secure_filename(photo_upld.filename)
            photo_upld.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            pTitle=form.pTitle.data
            description=form.description.data
            number_of_bedrooms=form.number_of_bedrooms.data
            number_of_bathrooms=form.number_of_bathrooms.data
            price=form.price.data
            property_type=form.property_type.data
            location=form.location.data
            photo_upld=filename

            addedProperty= PropertyProfile(pTitle, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo_upld)
            db.session.add(addedProperty)
            db.session.commit()
            # db = connect_db()
            # cur = db.cursor()
            # cur.execute('insert into PropertyProfile(property_title, description, number_of_bedrooms, number_of_bathrooms, price, property_type, location, photo_name ) values (%s, %s, %s, %s, %s, %s, %s, %s)', addedProperty)
            flash('Form Submitted Successfuly!', 'success')
            return redirect(url_for('properties'))
    flash_errors(form)
    return render_template('add_property.html', form=form)


def get_uploaded_images():
    uploads_dir = os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER'])
    filenames = []
    for filename in os.listdir(uploads_dir):
        if os.path.isfile(os.path.join(uploads_dir, filename)):
            filenames.append(filename)
    return filenames 

@app.route('/uploads/<filename>')
def get_image(filename):

    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), filename)

 
def u_images():
    fileNames = get_uploaded_images()
    image_files = [url_for('get_image', filename=filename) for filename in fileNames if filename.endswith(('.jpg', '.JPG', '.png', '.PNG'))]
    return (image_files)

@app.route('/properties')
def properties():
    eimages=u_images()
    vproperties= db.session.execute(db.select(PropertyProfile)).scalars()
    return render_template('properties.html', vproperties=vproperties, eimages=eimages)


@app.route('/properties/<propertyid>')
def view_property(propertyid):
    propertyid = int(propertyid)
    selected_property = db.session.execute(db.select(PropertyProfile).filter_by(id=propertyid )).scalar_one()
    if selected_property:
        return render_template('property.html', selected_property=selected_property)

app.route('/uploads/<filename>')
def get_image(vfilename):

    return send_from_directory(os.path.join(os.getcwd(), app.config['UPLOAD_FOLDER']), vfilename)

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
