from flask import Flask, render_template, request, redirect, url_for, jsonify
from bd.repositorio_leads import obtener_leads

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/leads")
def leads():
    lista_leads = obtener_leads()
    return jsonify(lista_leads)


if __name__ == "__main__":
    app.run(debug=True, port=5005)
