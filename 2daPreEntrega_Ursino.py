# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1pFCfDFKeefPKCb6mEWcyYuPhcIu20dRU
"""

pip install openai==0.28

import openai
from IPython.display import display, Markdown

openai.api_key = "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"

def generate_architecture_description(system, prompt):
    system_msg = {"role": "system", "content": system}
    user_msg = {"role": "user", "content": prompt}

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[system_msg, user_msg]
    )

    return response["choices"][0]["message"]["content"]

system_prompt = """
Eres un asistente que ayuda a los arquitectos a generar descripciones detalladas para diseños de casas modernas basadas en los requisitos y preferencias del cliente.
"""

user_prompt = """
Necesito crear una descripción detallada del diseño de una casa moderna de 200 metros cuadrados. El cliente desea un estilo minimalista con grandes ventanales, techos altos y espacios abiertos.
La casa debe tener 3 habitaciones, 2 baños, una cocina abierta y un salón espacioso. Además, el cliente prefiere utilizar materiales sostenibles como madera reciclada y concreto pulido.
Por favor, genera una descripción textual detallada del diseño, incluyendo:
1. Una descripción del exterior de la casa, destacando los grandes ventanales y los materiales sostenibles.
2. Descripciones detalladas de cada habitación, incluyendo la distribución y el mobiliario sugerido.
3. Ideas para la decoración interior que sigan el estilo minimalista.
4. Sugerencias para imágenes que podrían ayudar a visualizar el diseño.
"""

def generate_image(prompt):
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size="512x512"
    )
    image_url = response['data'][0]['url']
    return image_url

detailed_description = generate_architecture_description(system_prompt, user_prompt)

image_prompt = f"Renderizado de una casa moderna de 200 metros cuadrados con un estilo minimalista, grandes ventanales, techos altos, espacios abiertos. Materiales sostenibles como madera reciclada y concreto pulido."
image_url = generate_image(image_prompt)

display(Markdown(f"### Descripción Generada\n\n{detailed_description}"))

display(Markdown("### Imagen Generada"))
display(Image(url=image_url))
