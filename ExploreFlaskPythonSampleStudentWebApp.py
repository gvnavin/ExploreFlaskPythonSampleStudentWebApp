from flask import Flask, flash, render_template, json, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "secretkey"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/student_info'
db = SQLAlchemy(app)
db.init_app(app)

#https://code.tutsplus.com/tutorials/creating-a-web-app-from-scratch-using-python-flask-and-mysql--cms-22972
#https://techarena51.com/blog/flask-sqlalchemy-tutorial/


class Student(db.Model):

    __tablename__ = "student"

    name = db.Column(db.String(100), primary_key=True)
    age = db.Column(db.Integer)
    address = db.Column(db.String(500))

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signUp', methods=['POST', 'GET'])
def signUp():
    print(request.form)
    print(request.method)
    try:
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']

        print("name="+name)
        print("age="+age)
        print("address="+address)

        student = Student(name=name, age=age, address=address)

        db.session.add(student)
        db.session.commit()
        print('Student information is stored in db')

    except Exception as e:
        return json.dumps({'error': str(e)})

    return "Student Information Stored Successfully"


if __name__ == '__main__':
    app.debug = True
    app.run()
