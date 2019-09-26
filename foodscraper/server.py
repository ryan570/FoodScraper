from flask import Flask, render_template
import wsgiserver

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    #server = wsgiserver.WSGIServer(app, port=5000)
    #server.start()
    app.run()