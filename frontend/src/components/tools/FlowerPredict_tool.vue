<template>
  <div class="predict-tool">
    <h2 class="tool-title">Flower Classification Tool</h2>
    <p><br>Please upload a flower image or choose a sample image. 
    <br>The model will predict which type of flower it is.<br><br></p>

    <!-- 上傳區 -->
    <input type="file" @change="handleFile" accept="image/*" />

    <!-- 預覽圖片 -->
    <div v-if="previewUrl">
      <img :src="previewUrl" alt="Preview" width="300" />
    </div>

    <!-- 按鈕區 -->
    <div class="send-buttons">
      <button @click="clearImage">Clear</button>
      <button @click="loadExampleImage">Example</button>
      <button @click="submit">Submit</button>
    </div>

    <!-- 顯示結果 -->
    <p v-if="result">Result: {{ result }}</p>
    <p v-if="error" class="error"> {{ error }}</p>
    <p v-if="loading">Predicting...</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const imageFile = ref(null)
const examplePath = ref('')
const previewUrl = ref('')
const result = ref('')
const error = ref('')
const loading = ref(false)

function handleFile(event) {
  const file = event.target.files[0]
  if (file) {
    imageFile.value = file
    previewUrl.value = URL.createObjectURL(file)
    examplePath.value = ''
    result.value = ''
  }
}

function clearImage() {
  imageFile.value = null
  examplePath.value = ''
  previewUrl.value = ''
  result.value = ''
  error.value = ''
}

async function loadExampleImage() {
  try {
    const filename = 'flower_example.jpg'  // 假設你放在 public 根目錄

    // fetch public 裡的圖片
    const response = await fetch(`/${filename}`)
    const blob = await response.blob()

    // 模擬一個 File 物件（像使用者選擇圖片）
    const file = new File([blob], filename, { type: blob.type })

    // 設定相關狀態
    imageFile.value = file
    previewUrl.value = URL.createObjectURL(file)
    examplePath.value = ''
    result.value = ''
    error.value = ''
  } catch (err) {
    error.value = 'Failed to load example image.'
  }
}


// async function loadExampleImage() {
//   try {
//     const res = await axios.get('/api/flower/example')
//     const filename = res.data.filename
//     previewUrl.value = '/flower_example.jpg'  // 顯示圖片
//     examplePath.value = 'flower_example.jpg'
//     imageFile.value = null
//     result.value = ''
//     error.value = ''
//   } catch (err) {
//     error.value = ' Failed to load example image.'
//   }
// }



async function submit() {
  error.value = ''
  result.value = ''
  loading.value = true

  try {
    const formData = new FormData()
    if (imageFile.value) {
      formData.append('file', imageFile.value)
    } else if (examplePath.value) {
      formData.append('example_path', examplePath.value)
    } else {
      throw new Error('No image selected')
    }

    const res = await axios.post('/api/flower', formData)
    result.value = `${res.data.label} (${res.data.confidence})`
  } catch (err) {
    error.value = 'Error during prediction.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.tool-title {
  font-size: 1.4rem;
  margin-bottom: 16px;
  color: rgb(0, 0, 0);
  font-family: var(--font-heading, 'Playfair Display', serif);
}
.predict-tool {
  text-align: center;
  padding: 24px;
}
img {
  margin-top: 12px;
  border-radius: 8px;
  box-shadow: 0 0 8px rgba(0,0,0,0.2);
}
.send-buttons{
  display: flex;
  flex-wrap: wrap;
  gap: 28px;
  justify-content: center;
  margin-top: 35px;
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
.error {
  color: red;
  font-weight: bold;
}
</style>
