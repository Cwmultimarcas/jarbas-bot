from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Jarbas está online!", 200

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Mensagem recebida:", data)
    return '', 200

if __name__ == '__main__':
    app.run()
