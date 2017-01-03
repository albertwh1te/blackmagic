from flask import Flask, render_template
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'test'
mongo = PyMongo(app)


@app.route('/')
def home_page():
    online_users = mongo.db.restaurants.find().limit(10)
    # print(online_users.count())
    # for i in online_users:
    #     print(i['name'])
    #     print(type(i))
    return render_template('index.html',
        online_users=online_users)


if __name__ == "__main__":
    app.run(debug=True)
