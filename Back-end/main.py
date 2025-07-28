# Temporary main until I move everything
from flask import Flask, render_template, request,jsonify

app= Flask(__name__)

#Database to stock what the bot learnt
knowledge_base = []

@app.route('/')
def home():
    return "Bienvenue sur mifAI !  Quelle est la première chose que tu aimerais apprendre à Fai ?"



