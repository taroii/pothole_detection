from flask import Flask, render_template, request
from io import BytesIO
import requests, base64

API_URL = "https://api-inference.huggingface.co/models/taroii/pothole-detection-model"
headers = {"Authorization": "INSERT-KEY-HERE"}

def query(img):
  response = requests.post(API_URL, headers=headers, data=img)
  return response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
  file = request.files['image']
  img_bytes = file.read()
  img_bytes = BytesIO(img_bytes)
  result = query(img_bytes)
  print(result)
  try:
    if result[0]['label'] == 'pothole':
      prediction_msg = 'Pothole detected!'
      prob_pothole = round(result[0]['score'], 2)
    else:
      prediction_msg = 'No pothole detected.'
      prob_pothole = round(result[1]['score'], 2)
  except:
    prediction_msg = 'No pothole detected.'
    prob_pothole = 'NA'

  img_base64 = base64.b64encode(img_bytes.getvalue()).decode()

  return render_template('result.html', prediction=prediction_msg, prob_pothole=prob_pothole, image=img_base64)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
