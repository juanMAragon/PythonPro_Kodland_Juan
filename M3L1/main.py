from flask import Flask
import random

app = Flask(__name__)


lista_fatti = ["Secondo uno studio del 2019, oltre il 60% delle persone risponde ai messaggi di lavoro sul proprio smartphone entro 15 minuti dall'uscita dal lavoro",
               "Il social network hanno aspetti positivi e negativi e dobbiamo essere consapevoli di entrambi quando usiamo queste piattaforme.",
               "Un modo per combattere la dipendenza tecnologica è cercare attività che portino piacere e migliorino l'umore"]


@app.route("/")
def ciao_mondo():
    return """
             <h1>Ciao, Mondo!</h1>
             <a href="/random_fact">Visualizza un fatto casuale!</a>
            """
    # testo = "ciao mondo"    
    # return f'<h1> {testo} </h1>'

@app.route("/random_fact")
def myRandomFact():
    return f"""
            <p>{random.choice(lista_fatti)}</p>
            <a href="/">torna alla home!</a>
            """

app.run(debug=True)