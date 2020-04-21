from flask import Flask,request,jsonify
from config import config
from models import db
from models import Pregunta

def create_app(enviroment):
    app = Flask(__name__)

    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app

enviroment = config['development']
app = create_app(enviroment)

@app.route('/', methods=['GET'])
def home():
    data = "prueba"
    return jsonify({'data': data})
 
@app.route('/preguntas', methods=['GET'])
def get_ques():
    preguntas= Pregunta.query.order_by(Pregunta.id).all()
    return jsonify({'preguntas': 
    [{"id": x.id, "materia": x.materia, "consigna": x.consigna} for x in preguntas]
    })

@app.route('/preguntas/<id>', methods=['GET'])
def get_ques_id(id):
    response = {'message': 'sucess'}
    return jsonify(response)    

@app.route('/preguntas', methods=['POST'])
def create_ques():
    json = request.get_json(force=True)

    user = Pregunta.create(json['materia'],json['consigna'])

    return jsonify({'pregunta': user.json() })
   

@app.route('/preguntas/<id>', methods=['PUT'])
def update_ques(id):
    response = {'message': 'success'}
    return jsonify(response)

@app.route('/preguntas/<id>', methods=['DELETE'])
def delete_ques(id):
    response = {'message': 'id'}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=8080)    