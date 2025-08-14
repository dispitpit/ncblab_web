<!--PageFooter.vue-->
<template>
  <footer class="footer">
    <!-- LAB資訊 -->
    <p>
      <a href="http://predictor.nchu.edu.tw/ncblab/index.html">Natural Computing & Bioinformatics Laboratory (NCB Lab.)</a>
      , Institute of Genomics and Bioinformatics, National Chung Hsing University, Taiwan.
    </p>  
    <!-- 你的聯絡Mmail-->
    <p>
      For questions and comments, please contact : 
      <a href="mailto:123@nchu.edu.tw">123@nchu.edu.tw</a>
    </p>
    <!-- 最後更新時間-->
    <p>Last update: July. 07, 2025</p>
  </footer>
</template>

<style scoped>
.footer {
  /* background-color: var(--color-bg-deep);  */
  background: linear-gradient(0deg,rgba(5, 51, 79, 1) 0%, rgba(94, 157, 230, 1) 69%, rgba(207, 187, 237, 1) 100%);
  /* background: linear-gradient(0deg,rgba(42, 123, 155, 1) 0%, rgba(87, 141, 199, 1) 35%, rgba(247, 188, 229, 1) 72%, rgba(245, 216, 206, 1) 100%); */
  padding: 8px;
  text-align: center;
  font-size: 12px;
  line-height: 1.2;
  color: rgb(255, 255, 255);
}



.footer a {
  color: inherit;              /* 繼承父元素的字體顏色（例如白色） */
  text-decoration: none;       /* 移除底線 */
}

.footer a:hover {
  text-decoration: underline;  /* 滑鼠移上去時再顯示底線（可選） */
  color: #f0dc84;              /* 滑過時變成亮黃色（可換） */
}

</style>
