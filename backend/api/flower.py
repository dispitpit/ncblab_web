# backend/api/flower.py
from flask import Blueprint, request, jsonify, send_from_directory
import torch
import torch.nn as nn
from torchvision import models, transforms
from PIL import Image
import os, traceback
import random

flower_bp = Blueprint('flower_bp', __name__)

# === 定位資料夾 ===
BASE_DIR = os.path.dirname(__file__)
FLOWER_DIR = os.path.abspath(os.path.join(BASE_DIR, '..', 'flower_model'))
MODEL_PATH = os.path.join(FLOWER_DIR, 'flower_model.pth')
TMP_PATH = os.path.join(FLOWER_DIR, 'temp_upload.jpg')
# EXAMPLE_DIR = os.path.join(FLOWER_DIR, 'flower_images')

# === 類別與模型 ===
class_names = ['daisy', 'dandelion', 'rose', 'sunflower', 'tulip']
model = models.resnet18(pretrained=False)
model.fc = nn.Linear(model.fc.in_features, len(class_names))
model.load_state_dict(torch.load(MODEL_PATH, map_location='cpu'))
model.eval()

transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406],
                         [0.229, 0.224, 0.225])
])

def predict_image(path):
    img = Image.open(path).convert('RGB')
    x = transform(img).unsqueeze(0)
    with torch.no_grad():
        prob = torch.softmax(model(x), 1)[0]
    idx = int(torch.argmax(prob))
    return class_names[idx], round(prob[idx].item(), 4)


# === API 路由 ===
# @flower_bp.route('/api/flower/example', methods=['GET'])
# def random_example_image():
#     try:
#         image_files = [f for f in os.listdir(EXAMPLE_DIR)
#                        if f.lower().endswith(('.jpg'))]
#         if not image_files:
#             return jsonify({'error': 'No images found'}), 404

#         random_file = random.choice(image_files)
#         return jsonify({'filename': random_file})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500
    
@flower_bp.route('/api/flower', methods=['POST'])
def flower_api():
    try:
        if 'file' in request.files and request.files['file'].filename:
            request.files['file'].save(TMP_PATH)
            img_path = TMP_PATH
        elif 'example_path' in request.form:
            fn = os.path.basename(request.form['example_path'])
            img_path = os.path.join(EXAMPLE_DIR, fn)
        else:
            return jsonify({'error': 'No image provided'}), 400

        label, conf = predict_image(img_path)
        return jsonify({'label': label, 'confidence': conf})

    except Exception as e:
        traceback.print_exc()
        return jsonify({'error': str(e)}), 500

# === 範例圖靜態提供 ===
@flower_bp.route('/flower_model/flower_images/<path:filename>')
def serve_flower_image(filename):
    return send_from_directory(EXAMPLE_DIR, filename)
