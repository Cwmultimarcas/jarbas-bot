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
    import os
port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
ajuste de porta para produção no Render
