# backend/api/excel.py

from flask import Blueprint, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import os

# 建立 Blueprint：名稱 excel_bp，供主程式 app.register_blueprint(excel_bp)
excel_bp = Blueprint('excel_bp', __name__)

# 暫存上傳檔案
TEMP_PATH = os.path.join(os.path.dirname(__file__), '..', 'temp_uploaded.xlsx')
TEMP_PATH = os.path.abspath(TEMP_PATH)

@excel_bp.route('/api/excel/upload', methods=['POST'])
def upload_excel():
    # 從 multipart/form-data 取得檔案
    file = request.files.get('file')
    print(" 收到的檔案物件：", file)
    if file:
        print(" 檔名：", file.filename)
    else:
        print("沒有收到檔案")

    # 簡單副檔名判斷（.xlsx / .csv）
    if file and file.filename.endswith(('.xlsx', '.csv')):
        # 無條件存到 TEMP_PATH（無論原始是否為 CSV）
        file.save(TEMP_PATH)
        try:
            if file.filename.endswith('.xlsx'):
                df = pd.read_excel(TEMP_PATH)
            else:
                df = pd.read_csv(TEMP_PATH)
            # df = pd.read_excel(TEMP_PATH) if file.filename.endswith('.xlsx') else pd.read_csv(TEMP_PATH)
            print("欄位：", df.columns.tolist())
            return jsonify({'columns': df.columns.tolist()})
        except Exception as e:
            print("pandas 讀檔錯誤：", e)
            return jsonify({'error': '讀取 Excel/Csv 檔案失敗'}), 500
    return jsonify({'error': 'Invalid file format'}), 400

@excel_bp.route('/api/excel/regression', methods=['POST'])
def regression():
    try:
        data = request.get_json()
        target = data['target']  # 使用者選的 y

        df = pd.read_excel(TEMP_PATH)
        if target not in df.columns:
            return jsonify({'error': 'Invalid target column'}), 400

        df = df.select_dtypes(include=['number']).dropna()
        y = df[target]
        X = df.drop(columns=[target])

        model = LinearRegression()
        model.fit(X, y)
        y_pred = model.predict(X)

        r2 = r2_score(y, y_pred)
        mse = mean_squared_error(y, y_pred)

        return jsonify({
            'r2_score': round(r2, 4),
            'mse': round(mse, 4),
            'coefficients': dict(zip(X.columns, model.coef_.round(4))),
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
