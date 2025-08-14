<template>
  <div class="dataset-container">
    <h2 class="dataset-title">Datasets</h2>
    <p class="dataset-description">Please input your dataset below.</p>
    <!-- <div class="dataset-placeholder">Enter your dataset name...</div> -->
  </div>
</template>

<style scoped>
.dataset-container {
  max-width: 600px;
  margin: 80px auto;
  padding: 40px;
  text-align: center;
  background-color: #f6f8fa;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

.dataset-title {
  font-size: 1.7rem;
  margin-bottom: 16px;
  color: rgb(98, 121, 197);
  font-family: var(--font-heading, 'Playfair Display', serif);
}

.dataset-description {
  font-size: 1rem;
  color: #555;
  margin-bottom: 24px;
  font-family: var(--font-body, 'Inter', sans-serif);
}

/* .dataset-placeholder {
  width: 100%;
  padding: 12px 16px;
  font-size: 1rem;
  color: #999;
  text-align: left;
  background-color: #fff;
  border: 1px dashed #ccc;
  border-radius: 6px;
  font-family: var(--font-body, 'Inter', sans-serif);
  user-select: none;
  pointer-events: none;
} */
</style>
