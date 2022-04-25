from flask import Flask, request, Response
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook', methods=['GET'])
def webhook():
    args = request.args
    code = args.get('code', default='200', type=str)
    delay = args.get('delay', default=0, type=int)

    time.sleep(delay)

    return Response("Good!", status=code, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
