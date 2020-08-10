import connexion
from flask_cors import CORS
from os import environ

debug = environ.get('DEBUG')
if debug is None or debug == '0':
    debug = False
elif debug == '1':
    debug = True
    
port = environ.get('PORT')
if port is None:
    port = 80
else:
    port = int(port)

api = environ.get('API')
if api is None:
    api = 'api.yml'

# Create the application instance
app = connexion.App(__name__, specification_dir=".")
CORS(app.app)
app.add_api(api)

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(debug=debug, port=port)

