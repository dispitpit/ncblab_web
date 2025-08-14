<!-- HOME PAGE -->
<!-- 這裡可以修改頁首的按鈕名稱、數量-->
<!-- 設計準則：
     1) 「頁首按鈕」= 此頁內的工具切換按鈕
     2) 若新增/刪除工具：需同步做三件事 → (a) 匯入元件import (b) 按鈕設定 (c) 元件區映射
-->
<script setup>
import { ref } from 'vue'

/* ===== 工具元件匯入區 =====
   命名慣例：<功能>Tool；存放於 ./tools/
   注意：路徑大小寫、檔名需與實體檔案一致
*/
import SumTool from './tools/Sum_tool.vue'
import FlowerPredictTool from './tools/FlowerPredict_tool.vue'
import ExcelAnalysisTool from './tools/ExcelAnalysis_tool.vue'

// currentTool變數控制當前顯示哪一頁
const currentTool = ref('')
</script>

<template>
  <div class="home-view">
    <!-- 標題 -->
    <h2 class="tool-title"> Tool Example</h2>

    <!-- 小說明 -->
    <p>Here are three possible interactive interface examples. 
    <br>Change the corresponding files to the front-end and back-end according to your model type.</p>
    <!-- 這裡展示了三種可能會使用到的互動介面範例，依據你的模型型態將對應的檔案進行前後端改動 -->
    <p>The example picture is an example of connecting to the torch model. 
    <br>Models trained by different packages will have different connection API methods. 
    <br>When training the model, try to save the relevant code during training.</p>
    <!-- 範例Picture為連接torch模型範例，不同套件所訓練之模型會有不同串接API方式，訓練模型時盡量保存訓練時相關程式碼 -->
    
    <!-- 按鈕設定 -->
    <div class="tool-buttons">
      <button @click="currentTool = 'sum'">Numeric</button>
      <button @click="currentTool = 'flower'">Pictures</button>
      <button @click="currentTool = 'excel'">Table</button>
    </div>

    <!-- 顯示元件區 -->
    <div class="tool-display">
      <component
        :is="{
          sum: SumTool,
          flower: FlowerPredictTool,
          excel: ExcelAnalysisTool,
        }[currentTool]"
      />
    </div>
  </div>
</template>

<!-- 美編區 -->
<style scoped>

.tool-title {
  font-size: 1.5rem;
  margin-bottom: 16px;
  color: rgb(0, 0, 0);
  font-family: var(--font-heading, 'Playfair Display', serif);
}
.home-view {
  padding: 24px;
  text-align: center;
  /* font-family: var(--font-body, 'Inter', sans-serif) */
  font-size: 1rem;
  color: #555;
  margin-bottom: 24px;
  font-family: var(--font-body, 'Inter', sans-serif);

}
.tool-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 40px;
  justify-content: center;
  margin-bottom: 25px;
}
.tool-buttons button {
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

.tool-buttons button:hover {
  background-color: #d2b3fc;
  /* border-bottom: 5px;
  border-color: black; */
}
.tool-display {
  margin-top: 24px;
}
</style>
