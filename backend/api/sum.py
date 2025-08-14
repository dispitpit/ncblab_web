from flask import Blueprint, request, jsonify

sum_bp = Blueprint('sum_bp', __name__)

@sum_bp.route('/api/sum', methods=['POST'])
def calc_sum():
    """
    接收 JSON 格式的請求，包含 a、b、c 三個欄位，
    回傳它們的總和。
    """
    # 從請求中解析 JSON
    data = request.get_json()

    # 從 JSON 中取 a、b、c，若缺少則預設為 0
    a = data.get('a', 0)
    b = data.get('b', 0)
    c = data.get('c', 0)

    # 回傳 JSON 格式的結果
    return jsonify({'sum': a + b + c})
