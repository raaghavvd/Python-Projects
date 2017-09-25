from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgres://wdpomcmrstrwbc:444591b6b2e162da8db11ed42f32ffa9672a3b41d36385244da71f04abf7542d@ec2-54-197-253-210.compute-1.amazonaws.com:5432/ddkheee1951r7?sslmode=require'

db=SQLAlchemy(app)
class Data(db.Model):
    __tablename__='data'
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self,email_,height_):
        self.email_=email_
        self.height_=height_
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/success",methods=["POST"])
def success():
    if request.method=='POST':
        email=request.form["email_id"]
        height=request.form["height"]
        if db.session.query(Data).filter(Data.email_== email).count()==0:

            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            average_height=db.session.query(func.avg(Data.height_)).scalar()
            average_height=round(average_height,1)
            count=db.session.query(Data.height_).count()




            send_email(email,height,average_height,count)

            return render_template("success.html")
    return render_template('index.html', text= 'Seems like we have got your data . Try again with a different email address!')



if __name__ =="__main__":
    app.debug=True
    app.run()
