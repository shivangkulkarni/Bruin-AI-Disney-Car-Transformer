import requests
from groq import Groq
import os

def generate_image_from_description(initial_description):
    # Step 1: Fine-tune the description using the Groq API (Mock Example)
    # groq_api_url = "https://api.groq.com/your-endpoint"
    # groq_headers = {
    #     'api-key': 'your-groq-api-key',
    #     'Content-Type': 'application/json'
    # }

    # groq_payload = {
    #     "description": initial_description,
    #     "fine_tune_params": {
    #         # You can define any specific fine-tuning parameters Groq provides.
    #     }
    # }

    # # Send the description to Groq
    # groq_response = requests.post(groq_api_url, json=groq_payload, headers=groq_headers)

    # # Check if the request was successful


    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "Here is a description of a person: " + initial_description + ". Please transform this into a short and simple one-paragraph description of the person as a car character in the Disney Cars universe. Focus on key physical and personality traits. Describe how these traits translate into their appearance as a car (e.g., paint color, headlights, body shape). Ensure the description is concise and avoids excessive detail.",
            }
        ],
        model="llama3-8b-8192",
    )    


    # if chat_completion.status_code != 200:
    #     print(f"Error with Groq API: {chat_completion.status_code}")
    #     return None
    # Assuming Groq returns the fine-tuned description
    fine_tuned_description = chat_completion.choices[0].message.content
    fine_tuned_description = 'can you make a car cartoon from the Disney Cars movie that fits this description (the image should be a car only, no human):' + fine_tuned_description
    if not fine_tuned_description:
        print("No fine-tuned description returned by Groq")
        return None

    print(f"Fine-tuned Description: {fine_tuned_description}")

    # Step 2: Send the fine-tuned description to DeepAI API for image generation
    deepai_url = "https://api.deepai.org/api/text2img"
    deepai_headers = {
        'api-key': '51d2a415-2c8b-4261-abce-b5b6fe3fa666'
    }

    deepai_payload = {
        'text': fine_tuned_description,
        'image_generator_version': 'hd',
        'style': '3D Cartoon Character Generator',
    }

    deepai_response = requests.post(deepai_url, data=deepai_payload, headers=deepai_headers)

    # Check if the request was successful
    if deepai_response.status_code != 200:
        print(f"Error with DeepAI API: {deepai_response.status_code}")
        return None

    # Get the image URL from DeepAI's response
    image_url = deepai_response.json().get("output_url")
    if not image_url:
        print("No image URL returned by DeepAI")
        return None

    print(f"Generated Image URL: {image_url}")

    # # Optional: Download the image and save it
    # image_data = requests.get(image_url).content
    # with open('generated_image.png', 'wb') as handler:
    #     handler.write(image_data)

    # print("Image saved as 'generated_image.png'")
    return image_url



