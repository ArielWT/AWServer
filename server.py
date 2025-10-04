from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola! Tu servidor Flask AWServer funciona"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    print("Recibido en servidor:", data)
    return jsonify({"respuesta": f"Recibido correctamente: {data}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



#1 paso para activar entorno virtual (venv) venv\Scripts\activate
#para subir cosas a git
#git add requirements.txt
#git commit -m "Agregar Gunicorn a requirements.txt"
#git remote add origin https://github.com/ArielWT/AWServer.git
#(agrega todos los archivos) git add .
#git push origin main

#Def app para flask
#2 $env:FLASK_APP="server.py"
#2 $env:FLASK_ENV="development"
#3 ejecutar:
# python -m flask run

