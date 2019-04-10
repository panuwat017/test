from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.pulse.queue import QueueRegister

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pymssql://adaptersa:ADi3250#@u1x@27.254.68.206:61433/AnalyticaAPI'
app.config['SQLALCHEMY_BINDS'] = {
    "pulse":"mssql+pymssql://adaptersa:ADi3250#@u1x@27.254.68.206:61433/AdapterPulse",
    "bonchon":"mssql+pymssql://adaptersa:ADi3250#@u1x@27.254.68.206:61433/Analytica_Bonchon"
}
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'panuwat'
api = Api(app)

app.config['JWT_AUTH_URL_RULE'] = '/authen'
jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
#pulse routing
api.add_resource(QueueRegister,'/pulse/queue')

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=8000, debug=True)