from flask import Flask
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager


# internal imports
from .blueprints.site.routes import site # add this import to grab our site blueprint
from .blueprints.auth.routes import auth
from config import Config
from .models import login_manager, db


# instantiating our Flask app
app = Flask(__name__)  # passing in the __name__ variable which just takes the name of the folder we're in
app.config.from_object(Config)
jwt = JWTManager(app) # allows our app to use JWTManger from anywhere (added security for our api routes)

# wrap our app in login_manager so we can use it wherever in our app
login_manager.init_app(app)
login_manager.login_view = 'auth.sign_in' 
login_manager.login_message = "Your Log In Is Required!"
login_manager.login_message_category = 'warning'




app.register_blueprint(site) # add this here to register your site blueprint
app.register_blueprint(auth)



# instantiating our datbase & wrapping our app
db.init_app(app)
migrate = Migrate(app, db)
cors = CORS(app) # Cross Origin Resource Sharing aka allowing other apps to talk to our flask app/server