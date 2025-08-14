<!-- PageHeader.vue-->
<script setup>
// logo 連接到首頁
const emit = defineEmits(['navigate'])
function goToHome() {
  emit('navigate', 'home')
}
</script>

<template>
  <header class="header" @click="goToHome">
    <!-- 網站左上角logo -->
    <img src="/mark.ico" class="logo" alt="Logo" />

    <div class="title-wrapper">
      <!-- 小標題 -->
      <div class="subtitle"> - NCBLAB  WEB  TEMPLATE -</div>
      <!-- 大標題 -->
      <h1 class="title"> Research Name </h1>
    </div>
  </header>
</template>

<style scoped>
/* logo變淡 */
.logo:hover{
  opacity: 0.75;
}

.header {
  display: flex;
  align-items: center;
  justify-content: center;
  /* background-color: var(--color-bg-deep); */
  background: #2A7B9B;
  /* background: linear-gradient(180deg,rgba(42, 123, 155, 1) 0%, rgba(87, 141, 199, 1) 35%, rgba(247, 188, 229, 1) 72%, rgba(245, 216, 206, 1) 100%); */
  /* background: linear-gradient(180deg,rgba(5, 51, 79, 1) 0%, rgba(94, 157, 230, 1) 69%); */
  background: linear-gradient(180deg,rgba(5, 51, 79, 1) 0%, rgba(94, 157, 230, 1) 69%, rgba(207, 187, 237, 1) 100%);
  color: rgb(255, 255, 255);
  padding: 16px 24px;
  gap: 16px;
  padding: 20px;
  cursor: pointer;
}

/* 左上角logo */
.logo {
  width: 75px;
  height: 75px;
}

.title-wrapper {
  text-align: center;
}

.subtitle {
  font-size: 10px;
  color: #ffffff;
  /* font-style: italic; */
  font-family: "Andale Mono", 'monospace'; /* 小標題字體 */
  letter-spacing: 0.55em;
}

.title {
  /* font-size: 40px;
  font-weight: bold;
  margin: 0;
  color: rgb(255, 255, 255);
  font-family: "Andale Mono", 'monospace';  /*大標題字體*/
  letter-spacing: 0.03em;
} 
</style>
