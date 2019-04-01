'''         Important Note - This program is written to run from the virtual environment named section4. The library
            used here like flask_restful, is installed only in virtual environment path, not in the regular path which
            intellji is referring.

            Follow these steps to run this application -
                1. Go to command line and type 'workon section4'
                2. Run the app - 'python app.py'. Trigger the requests from browser or postman
                3. To stop the app - 'cntl + c'
                4. Deactivate the virtual environment - 'deactivate'
'''

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'TestingOnly'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)  #/auth endpoint

api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/item/???????
api.add_resource(Store, '/store/<string:name>')
api.add_resource(ItemList, '/items')  # http://127.0.0.1:5000/items
api.add_resource(StoreList, '/stores')  # http://127.0.0.1:5000/items

api.add_resource(UserRegister, '/register')  # http://127.0.0.1:5000/items

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)


