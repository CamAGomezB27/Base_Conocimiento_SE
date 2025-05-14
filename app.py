from flask import Flask, request, jsonify
from rules import DiagnosticoMedico, Sintomas

app = Flask(__name__)

@app.route("/diagnostico", methods=["POST"])
def diagnostico():
    data = request.get_json()
    engine = DiagnosticoMedico()
    engine.reset()
    engine.declare(Sintomas(**data))
    engine.run()
    return jsonify({"diagnostico": engine.resultado})

@app.route("/", methods=["GET"])
def home():
    return "Servicio del sistema experto médico funcionando."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)