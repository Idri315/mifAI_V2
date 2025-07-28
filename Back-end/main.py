# Temporary main until I move everything
from flask import Flask, render_template, request,jsonify
import random

app= Flask(__name__)

#Jauges
jauge_confiance = 50
jauge_affection = 50


#Database pour stocker ce que le robot à appris
knowledge_base = []

#Route vers l'interface du chatbot
@app.route('/')
def home():
    #fichier HTML chaterface
    return "Bienvenue sur mifAI !  Quelle est la première chose que tu aimerais apprendre à Fai ?"

#Route pour communiquer avec Fai
@app.route('/send_message', methods=['POST'])
def send_message():
    global jauge_confiance, jauge_affection

    user_message = request.json.get('message')
    print(f"{user_message}")

    longueur_message = len(user_message)

    #à changer après
    if longueur_message > 50:
        jauge_affection+= random.randint(1, 5) #Augmentation aléatoire de l'affection
        jauge_confiance += random.randint(1, 3) # Augmentation aléatoire de la confiance
    else : 
        jauge_confiance -= random.randint(1, 3) # Baisse si l'explication est trop courte

    jauge_confiance= max(0, min(100, jauge_confiance))
    jauge_affection = max(0, min(100, jauge_affection))

    print(f"Confiance : {jauge_confiance}, Affection : {jauge_affection}")

    chatbot_response = "Intéressant. Peux tu développer ce point ?"

    return jsonify({"response" : chatbot_response, "confiance" : jauge_confiance, "affection" : jauge_confiance})


if __name__ == '__main__':
    app.run(debug = True)