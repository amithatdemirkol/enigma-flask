from flask import Flask, render_template, request
from enigma.enigma_machine import EnigmaMachine

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        message = request.form['message']
        rotor_positions = [int(request.form['rotor1']), int(request.form['rotor2']), int(request.form['rotor3'])]
        
        # Enigma machine setup
        machine = EnigmaMachine(rotor_positions)
        encrypted_message = machine.encrypt_message(message.upper())

        return render_template('result.html', message=message, encrypted_message=encrypted_message)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
