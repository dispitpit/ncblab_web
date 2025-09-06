# ncblab_web

### 平台介紹
本 project 是專為 NcbLab 成員設計的基礎模板，方便大家將各種模型快速部署到網站上。
你可以省去美編、網站架構與設定檔等繁瑣處理，只需 download 本專案並參照提供的 PPT 說明，即可根據自己的需求進行修改和擴充。

如有任何問題或需要 PPT 檔案，洽 Amanda。

### 安裝步驟

下載後在終端機依序輸入：

#### 1. 前端 Vue

```bash
npm install axios
```

#### 2. 後端 Flask

```bash
pip install flask flask-cors
```

---

### 本端測試

#### 開啟終端機1：啟動後端

```bash
cd backend
pip install -r requirements.txt
python main_api.py
```

---

#### 開啟終端機2：啟動前端

```bash
cd frontend
npm run dev
```

*************

#### 注意事項:

此port和host設定為公開網站使用
如在本地端測試，請修改port、host為適合本地的設定，避免前後端無法連接
