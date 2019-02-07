from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from datetime import datetime
from weasel import weasel
app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         # Add client side validation later
#         # Restrict string length
#         # Restrict characters to lower case
#         # Restrict chance of mutation
#         # Restrict generation size
#         target = request.form['target']
#         chance = int(request.form['chance'])
#         pool_size = int(request.form['pool_size'])
#         output = weasel(target, chance, pool_size)
#         return render_template('result.html', output=output)
#     else:
#         return render_template('index.html')


@app.route('/', methods=['GET'])
def compute():
    target = request.form['target']
    chance = int(request.form['chance'])
    pool_size = int(request.form['pool_size'])
    output = weasel(target, chance, pool_size)
    return output


if __name__ == '__main__':
    app.run(debug=True, port=8888)
