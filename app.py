import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from PIL import Image
import openai
from generate import generate_custom_description, generate_disney_car_image

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads/'

# Ensure OpenAI key is set
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_disney_car_from_image(image_path):
    # Step 1: Generate text description using BLIP (example function from above)
    description = generate_custom_description(image_path)
    
    # Step 2: Generate Disney Cars-style image using DALL-E 3
    disney_car_image_url = generate_disney_car_image(description)
    
    return disney_car_image_url

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            
            # Generate Disney car image URL
            disney_car_image_url = generate_disney_car_from_image(filepath)
            
            # Pass the URL to the template
            return render_template('index.html', uploaded_image=filepath, disney_car_image_url=disney_car_image_url)
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
