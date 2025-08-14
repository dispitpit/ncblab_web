啟動local網站: npm run dev 
(*注意: 路徑必須於frontend底下)
-
API串接: 安裝flask連動vue
1.vue裝: npm install axios
2.flaskj裝: pip install flask flask-cors
-
***本端測試***
開啟終端機1：啟動後端
cd backend
pip install -r requirements.txt
python main_api.py    
-
開啟終端機2：啟動前端
cd frontend
npm run dev
*************

if 前端失敗
if 後端失敗
1.套件沒裝
2.標格失敗 -> pip install openpyxl (panda解析檔案用)
pip install secure-smtplib (寄mail用)

Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
解不能裝nmp