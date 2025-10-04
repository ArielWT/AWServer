from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta principal
@app.route("/")
def home():
    return "¡Hola! Tu servidor Flask AWServer funciona"

# Ruta para recibir datos de otras apps
@app.route("/api", methods=["POST"])
def api():
    data = request.json  # Espera datos en formato JSON
    if not data:
        return jsonify({"error": "No se recibió JSON"}), 400

    # Ejemplo: procesar datos y responder
    mensaje = data.get("mensaje", "No hay mensaje")
    respuesta = {
        "mensaje_recibido": mensaje,
        "status": "OK"
    }
    return jsonify(respuesta)

# Ruta de prueba GET
@app.route("/status", methods=["GET"])
def status():
    return jsonify({"status": "Servidor activo"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


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

