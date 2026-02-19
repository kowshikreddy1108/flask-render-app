# #
# # from flask import Flask,render_template,url_for
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime
# #
# # app=Flask(__name__)
# # app.config["SQLALCHEMY_DATABASE_URI"]='sqlite:///text.db'
# # db=SQLAlchemy(app)
# #
# # class Todo(db.Model):
# #     id=db.Column(db.Integer,primary_key=True)
# #     content=db.Column(db.String(200),nullable=False)
# #     date_created=db.Column(db.DateTime,default=datetime.utcnow)
# #
# #
# #     def __repr__(self):
# #         return "<Task %r>" %self.id
# # #
# # # @app.route('/')
# # # def index():
# # #     return render_template("home.html")
# #
# # if __name__ == "__main__":
# #     with app.app_context():
# #         db.create_all()
# #     app.run(debug=True)
#
#
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime
#
# app = Flask(__name__)
#
# # Database configuration
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///text.db"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
#
# db = SQLAlchemy(app)
#
# # Model (Table)
# class Todo(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     content = db.Column(db.String(200), nullable=False)
#     date_created = db.Column(db.DateTime, default=datetime.utcnow)
#
#     def __repr__(self):
#         return f"<Task {self.id}>"
#
# # Simple route
# @app.route("/")
# def home():
#     return "Database will be created!"
#
# if __name__ == "__main__":
#     # Create database inside application context
#     with app.app_context():
#         db.create_all()
#         print("Database created successfully!")
#
#     app.run(debug=True)
#


##creating rotes##


###EXAMPLE1####
#
# from flask import Flask,render_template
# import os
#
# app=Flask(__name__)
# @app.route('/')
# def home():
#     return render_template("home.html")
#
# @app.route('/about')
# def about():
#     return render_template("about.html")
#
#
# if __name__=="__main__":
#     port=int(os.environ.get("PORT",5000))
#     app.run(debug=True,host='0.0.0.0',port=port)




##EXAMPLE 2###
from flask import Flask,render_template,request,redirect,url_for
import os

app=Flask(__name__)
@app.route("/")
def home():
    tech=["HTML","CSS","PYTHON"]
    name="30 days of Python Programming"
    return render_template("home.html",techs=tech,name=name,title="Home")
@app.route("/about")
def about():
    name="30days of python"
    return render_template("about.html",name=name,title="about us")
@app.route("/post")
def post():
    name="Text analyzer"
    return render_template("post.html",name=name,title=name)

if __name__=="__main__":
    port=int(os.environ.get("PORT",5000))
    app.run(debug=True,host='0.0.0.0',port=port)