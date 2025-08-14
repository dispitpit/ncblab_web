<template>
  <div class="about-container">
    <!-- 頁面標題 -->
    <h2 class="about-title">About</h2>

    <!-- 說明文字 -->
    <p class="about-description">
      Please input your about below.
    </p>

    <!-- <div class="about-card">
      <p><strong>Version:</strong> v1.0.0</p>
      <p><strong>Author:</strong> YourName</p>
      <p><strong>Updated:</strong> July 2025</p>
    </div> -->
  </div>
</template>

<style scoped>
.about-container {
  max-width: 600px;
  margin: 80px auto;
  padding: 40px;
  text-align: center;
  background-color: #f6f8fa;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.about-title {
  font-size: 1.7rem;
  margin-bottom: 16px;
  color: rgb(98, 121, 197);
  font-family: var(--font-heading, 'Playfair Display', serif);
}

.about-description {
  font-size: 1rem;
  color: #555;
  margin-bottom: 24px;
  font-family: var(--font-body, 'Inter', sans-serif);
}

/* .about-card {
  text-align: left;
  background-color: #fff;
  border: 1px dashed #ccc;
  border-radius: 6px;
  padding: 16px;
  font-family: var(--font-body, 'Inter', sans-serif);
  color: #333;
  line-height: 1.6;
} */
</style>
