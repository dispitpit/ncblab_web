from flask import Blueprint, request, jsonify
import smtplib
from email.mime.text import MIMEText

# 建立 Blueprint：名稱 contact_bp，用於掛載「/api/contact/send」路由
contact_bp = Blueprint('contact_bp', __name__)

@contact_bp.route('/api/contact/send', methods=['POST'])
def send_contact_email():
    # 取得 JSON 請求內容（前端 axios.post('/api/contact/send', {...})）
    data = request.get_json()
    # 欄位預設值：name 預設 Anonymous；email 預設空字串；message 預設空字串
    name = data.get('name', 'Anonymous')
    email = data.get('email', '')
    message = data.get('message', '')

    # 檢查欄位
    if not message:
        return jsonify({'error': 'Message is required'}), 400

    # 建立 email 內容
    content = f"From: {name} <{email}>\n\n{message}"
    msg = MIMEText(content)
    msg['Subject'] = ' 新的網站使用者回饋' # 郵件主旨
    msg['From'] = 'yourserver@example.com' # 寄件位址
    msg['To'] = 'yourinbox@example.com' # 收件位址

    try:
        # 使用 Gmail SMTP（可換成你自己的）
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('yourserver@example.com', 'your-password-or-app-password')
        server.send_message(msg)
        server.quit()
        return jsonify({'success': True})
    except Exception as e:
        # 例外直接回傳錯誤字串（正式上線請去除)
        return jsonify({'error': str(e)}), 500
