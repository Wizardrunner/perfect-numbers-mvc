import csv
from flask import Flask, render_template, request, send_file
from io import StringIO, BytesIO
from threading import Thread
import time

app = Flask(__name__)

# Variables globales
calculation_results = []

def es_primo(num):
    """Verifica si un número es primo."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def formatear_ordinal(numero):
    """Formatea un número como ordinal (1º, 2º, 3º, etc.)."""
    return f"{numero}º"

def calcular_numeros_perfectos(limite):
    """Calcula números perfectos con detalles explicativos y posición ordinal."""
    global calculation_results
    calculation_results = []  # Reiniciar resultados
    numero_ordinal = 1  # Contador para números perfectos

    for p in range(2, limite + 1):
        mersenne = 2**p - 1
        es_primo_mersenne = es_primo(mersenne)
        if es_primo_mersenne:
            numero_perfecto = 2**(p-1) * mersenne
            calculation_results.append({
                "p": p,
                "mersenne": mersenne,
                "es_primo": es_primo_mersenne,
                "numero_perfecto": numero_perfecto,
                "ordinal": formatear_ordinal(numero_ordinal)  # Formateado como ordinal
            })
            numero_ordinal += 1  # Incrementar solo si es un número perfecto
        else:
            calculation_results.append({
                "p": p,
                "mersenne": mersenne,
                "es_primo": es_primo_mersenne,
                "numero_perfecto": "-",
                "ordinal": None  # No hay número perfecto
            })

@app.route("/", methods=["GET", "POST"])
def index():
    mensaje_error = None
    limite = None

    if request.method == "POST":
        if "cancelar" in request.form:  # Botón "Cancelar"
            return render_template("index.html", numeros_perfectos=[], mensaje_error=None, limite=None)

        limite = int(request.form.get("limite", 10))

        # Advertencia para valores altos
        if limite > 60 and "continuar" not in request.form:
            mensaje_error = "El cálculo puede ser lento para valores mayores a 60. ¿Deseas continuar?"
            return render_template("index.html", numeros_perfectos=[], mensaje_error=mensaje_error, limite=limite)

        # Realiza el cálculo
        calcular_numeros_perfectos(limite)

    return render_template(
        "index.html",
        numeros_perfectos=calculation_results,
        mensaje_error=mensaje_error,
        limite=limite
    )

@app.route("/export", methods=["POST"])
def export():
    """Exporta los resultados válidos (sin filas vacías) a un archivo CSV."""
    numeros_perfectos = [
        {
            "p": resultado["p"],
            "ordinal": resultado["ordinal"],
            "numero_perfecto": resultado["numero_perfecto"]
        }
        for resultado in calculation_results
        if resultado["numero_perfecto"] != "-"
    ]

    # Crear archivo CSV en memoria usando StringIO
    output = StringIO()
    writer = csv.writer(output)

    # Encabezados del archivo
    writer.writerow(["Valor de p", "N.º Ordinal", "Número Perfecto"])

    # Filas del archivo
    for item in numeros_perfectos:
        writer.writerow([item["p"], item["ordinal"], item["numero_perfecto"]])

    # Convertir el contenido de StringIO a bytes
    memory_file = BytesIO()
    memory_file.write(output.getvalue().encode('utf-8'))
    memory_file.seek(0)

    # Enviar archivo como descarga
    return send_file(
        memory_file,
        mimetype="text/csv",
        as_attachment=True,
        download_name="numeros_perfectos.csv"
    )

if __name__ == "__main__":
    app.run(debug=True)
