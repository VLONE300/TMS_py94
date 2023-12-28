from flask import Flask, request, render_template
import psycopg2
from sqlalchemy.orm import Session
from app import DataLoader
from config import host, user, password, db_name, port
from self_works.lesson21.db import User,engine

app = Flask(__name__)


@app.route('/users', methods=['POST', 'GET'])
def get_products():
    if request.method == 'GET':
        with Session(engine) as sss:
            users = sss.query(User).all()
        return render_template('index.html', users=users)

    elif request.method == 'POST':
        product = User(
            name=request.form['name'],
            carbs=float(request.form['carbs']),
            proteins=float(request.form['proteins']),
            fats=float(request.form['fats']),
            grs=float(request.form['grs']),
        )
        with Session(engine) as sss:
            sss.add(product)
            sss.commit()

            products = sss.query(User).all()
        return render_template('products.html', products=products)




def main():
    base_url = 'http://185.225.232.111:8000'
    data_loader = DataLoader(base_url)

    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        port=port
    )

    data_loader.load_data_to_db(connection)

    connection.close()


if __name__ == "__main__":
    app.run(debug=False)
    main()