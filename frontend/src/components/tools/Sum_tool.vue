<template>
  <div class="sum-tool">
    <h3 class="tool-title">Add Three number</h3>
    <p>Please enter the numbers：</p>

    <input v-model.number="a" type="number" placeholder="a" />
    <input v-model.number="b" type="number" placeholder="b" />
    <input v-model.number="c" type="number" placeholder="c" />

    <div class="send-buttons">
      <button @click="calc">Send</button>  
    </div>
    

    <p v-if="result !== null">Sum of number：{{ result }}</p>
    <p v-if="error">{{ error }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const a = ref(0)
const b = ref(0)
const c = ref(0)
const result = ref(null)
const error = ref('')

async function calc() {
  result.value = null
  error.value = ''
  try {
    const res = await axios.post('/api/sum', { a: a.value, b: b.value, c: c.value })
    result.value = res.data.sum
  } catch (err) {
    error.value = '無法取得結果，請確認後端是否啟動'
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
.sum-tool {
  padding: 20px;
  text-align: center;
  /* border-radius: 10px; */
}
input {
  width: 60px;
  margin: 0 6px;
  padding: 5px;


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
</style>
