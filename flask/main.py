from flask import Flask, render_template, request
from io import BytesIO
import requests, base64

API_URL = "https://api-inference.huggingface.co/models/taroii/pothole-detection-model"
headers = {"Authorization": "INSERT_CODE_HERE"}

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
      second_message = 'Probability of Pothole: ' + str(round(result[0]['score'], 2)) 
    else:
      prediction_msg = 'No pothole detected.'
      second_message = 'Probability of Pothole: ' + str(round(result[1]['score'], 2))
  except:
    prediction_msg = 'Sorry! The model is still loading...'
    second_message = 'Please wait ' + str(result['estimated_time']) + ' seconds :)'
    
  img_base64 = base64.b64encode(img_bytes.getvalue()).decode()
  
  return render_template('result.html', prediction=prediction_msg, second_message=second_message, image=img_base64)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81, debug=True)
