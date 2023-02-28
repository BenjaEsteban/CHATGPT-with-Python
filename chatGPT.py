import openai
import config

openai.api_key = config.secretKey

while True:

    pregunta = input('\nIntroduce una pregunta: ')
    
    if pregunta == "exit":
        break

    completion = openai.Completion.create(engine='text-davinci-003', #text-davinci es el modelo entrenado más actualizado en el día de hoy 
                            prompt=pregunta,
                            max_tokens=2048)

    print(completion.choices[0].text)