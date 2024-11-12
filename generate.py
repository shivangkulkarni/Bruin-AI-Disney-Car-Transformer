from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import base64
import requests
from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def encode_image(image_path):
  with open(image_path, "rb") as image_file:
    return base64.b64encode(image_file.read()).decode('utf-8')

def generate_custom_description(image):
    base64_image = encode_image(image)

    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this person as a Disney Cars-style character, focusing on how their physical appearance, personality, and unique qualities would translate into a customized car. Imagine details such as their body shape and color, which should reflect their personality and presence. Describe the car's grill (like a mouth), headlights (like eyes), and any specific design features or accessories that capture their individuality and essence. Consider symbols or custom decals that represent their passions or achievements, and explain how the car would perform or move in ways that reflect their strengths and style."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}",
                        }
                    },
                ],
            }
        ],
    )

    fine_tuned_description = chat_completion.choices[0].message.content

    deep_ai_fine_tuned_description = "can you make a car cartoon from the Disney Cars movie that fits this description (the image should be a car only, no human): " + fine_tuned_description

    fine_tuned_description = "Generate an image of a 3D cartoon car in a lively, vibrant animated style, with colors and design inspired by classic animated movies featuring expressive vehicle characters inspired by this description: " + fine_tuned_description

    print(deep_ai_fine_tuned_description)
  
    return deep_ai_fine_tuned_description

    # image = Image.open(image_path).convert("RGB")
    # inputs = processor(images=image, prompt=custom_prompt, return_tensors="pt")
    # description_ids = model.generate(
    #     **inputs,
    #     max_length=40,  
    #     min_length=25,  
    #     num_beams=3,  # Use beam search for better quality
    #     repetition_penalty=1.1,  # Avoid repetitive outputs
    #     length_penalty=2.0,  # Encourage longer sequences
    #     top_p=0  # Use nucleus sampling for diversity in output
    # )
    # description = processor.decode(description_ids[0], skip_special_tokens=True)
    # print(description)
    # return description

def generate_disney_car_image(prompt):
        
    deepai_url = "https://api.deepai.org/api/text2img"
    deepai_headers = {
        'api-key': os.environ.get("DEEPAI_API_KEY")
    }

    deepai_payload = {
        'text': prompt,
        'image_generator_version': 'hd',
        'style': '3D Cartoon Character Generator',
        'preference': 'quality',
    }

    deepai_response = requests.post(deepai_url, data=deepai_payload, headers=deepai_headers)
    disney_car_image_url = deepai_response.json().get("output_url")

    print(f"Generated Image URL: {disney_car_image_url}")

    # client = OpenAI(
    #     api_key=os.environ.get("OPENAI_API_KEY"),
    # )

    # response = client.images.generate(
    #     model="dall-e-3",
    #     prompt="give my prompt to DALL-E verbatim:" + prompt,
    #     n=1,
    #     size="1024x1024",
    # )

    # print(response)

    # disney_car_image_url = response.data[0].url
    return disney_car_image_url



