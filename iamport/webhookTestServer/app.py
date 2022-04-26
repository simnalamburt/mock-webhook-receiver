from flask import Flask, request, Response
import time

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/webhook/post/<code>/<delay>', methods=['POST'])
def webhook_post(code, delay):
    time.sleep(int(delay))

    return Response("Good!", status=code, mimetype='application/json')


@app.route('/webhook/get', methods=['GET'])
def webhook_get():
    args = request.args
    code = args.get('code', default='200', type=str)
    delay = args.get('delay', default=0, type=int)

    time.sleep(delay)

    return Response("Good!", status=code, mimetype='application/json')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
