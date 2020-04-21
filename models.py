from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class Pregunta(db.Model):
    __tablename__ = 'preguntas'

    id = db.Column(db.Integer,primary_key=True)
    materia = db.Column(db.String(50), nullable=False)
    consigna = db.Column(db.String(400), nullable=False)


    @classmethod
    
    def create(self, materia,consigna):
        pregunta = Pregunta(materia=materia,consigna=consigna)
        return pregunta.save()

    def save(self):
        try:
                db.session.add(self)
                db.session.commit()

                return self
        except:
                return False

    def update(self):
        self.save()

    def json(self):
        return {
            'id': self.id,
            'materia': self.materia,
            'consigna': self.consigna
        }        

        