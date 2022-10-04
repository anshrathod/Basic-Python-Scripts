import json

from flask import Flask, render_template, request, jsonify

from machineLearn import Titanic

app = Flask(__name__)
model = Titanic()


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/titanic', methods=['POST'])
def titanic():
    res = request.values.to_dict()
    pd = model.predict(res)
    print(pd)
    return jsonify({
        'status': int(pd[0])
    })


if __name__ == '__main__':
    app.run(debug=True)
