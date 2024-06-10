from flask import Flask
from public import public
from admin import admin
from pharmacy import pharmacy
from distributor import distributor
from manufacturer import manufacturer
from api import api


app=Flask(__name__)
app.secret_key="key"


app.register_blueprint(public)
app.register_blueprint(admin,url_prefix='/admin')
app.register_blueprint(pharmacy,url_prefix='/pharmacy')
app.register_blueprint(distributor,url_prefix='/distributor')
app.register_blueprint(manufacturer,url_prefix='/manufacturer')
app.register_blueprint(api,url_prefix='/api')



app.run(debug=True,host="0.0.0.0",port=5955)


