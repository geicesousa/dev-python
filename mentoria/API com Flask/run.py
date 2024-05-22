# -*- coding: utf-8 -*-

from flask import Flask, render_template, jsonify, request
from app import cardapio

app = Flask(__name__)


@app.route("/cardapio")
def hello():
    return jsonify(cardapio)

@app.route("/<nome>")
def index(nome):
    return jsonify(cardapio.get('pizzas').get(nome))


@app.route("/html/<nome>")
def html_page(nome):
    return render_template("html_page.html", nome=nome)

@app.route("/html/dog")
def html_dog():
    import requests

    nome = request.args.get('nome')

    # API utilizada é a TheDogApi - https://docs.thedogapi.com/
    dogImage = requests.get('https://api.thedogapi.com/v1/images/search')
    url = dogImage.json()[0].get('url')
    
    return render_template("html_page.html", nome=nome, image=url)

@app.route("/jsonify")
def json_api_jsonify():
    pessoas = [{"nome": "Ana", "idade": 35},
               {"nome": "Claudia", "idade": 26},
               {"nome": "Priscila", "idade": 42},
               {"nome": "Carine", "idade": 22}]

    return jsonify(pessoas=pessoas, total=len(pessoas))

@app.route("/topvereadores2020/")
def get_top_votos_candidatos():
    cargo = request.args.get('cargo', 'Vereador')
    indice = request.args.get('indice', 3)

    votacoes = get_top_votos(cargo, indice)

    return jsonify(votacoes.to_dict(orient ='records'))

def get_top_votos(cargo, indice):
    import pandas as pd

    dados = pd.read_csv('dados/dados.csv', usecols ='''NM_URNA_CANDIDATO SG_PARTIDO 
        TOTAL_VOTOS NM_MUNICIPIO DS_CARGO'''.split(), sep=",")
    dados = dados.loc[dados['DS_CARGO'] == cargo][['NM_URNA_CANDIDATO', 'SG_PARTIDO', 'TOTAL_VOTOS']]
    dados = dados.sort_values('TOTAL_VOTOS', ascending=False).head(indice)

    return dados

app.run(debug=True, use_reloader=True)

if __name__ == "__main__":
    app.run()