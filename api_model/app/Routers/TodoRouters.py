from flask import Blueprint, request, json
from ..Controllers.Todo import greedySearch
from ..Controllers.TodoLinhKien import predict

todo = Blueprint('todo', __name__)

# http://localhost:5000/api/predict/?seq=abc  method = GET
@todo.route('/api/predict/', methods=['GET'])
def predict_dien_dau():
    seq = request.args['seq']
    try:
        return greedySearch(seq), 200
    except:
        return "Chưa có trong từ điển", 400

@todo.route('/api/predict1/', methods=['GET'])
def predict_phan_lop():
    seq = request.args['seq']
    try:
        return predict(seq), 200
    except:
        return "Lỗi", 400