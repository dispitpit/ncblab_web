from flask import Flask
from flask_cors import CORS

# 匯入你所有的 API Blueprint
# 說明：
# - 每個子域功能用一個 Blueprint 拆分，便於模組化與測試
# - 路徑如 api/sum.py 內部應有：sum_bp = Blueprint('sum', __name__, url_prefix='/api/sum')
from api.sum import sum_bp
from api.excel import excel_bp
from api.flower import flower_bp
# from api.protein import protein_bp
# from api.urlinfo import urlinfo_bp
# from api.crawler import crawler_bp
# from api.nlp import nlp_bp

# ===== 建立 Flask 應用 =====
app = Flask(__name__)
CORS(app)  # 解決跨域問題

# 註冊所有 Blueprint
app.register_blueprint(sum_bp)
app.register_blueprint(flower_bp)
app.register_blueprint(excel_bp)
# app.register_blueprint(protein_bp)
# app.register_blueprint(urlinfo_bp)
# app.register_blueprint(crawler_bp)
# app.register_blueprint(nlp_bp)

# 靜態檔案路徑（提供 /static/... 圖片）
@app.route('/static/<path:filename>')
def serve_static(filename):
    from flask import send_from_directory
    return send_from_directory('./frontend/static', filename)

# 測試用首頁（可選）
@app.route('/')
def index():
    return {'message': 'Backend is running.'}

# ===== 啟動應用（僅開發用） =====
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
