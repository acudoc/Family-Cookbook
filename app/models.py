from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    recipes = db.relationship('Recipe', backref='author', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp =db.Column(db.DateTime, index=True, default=datetime.utcnow)
    title = db.Column(db.String(120), index=True)
    description = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    ingredients = db.relationship('Ingredient', backref='recipe', lazy='dynamic')

    def __repr__(self):
        return '<Recipe {}>'.format(self.recipe)

class Ingredient(db.Model):
    __tablename__ = 'ingredient'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'))
    measurement_id = db.Column(db.Integer, db.ForeignKey('measurement.id'))
    measurement = db.relationship('Measurement', backref='ingredient', foreign_keys=[measurement_id])

    def __repr__(self):
        return '<Ingredient {}>'.format(self.ingredient)

class Measurement(db.Model):
    __tablename__ = 'measurement'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.id'))

    def __repr__(self):
        return '<Measurement {}>'.format(self.measurement)



