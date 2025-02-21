from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

def get_texto_descritivo_chatGPT(destino):
    client = OpenAI(api_key=str(os.getenv('OPEN_AI_KEY')))
    texto = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                'role':'user',
                'content':f'Faça uma descrição muito breve de {destino} com exatamente dois parágrafos, '
                          f'enfatizando os pontos positivos do lugar. Máximo de 100 caracteres por parágrafo'
            }
        ],

    )

    return texto.choices[0].message.content