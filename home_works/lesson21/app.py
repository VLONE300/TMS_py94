from flask import Flask, request, render_template, flash

from sqlalchemy.orm import Session
from home_works.lesson21.db import Product, engine

app = Flask(__name__)

app.config['SECRET_KEY'] = 'qwrtqtyeyuupueqwetq1234'


def get_name():
    with Session(engine) as sss:
        names = sss.query(Product.name).all()
        name_list = [name[0].lower() for name in names]
    return name_list


@app.route('/products', methods=['POST', 'GET'])
def get_products():
    if request.method == 'GET':
        with Session(engine) as sss:
            products = sss.query(Product).all()
        return render_template('products.html', products=products)

    elif request.method == 'POST':
        product = Product(
            name=request.form['name'],
            carbs=float(request.form['carbs']),
            protein=float(request.form['proteins']),
            fats=float(request.form['fats']),
            gramms=float(request.form['grs']),
        )
        with Session(engine) as sss:
            if product.name.lower() not in get_name():
                flash('Product successfully added')
                sss.add(product)
                sss.commit()
            else:
                flash('Product already exists')

            products = sss.query(Product).all()
        return render_template('products.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)
