from flask import *
from flask_basicauth import BasicAuth

app = Flask(__name__)
basic_auth = BasicAuth(app)

app.config['BASIC_AUTH_USERNAME'] = 'guest'
app.config['BASIC_AUTH_PASSWORD'] = 'rabbitwitholives77'

@app.route("/", methods = ['GET'])
def index():
    return render_template('index.html')

@app.route("/basketball", methods = ['GET'])
@basic_auth.required
def topic1():
    return render_template('basketball.html')
    
@app.route("/food", methods = ['GET'])
@basic_auth.required
def topic2():
    return render_template('food.html')

@app.route("/television", methods = ['GET'])
@basic_auth.required
def topic3():
    return render_template('television.html')

@app.route("/finance", methods = ['GET'])
@basic_auth.required
def topic4():
    return render_template('finance.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
