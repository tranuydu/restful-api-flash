import os
from flask import Flask, request, render_template
#from flask_restful import Resource, Api, reqparse
#from flask_jwt import JWT, jwt_required, current_identity

app = Flask(__name__)
#app.config['PROPAGATE_EXCEPTIONS'] = True # To allow flask propagating exception even if debug is set to false on app
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS']= False
#app.config['SQLALCHEMY_DATABASE_URI']=os.environ.get('DATABASE_URL','sqlite:///data.db') #find out the environement variable on heroku if it is not found we will use local sqlite string
#app.secret_key = 'jose'

#api = Api(app)
@app.route('/', methods=['GET'])
def trangchu():
    return render_template('TrangChu.html')
#jwt = JWT(app, authenticate, identity)

#api.add_resource(Item, '/item/<string:name>')
#api.add_resource(ItemList, '/items')
#api.add_resource(UserRegister, '/register')
#api.add_resource(UserList, '/users')
#api.add_resource(Store, '/store/<string:name>')
#api.add_resource(StoreList, '/stores')

if __name__ == '__main__':
    #from db import db
    #db.init_app(app)
    app.run(port=5000,debug=True)  # important to mention debug=True
