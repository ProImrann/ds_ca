# importing the modules required in the route.py
from fileinput import filename

from flask import flash, redirect, render_template, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from restaurant import app, bcrypt, db
from restaurant.forms import Booking, LoginForm, OfferForm, RegistrationForm
from restaurant.models import Offers, User

# -----------------------The home page--------------------------

@app.route("/")
@app.route("/home")
@login_required # You need to log in first in order to acces the home page
def home():
    return render_template("home.html")

# -------------------------------The login page -------------

@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Incorrect Type of user, email or password', 'danger')
    return render_template("login.html", title="Login", form=form)

# --------------------------------logout page --------------------------------
@app.route("/logout", methods=['GET', 'POST'])
def logout(): 
    logout_user()
    return redirect(url_for('login'))

# -------------------The registration page ----------------

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password, type=form.type.data)
        db.session.add(user) 
        db.session.commit()
        flash(f'Account created', 'success')
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)

# --------------------------Add new offer page ----------------

@app.route("/new_offer", methods=['GET', 'POST'])
@login_required
def new_offer():
    form = OfferForm()
    if form.validate_on_submit():
        offer = Offers(offer_name=form.offer_name.data, offer_type=form.offer_type.data, price=form.price.data,description=form.description.data)
        db.session.add(offer)
        db.session.commit()
        flash(f'Offer added', 'success')        
        return redirect(url_for('home'))
    return render_template("add.html", title='new offer', form=form, legend="New offer")

# ----------------------The about page --------------------

@app.route("/about")
def about():
    return render_template("about.html")

# ---------------------------Offer page ------------------------

@app.route("/rooms")
@login_required
def rooms():
    offer = Offers.query.filter(Offers.offer_type == "Room", Offers.status == True)
    img_file = url_for('static', filename= './images/room.jpg')
    return render_template("offers.html", offers=offer, img_file=img_file)

# ---------------------------Dish page ------------------------

@app.route("/dishes")
@login_required
def dishes():
    offer = Offers.query.filter(Offers.offer_type == "Dish", Offers.status == True)
    img_file = url_for('static', filename= './images/dish.jpg')
    return render_template("offers.html", offers=offer, img_file=img_file)

# ---------------------------Sport page ------------------------

@app.route("/sports")
@login_required
def sports():
    offer = Offers.query.filter(Offers.offer_type == "Sport", Offers.status == True)
    img_file = url_for('static', filename= './images/sport.jpg')
    return render_template("offers.html", offers=offer, img_file=img_file)


# ---------------------------Hall conference page ------------------------

@app.route("/Halls/conference")
@login_required
def halls():
    offer = Offers.query.filter(Offers.offer_type == "Conference room", Offers.status == True)
    img_file = url_for('static', filename= './images/conference.jpg')
    return render_template("offers.html", offers=offer, img_file=img_file)

@app.route("/booked")
@login_required
def booked():
    offer = Offers.query.filter(Offers.status == False)
    img_file = url_for('static', filename= './images/home_image.jpg')
    return render_template("offers.html", offers=offer, img_file=img_file)
# ------------------------------------The laptop page-----------------------

@app.route('/offer/<int:offer_id>')
def offer(offer_id):
    offer = Offers.query.get_or_404(offer_id)
    if offer.offer_type == "Room":
        img_file = url_for('static', filename= './images/room.jpg')
    elif offer.offer_type == "Sport":
        img_file = url_for('static', filename= './images/sport.jpg')
    elif offer.offer_type == "Dish":
        img_file = url_for('static', filename= './images/dish.jpg')
    elif offer.offer_type == "Conference room":
        img_file = url_for('static', filename= './images/conference.jpg')
    return render_template('offer.html', title=offer.offer_name, offer=offer, img_file=img_file)
# --------------------------book offer------------------------
@app.route('/offer/<int:offer_id>/buy', methods=['GET','POST'])
@login_required
def buy_offer(offer_id):
    offer = Offers.query.get_or_404(offer_id)
    form = Booking()
    if form.validate_on_submit():
        offer.book_date = form.book_date.data
        offer.status = False
        db.session.commit()
        offer.offer_id = current_user.username
        db.session.commit()
        flash('Bought offer')
        return redirect(url_for('home'))
    return render_template('buy.html', title = 'Buy offer', form = form, legend="Book offer")

# -------------------------- offer update ----------------------
@app.route('/offer/<int:offer_id>/update', methods=['GET','POST'])
@login_required
def update_offer(offer_id):
    offer = Offers.query.get_or_404(offer_id)
    form = OfferForm()
    if form.validate_on_submit():
        offer.offer_name = form.offer_name.data
        offer.description = form.description.data
        offer.price = form.price.data
        offer.offer_type = form.offer_type.data
        db.session.commit()
        flash('Offer Updated', 'success')
    elif request.method =='GET': 
        form.offer_name.data = offer.offer_name
        form.description.data = offer.description
        form.price.data = offer.price
    return render_template('add.html', title = 'Update offer', form = form, legend="Update offer")

# -------------------------- offer delete ----------------------

@app.route('/offer/<int:offer_id>/delete', methods=['GET','POST'])
@login_required
def delete_offer(offer_id):
    offer = Offers.query.get_or_404(offer_id)
    db.session.delete(offer)
    db.session.commit()
    return redirect(url_for('home'))

# --------------------------acount page------------------------
@app.route("/acount")
@login_required
def acount():
    return render_template('acount.html', title='Account')

@app.route("/users")
@login_required
def users():
    user = User.query.filter()
    return render_template("users.html", users=user)
