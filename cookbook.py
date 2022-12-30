from app import app, db
from app.models import User, Recipe, Ingredient, Measurement


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Recipe': Recipe, 'Ingredient': Ingredient, 'Measurement': Measurement}