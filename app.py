#!/usr/bin/env python3

from flask import Flask, render_template, request, session, redirect, url_for
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_choice = request.form.get('choice')
        computer_choice = random.choice(['rock', 'paper', 'scissors'])
        
        winner = determine_winner(user_choice, computer_choice)
        
        return render_template('result.html', user_choice=user_choice, computer_choice=computer_choice, winner=winner)
    
    return render_template('index.html')

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return 'It\'s a tie!'
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        return 'You win!'
    else:
        return 'Computer wins!'

if __name__ == '__main__':
    app.run(debug=True)
