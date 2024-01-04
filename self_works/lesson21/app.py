from flask import Flask, request, render_template

from sqlalchemy.orm import Session

from self_works.lesson21.data_loader import get_users_id, get_user_data, get_email_from_db
from self_works.lesson21.db import NewUser, engine

app = Flask(__name__)


@app.route('/sync', methods=['POST'])
def sync():
    with Session(autoflush=False, bind=engine) as db:
        for user_id in get_users_id():
            user = get_user_data(user_id)
            new_user = NewUser(name=f"{user['name']}", email=f"{user['email']}", age=f"{user['age']}")
            db.add(new_user)
            db.commit()
            print(new_user.id)
    return 'Sync done'


@app.route('/upload', methods=['POST'])
def upload():
    with Session(autoflush=False, bind=engine) as db:
        for user_id in get_users_id():
            user = get_user_data(user_id)
            if user['email'] not in get_email_from_db():
                new_user = NewUser(name=f"{user['name']}", email=f"{user['email']}", age=f"{user['age']}")
                db.add(new_user)
                db.commit()
                print(new_user.id)
    return 'Upload done'


@app.route('/delete', methods=['POST'])
def drop_all():
    with Session(autoflush=False, bind=engine) as db:
        db.query(NewUser).delete()
        db.commit()
    return 'All data dropped'


@app.route('/users', methods=['GET'])
def get_products():
    if request.method == 'GET':
        with Session(engine) as sss:
            users = sss.query(NewUser).all()
        return render_template('index.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
