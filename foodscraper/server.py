import wsgiserver
from flask import Flask

app = Flask(__name__)

app.register_blueprint(display)

if __name__ == '__main__':
    #server = wsgiserver.WSGIServer(app, port=5000)
    #server.start()
    app.run()