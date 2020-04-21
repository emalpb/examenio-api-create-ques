from flask import Flask,request,jsonify
from config import config
from models import db
from models import pregunta

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
app = create_app(enviroment)

app.route('/preguntas', methods=['GET'])
def get_ques():
    preguntas= [pregunta.json() for i in pregunta.query.all()]
    return jsonify({'preguntas': preguntas})

app.route('/preguntas/<id>', methods=['GET'])
def get_ques(id):
    response = {'message': 'sucess'}
    return jsonify(response)    

@app.route('/preguntas', methods=['POST'])
def create_ques():
    json = request.get_json(force=True)

    if json.get('consigna') is None:
        return jsonify({'message' : 'consigna vacia'}),400

    pregunta = pregunta.create(json['consigna'])
    return jsonify({'pregunta':pregunta.json()})    

@app.route('/preguntas/<id>', methods=['PUT'])
def update_ques(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/preguntas/<id>', methods=['DELETE'])
def delete_ques(id):
    response = {'message': 'success'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)    