from flask import Flask
from flask import request
from flask import jsonify
from flask import render_template
from datetime import datetime
from weasel import Mutation
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        target = request.form['target']
        return render_template('result.html', target=target)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=8888)
