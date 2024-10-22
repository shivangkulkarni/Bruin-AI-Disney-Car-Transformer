import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from image_gen import generate_image_from_description

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")




image_path = 'image.jpg' # Image path

raw_image = Image.open(image_path).convert('RGB')

# image captioning
inputs = processor(raw_image, return_tensors="pt")

out = model.generate(

    **inputs,
    max_length=40,  
    min_length=25,  
    num_beams=3,  # Use beam search for better quality
    repetition_penalty=1.1,  # Avoid repetitive outputs
    length_penalty=2.0,  # Encourage longer sequences
    top_p=0  # Use nucleus sampling for diversity in output
)
description = processor.decode(out[0], skip_special_tokens=True)

print(description)

print(processor.decode(out[0], skip_special_tokens=True))

print(output)