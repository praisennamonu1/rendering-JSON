from flask import Flask, jsonify
# jsonify is used to convert data types into JSON format.

app = Flask(__name__)

@app.route('/')
def home():
    return 'I am Preno'

@app.route('/number')
def number():
    return jsonify(42)

@app.route('/list')
def some_list():
    return jsonify(['Naruto', 'AOT', 'HxH'])

@app.route('/dict')
def some_dict():
    return jsonify({'name': 'Eren', 'age': 27, 'city': 'Paradis'})

if __name__ == '__main__':
    app.run(debug=True)