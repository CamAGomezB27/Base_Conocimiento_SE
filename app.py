from flask import Flask, request, jsonify
from rules import DiagnosticoMedico, Sintomas

app = Flask(__name__)

@app.route("/diagnostico", methods=["POST"])
def diagnostico():
    data = request.get_json()

    # Verifica si los datos están presentes y son válidos
    if not data:
        return jsonify({"error": "No data provided"}), 400

    try:
        # Crear un objeto Sintomas con los datos proporcionados
        sintomas = Sintomas(**data)
    except TypeError as e:
        return jsonify({"error": f"Invalid data: {e}"}), 400

    # Inicializar el motor de diagnóstico
    engine = DiagnosticoMedico()
    engine.reset()
    engine.declare(sintomas)
    engine.run()

    # Retornar el resultado del diagnóstico
    return jsonify({"diagnostico": engine.resultado})

@app.route("/", methods=["GET"])
def home():
    return "Servicio del sistema experto médico funcionando."

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
