from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

from homework_06.forms.places import AddPlaceForm
from homework_06.models.all_models import Place, Category, City
from homework_06.models.database import db

places_app = Blueprint('places_app', __name__)


@places_app.get('/')
def places_list():
    places = Place.query.all()
    return render_template('places/place_list.html', places=places)


@places_app.get('/<int:place_id>')
# @login_required
def place_detail(place_id):
    place = Place.query.filter_by(id=place_id).first()
    return render_template('places/place_detail.html', place=place)


@places_app.get('/category/<int:cat_id>')
def places_by_category(cat_id):
    places = Place.query.join(Category).filter(Category.id == cat_id).all()
    return render_template('places/place_list.html', places=places)


@places_app.get('/city/<int:city_id>')
def places_by_city(city_id):
    places = Place.query.join(City).filter(City.id == city_id).all()
    return render_template('places/place_list.html', places=places)


@places_app.route('/create-place', methods=['POST', 'GET'])
# @login_required
def create_place():
    form = AddPlaceForm()
    categories = [(cat.id, cat.name_category) for cat in Category.query.all()]
    cities = [(city.id, city.name_city) for city in City.query.all()]
    form.category.choices = categories
    form.city.choices = cities
    if form.validate_on_submit():
        name_place = form.name_place.data
        description = form.description.data
        category = form.category.data
        # заглушка
        # author_id = current_user.id
        author_id = 4
        city_id = form.city.data
        rate = form.rate.data
        place = Place(name_place=name_place,
                      description=description,
                      category_id=category,
                      author_id=author_id,
                      city_id=city_id,
                      rate=rate)
        db.session.add(place)
        db.session.commit()
        return redirect(url_for('places_app.place_detail', place_id=place.id))
    return render_template('places/create_place.html', form=form)
