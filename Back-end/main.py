# Temporary main until I move everything
from flask import Flask, render_template, request,jsonify

app= Flask(__name__)

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
    user_message = request.json.get('message')

    #Etape 1 : stocker le message de l'utilisateur
    knowledge_base.append(user_message)
    print(f"{user_message}")

    #Etape 2 : Réponse du bot
    #Pour l'instant il répond de manière très simple : 
    chatbot_response = "INtéressant. Peux-tu développer ce point ?"

    #Etape 3 : Renvoyer la réponse en format JSON
    return jsonify({"response" : chatbot_response})

if __name__ == '__main__':
    app.run(debug = True)