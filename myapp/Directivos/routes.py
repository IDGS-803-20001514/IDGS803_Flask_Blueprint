from flask import Blueprint

directivos = Blueprint('directivos', __name__)

@directivos.route('/getDirectivos', methods=['GET'])
def getDirectivos():
    return {'Key': 'Directivos'}