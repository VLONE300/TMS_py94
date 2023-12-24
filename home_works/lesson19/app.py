from flask import Flask, jsonify, request
import sqlalchemy as db
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

app = Flask(__name__)

client = app.test_client()
engine = create_engine('postgresql://vlone:qwerty1234@localhost/hw_lesson17')

session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = session.query_property()

from models import *

Base.metadata.create_all(bind=engine)


@app.route('/', methods=['GET'])
def get_list():
    products = Product.query.all()
    serialized = []
    for product in products:
        serialized.append({
            'id': product.id,
            'name': product.name,
            'protein': product.protein,
            'fats': product.fats,
            'carbs': product.carbs,
        })
    return jsonify(serialized)


@app.route('/', methods=['POST'])
def update_list():
    new_data = Product(**request.json)
    session.add(new_data)
    session.commit()
    serialized = {
        'id': new_data.id,
        'name': new_data.name,
        'protein': new_data.protein,
        'fats': new_data.fats,
        'carbs': new_data.carbs
    }

    return jsonify(serialized)


@app.route('/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    item = Product.query.filter(Product.id == product_id).first()
    params = request.json
    if not item:
        return {'message': 'No products with this id'}, 400
    for key, value in params.items():
        setattr(item, key, value)
    session.commit()
    serialized = {
        'id': item.id,
        'name': item.name,
        'protein': item.protein,
        'fats': item.fats,
        'carbs': item.carbs
    }
    return serialized


@app.route('/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    item = Product.query.filter(Product.id == product_id).first()
    if not item:
        return {'message': 'No products with this id'}, 400
    session.delete(item)
    session.commit()
    return '', 204


@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


if __name__ == '__main__':
    app.run(debug=True)
