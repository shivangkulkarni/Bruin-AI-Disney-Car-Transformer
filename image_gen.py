import requests
r = requests.post(
    "https://api.deepai.org/api/text2img",
    data={
        'text': 'can you make a car cartoon from the Disney Cars movie that fits this description (the image should be a car only, no human): Meet the charming "Premiere Pete", a sleek sedan with a dark gray and silver paint job, reminiscent of a well-tailored suit. His bright, shining headlights reflect his warm and optimistic personality, while his streamlined body shape exudes confidence and sophistication. As a car character, Premiere Pete embodies the same friendly and approachable traits as the smiling man at the movie premiere, always dressed to impress and ready to roll onto the red carpet.',
        'image_generator_version': 'hd',
        'style': '3D Cartoon Character Generator',
    },
    headers={'api-key': ''}
)
print(r.json())


