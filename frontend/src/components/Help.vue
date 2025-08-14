<template>
  <div class="help-container">
    <h2>Help</h2>
    <p>網站使用說明、目錄結構與前後端對應。</p>

    <h3>專案結構簡介</h3>
    <p>本網站分為兩大部分：</p>
    <ul>
      <li><strong>前端 frontend/</strong>：提供使用者介面</li>
      <li><strong>後端 backend/</strong>：提供模型與 API 功能</li>
    </ul>

    <h3>前端結構導覽</h3>
    <table>
      <thead>
        <tr>
          <th>功能說明</th>
          <th>檔案位置</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>瀏覽器分頁圖標與標題</td>
          <td><code>frontend/index.html</code></td>
        </tr>
        <tr>
          <td>頁面按鈕與主要路由</td>
          <td><code>frontend/App.vue</code></td>
        </tr>
        <tr>
          <td>頁首（Logo 與標題）</td>
          <td><code>frontend/components/PageHeader.vue</code></td>
        </tr>
        <tr>
          <td>頁尾</td>
          <td><code>frontend/components/PageFooter.vue</code></td>
        </tr>
        <tr>
          <td>首頁內容</td>
          <td><code>frontend/components/HomeView.vue</code></td>
        </tr>
        <tr>
          <td>關於頁面</td>
          <td><code>frontend/components/AboutView.vue</code></td>
        </tr>
        <tr>
          <td>聯絡我們頁面</td>
          <td><code>frontend/components/ContactView.vue</code></td>
        </tr>
        <tr>
          <td>資料集工具頁面</td>
          <td><code>frontend/components/Datasets.vue</code></td>
        </tr>
        <tr>
          <td>本頁說明</td>
          <td><code>frontend/components/Help.vue</code></td>
        </tr>
      </tbody>
    </table>

    <h3>工具對應的後端 API</h3>
    <table>
      <thead>
        <tr>
          <th>前端元件</th>
          <th>後端 Python 檔案</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><code>FlowerPredict_tool.vue</code></td>
          <td><code>backend/api/flower.py</code></td>
        </tr>
        <tr>
          <td><code>Sum_tool.vue</code></td>
          <td><code>backend/api/sum.py</code></td>
        </tr>
        <tr>
          <td><code>ExcelAnalysis_tool.vue</code></td>
          <td><code>backend/api/excel.py</code></td>
        </tr>
        <tr>
          <td><code>ContactView.vue</code></td>
          <td><code>backend/api/contact.py</code></td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<style scoped>
/* 整頁背景改成灰色 */
body {
  background-color: #eceff4; /* 柔和灰 */
  margin: 0;
}

/* 卡片容器 */
.help-container {
  max-width: 800px;
  margin: 20px auto;
  padding: 5px;
  /* background-color: #ffffff; 卡片白底 */
  /* border-radius: 12px; */
  /* box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08); */
  font-family: var(--font-body, 'Inter', sans-serif);
  color: #333;
  line-height: 1.7;
}

/* 主標題 */
h2 {
  font-size: 1.7rem;
  color: rgb(98, 121, 197); /* ⬅️ 新主題色 */
  margin-bottom: 16px;
  font-family: var(--font-heading, 'Playfair Display', serif);
}

/* 副標題 */
h3 {
  font-size: 1.25rem;
  margin-top: 32px;
  margin-bottom: 12px;
  color: rgb(98, 121, 197); /* 同樣主題色 */
}

/* 內文段落 */
p {
  margin-bottom: 12px;
}

/* 清單樣式 */
ul {
  list-style-type: disc;
  padding-left: 1.5em;
  margin-bottom: 16px;
}

/* 表格樣式 */
table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 12px;
  margin-bottom: 32px;
  font-size: 0.95rem;
}

th, td {
  padding: 12px 16px;
  border: 1px solid #ddd;
  text-align: left;
  background-color: #ffffff;
}

th {
  background-color: #eaf1ff;
  font-weight: 600;
  color: #222;
}

/* 行內程式碼 */
code {
  background-color: #f0f0f0;
  padding: 2px 6px;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  font-size: 0.9em;
}
</style>

