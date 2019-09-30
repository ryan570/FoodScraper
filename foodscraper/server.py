import time

import schedule
import wsgiserver
from flask import Flask

from display import display, update

app = Flask(__name__)

app.register_blueprint(display)

if __name__ == '__main__':
    #server = wsgiserver.WSGIServer(app, port=5000)
    #server.start()
    app.run()

    schedule.every().day.at("01:00").do(update)

    while True:
        schedule.run_pending()
        time.sleep(1000)