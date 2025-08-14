<script setup>
import { ref } from 'vue'
import axios from 'axios'

const file = ref(null)
const columns = ref([])
const target = ref('')
const result = ref(null)
const error = ref('')
const loading = ref(false)

// 上傳 Excel
async function handleUpload(event) {
  result.value = null
  error.value = ''
  columns.value = []
  const selectedFile = event.target.files[0]
  if (!selectedFile) return

  const formData = new FormData()
  formData.append('file', selectedFile)

  loading.value = true
  try {
    const res = await axios.post('/api/excel/upload', formData)
    columns.value = res.data.columns
  } catch (err) {
    console.error("error：", err)
    error.value = '無法上傳檔案或檢視欄位'
  } finally {
    loading.value = false
  }
}

// 使用範例 Excel
async function loadExampleFile() {
  result.value = null
  error.value = ''
  columns.value = []

  loading.value = true
  try {
    const response = await fetch('/sample_data.xlsx')
    if (!response.ok) {
      throw new Error(`載入失敗 HTTP ${response.status}`)
    }
    const blob = await response.blob()
    const formData = new FormData()
    formData.append('file', new File([blob], 'sample_data.xlsx'))

    const res = await axios.post('/api/excel/upload', formData)
    columns.value = res.data.columns
  } catch (err) {
    console.error('無法載入範例檔案:', err)
    error.value = '無法載入範例檔案'
  } finally {
    loading.value = false
  }
}


// 清除表單
function clearAll() {
  file.value = null
  columns.value = []
  target.value = ''
  result.value = null
  error.value = ''
}

// 送出迴歸分析
async function runRegression() {
  result.value = null
  error.value = ''
  if (!target.value) {
    error.value = '請選擇一個目標欄位'
    return
  }

  loading.value = true
  try {
    const res = await axios.post('/api/excel/regression', {
      target: target.value
    })
    result.value = res.data
  } catch (err) {
    error.value = '分析失敗，請確認欄位資料是否為數值型'
  } finally {
    loading.value = false
  }
}

// 下載分析結果為 CSV
function downloadResult() {
  if (!result.value) return

  let csv = 'Feature,Coefficient\n'
  for (const [feature, coef] of Object.entries(result.value.coefficients)) {
    csv += `${feature},${coef}\n`
  }
  csv += `\nR2 Score,${result.value.r2_score}\nMSE,${result.value.mse}\n`

  const blob = new Blob([csv], { type: 'text/csv' })
  const link = document.createElement('a')
  link.href = URL.createObjectURL(blob)
  link.download = 'regression_result.csv'
  link.click()
}
</script>

<template>
  <div class="excel-tool">
    <h3 class="tool-title">Excel Regression Analysis</h3>

    <input type="file" accept=".xlsx,.csv" @change="handleUpload" />

    <div class="send-buttons">
      <button @click="loadExampleFile">Example</button>
      <button @click="clearAll">Clear</button>
    </div>

    <div v-if="loading">
      <p>in processing...</p>
    </div>

    <div v-if="columns.length">
      <p>請選擇要預測的目標欄位：</p>
      <select v-model="target">
        <option disabled value="">-- Choose --</option>
        <option v-for="col in columns" :key="col" :value="col">{{ col }}</option>
      </select>
      <button @click="runRegression">Send</button>
    </div>

    <div v-if="result" class="result">
      <h4>Analysis Result</h4>
      <p><strong>R² Score:</strong> {{ result.r2_score }}</p>
      <p><strong>MSE:</strong> {{ result.mse }}</p>
      <h5>迴歸係數：</h5>
      <ul>
        <li v-for="(coef, feature) in result.coefficients" :key="feature">
          {{ feature }}: {{ coef }}
        </li>
      </ul>
      <button @click="downloadResult">download reuslt CSV </button>
    </div>

    <p v-if="error" class="error-msg">{{ error }}</p>
  </div>
</template>

<style scoped>

.tool-title {
  font-size: 1.4rem;
  margin-bottom: 16px;
  color: rgb(0, 0, 0);
  font-family: var(--font-heading, 'Playfair Display', serif);
}

.excel-tool {
  padding: 20px;
}
.send-buttons{
  display: flex;
  flex-wrap: wrap;
  gap: 28px;
  justify-content: center;
  margin-top: 20px;
}
.send-buttons button {
  /* margin-top: 12px;
  padding: 6px 12px;
  cursor: pointer; */
  padding: 10px 20px;
  font-size: 15px;
  border: none;
  background-color: #5d9ff5;
  color: white;
  /* border-color: black; */
  border-radius: 10px;
  cursor: pointer;
  /* font-size: 15px; */
  /* font-variant: 'small-caps' */
  font-family: 'Noto Sans TC', sans-serif;
  /* font-family: 'EB Garamond', serif; */
  font-variant: small-caps;
  letter-spacing: 0.11em;
}

.send-buttons button:hover {
  background-color: #d2b3fc;
}
select {
  margin: 10px;
}
button {
  padding: 8px 14px;
  margin-top: 8px;
  cursor: pointer;
}
.result {
  margin-top: 20px;
  padding: 12px;
  background: #eef;
  border-radius: 8px;
}
.error-msg {
  color: red;
  margin-top: 10px;
}
</style>
