from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from weasel import weasel
from flask.json import jsonify
# import datetime
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def compute():
    target = request.form['target']
    chance = int(request.form['chance'])
    pool_size = int(request.form['pool_size'])
    # begin = datetime.datetime.now().timestamp()
    output = weasel(target, chance, pool_size)
    # end = datetime.datetime.now().timestamp()
    # time = end - begin
    # return jsonify({'generations': output, 'time': time})
    return render_template('result.html', output=output, target=target)

if __name__ == '__main__':
    app.run(debug=True, port=8888)
