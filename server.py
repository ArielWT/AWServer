import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "¡Hola! Tu servidor Flask AWServer funciona"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)


#paso para activar entorno virtual (venv) venv\Scripts\activate
#para subir cosas a git
#git add requirements.txt
#git commit -m "Agregar Gunicorn a requirements.txt"
#git push origin main
