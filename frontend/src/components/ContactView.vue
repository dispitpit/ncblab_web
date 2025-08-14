<template>
  <div class="contact-wrapper">
    <!-- 頁面標題 -->
    <h2 class="tool-title">Contact us</h2>
    <p>If you have any suggestions, questions or willingness to cooperate, please contact us through the form below:</p>

    <!-- 表單區塊 -->
    <div class="form">
      <!-- 姓名欄位 -->
      <label>
        Name
        <textarea v-model="name" type="text" placeholder="Enter your name" />
      </label>

      <!-- Email 欄位 -->
      <label>
        Email
        <textarea v-model="email" type="email" placeholder="Enter your Email (optional)" />
      </label>

      <!-- 留言欄位 -->
      <label>
        Message
        <textarea v-model="message" placeholder="Please enter your question or comment" rows="5" />
      </label>

    <!-- 送出按鈕 -->
    <div class="send-buttons">
      <button @click="sendMessage">Submit</button>
    </div>
      <!-- 成功訊息 -->
      <p v-if="success" class="success">Message has been sent, thank you for contacting us!</p>
      <!-- 錯誤訊息 -->
      <p v-if="error" class="error">{{ error }}</p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// 表單資料綁定
const name = ref('')
const email = ref('')
const message = ref('')

// 狀態訊息
const success = ref(false) // 成功提示
const error = ref('') // 錯誤提示

// 送出表單方法
async function sendMessage() {
  // 重置
  success.value = false
  error.value = ''
  
  // 檢查必填欄位
  if (!message.value.trim()) {
    error.value = 'Please enter message'
    return
  }

  try {
    // 呼叫API
    await axios.post('/api/contact/send', {
      name: name.value,
      email: email.value,
      message: message.value
    })

    // 成功: 顯示訊息並清空欄位
    success.value = true
    name.value = ''
    email.value = ''
    message.value = ''
  } catch (err) {
    // 顯示錯誤訊息
    error.value = '連線失敗或服務器錯誤'
  }
}
</script>

<style scoped>

/* 標題樣式 */
.tool-title {
  font-size: 1.5rem;
  margin-bottom: 16px;
  color: rgb(0, 0, 0);
  font-family: var(--font-heading, 'Playfair Display', serif);
}

.contact-wrapper {
  padding: 40px;
  max-width: 600px;
  margin: auto;
  color: #555;
}

/* 表單樣式 */
.form {
  display: flex;
  flex-direction: column;
  gap: 16px;
  margin-top: 20px;
  font-size: 16px;
  color: rgb(0, 0, 0);
  
}

/* 表單輸入區的樣式 */
input,
textarea {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  font-size: 16px;
}

/* 送出按鈕樣式 */
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

/* 滑鼠懸停時按鈕變色設定 */
.send-buttons button:hover {
  background-color: #d2b3fc;
  
}

/* 成功訊息樣式 */
.success {
  color: green;
  font-weight: bold;
}
/* 錯誤訊息樣式 */
.error {
  color: red;
  font-weight: bold;
}
</style>
