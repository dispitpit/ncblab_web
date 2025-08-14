<!-- App.vue包含內容: -->
<!-- 各頁連接點、主樣式、整合頁首頁尾、切換動畫-->
<script setup>
// 匯入Vue內建功能
import { ref, onMounted } from 'vue'
// 引入各子程式
/* 引入方法: 
  import <自訂名稱自訂> form '<程式路徑>'
*/

// PAGE:
import HomeView from './components/HomeView.vue'
import AboutView from './components/AboutView.vue'
import ContactView from './components/ContactView.vue'
import Datasets from './components/Datasets.vue'
import Help from './components/Help.vue'
// HEADER、FOOTER:
import PageHeader from './components/PageHeader.vue'
import PageFooter from './components/PageFooter.vue'


//內容動畫
const contentVisible = ref(false)
onMounted(() => {
  // 導覽列延後0.5秒出現
  setTimeout(() => {
    buttonsVisible.value = true     // 按鈕先出現
  }, 500)
  // 內容延後1秒後出現
  setTimeout(() => {
    contentVisible.value = true     // 最後內容出現
  }, 1000)
})


//頁首頁尾動畫
const footerVisible = ref(false)
onMounted(() => {
  setTimeout(() => {
    footerVisible.value = true
  }, 500)  // 延遲淡入
})


// 按鈕動畫
const buttonsVisible = ref(false)
onMounted(() => {
  setTimeout(() => {
    buttonsVisible.value = true
  }, 500)  // 慢一點出現
})

// 頁面切換設定
const currentPage = ref('home') // 預設首頁位置
function goTo(page) {
  // 切換對應的元件設定
  currentPage.value = page
}
</script>

<template>
  <div class="page-wrapper">
    <!-- 頁首 -->
    <Transition name="fade-up">
      <PageHeader v-if="footerVisible" @navigate="goTo"/>
    </Transition>
    
    <!-- 導覽列 -->
    <transition name="fade-slow">
      <nav class="nav-bar" v-if="buttonsVisible">
        <!-- 每個按鈕綁定goTo()來切換頁面，根據currentPage加上active樣式-->
        <button @click="goTo('home')" :class="{ active: currentPage === 'home' }">Home</button>
        <button @click="goTo('about')" :class="{ active: currentPage === 'about' }">About</button>
        <button @click="goTo('contact')" :class="{ active: currentPage === 'contact' }">Contact</button>
        <button @click="goTo('datasets')" :class="{ active: currentPage === 'datasets' }">Datasets</button>
        <button @click="goTo('help')" :class="{ active: currentPage === 'help'}">Help</button>
      </nav>
    </transition>

    <!-- 主頁面區域 -->
    <main class="main-content">
      <transition name="fade-content">
        <!-- 根據 currentPage 動態渲染對應的元件 -->
        <component
          v-if="contentVisible"
          :is="{
            home: HomeView,
            about: AboutView,
            contact: ContactView,
            datasets: Datasets,
            help: Help
          }[currentPage]"
        />
      </transition>
    </main>

    <!-- 頁尾: 加入動畫 -->
    <Transition name="fade-up">
      <PageFooter v-if="footerVisible" />
    </Transition>
  </div>
</template>

<style scoped>
/* 當前頁面 */
.page-wrapper {
  background-color: #ffffff; /*主背景*/
  min-height: 100vh; /* 確保內容填滿螢幕 */
  display: flex; 
  flex-direction: column; /* 垂直排列 */
}

.main-content {
  flex: 1; /* 中央內容區自動撐開剩餘高度，footer 貼底用 */
  padding: 24px;
}

/* 內容動畫 */
.fade-content-enter-active {
  transition: opacity 0.5s ease, transform 1.5s ease;
}
.fade-content-enter-from {
  opacity: 0;
  transform: translateY(20px);
}
/* 按鈕動畫 */
.fade-slow-enter-active {
  transition: opacity 0.5s ease, transform 1.5s ease;
}
.fade-slow-enter-from {
  opacity: 0;
  transform: translateY(8px);
}
/* 頁首頁尾動畫 */
.fade-up-enter-active {
  transition: all 1.5s ease;
}
.fade-up-enter-from {
  opacity: 0;
  transform: translateY(20px);
}

/* 按鈕 */
nav.nav-bar {
  display: flex; /* 按鈕水平排列 */
  justify-content: center; /* 水平置中 */
  gap: 16px; /* 按鈕之間的間距 */
  border-bottom: 1px solid #ccc; /* 下邊框分隔線 */
  padding: 8px 0; /* 上下內距 */
  background-color: rgb(207, 187, 237); /* 背景色 */
}

nav.nav-bar button {
  position: relative; /* 為了讓 ::after 定位於 button 底部 */
  background-color: transparent; /* 透明背景 */
  border: none; /* 無邊框 */
  color: #ffffff; /* 白字 */
  padding: 6px 14px;  /* 內距 */
  border-radius: 4px;  /* 圓角 */
  cursor: pointer; /* 滑鼠游標變為手指 */
  font-weight: 650;  /* 粗體字重 */
  transition: background 0.1s; /* 背景快速過渡 */
  font-size: 20px;
  font-family: 'Noto Sans TC', sans-serif; 
  font-variant: small-caps;  /* 小型大寫字母效果 */
  letter-spacing: 0.11em;  /* 字距 */
  overflow: hidden; /* 確保底線動畫不會溢出 */
}

nav.nav-bar button::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0%;
  height: 3px;
  background-color:rgb(87, 123, 190);
  transition: width 0.4s ease-in-out;
}

nav.nav-bar button:hover::after {
  width: 100%;
}

nav.nav-bar button.active::after {
  width: 100%;
}

</style>
