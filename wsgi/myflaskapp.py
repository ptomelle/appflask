from flask import Flask,request, send_from_directory
from flask import render_template
from flask import jsonify
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)

# simula molto bene un database di dizionari con chiave numerica
# i dizionari possono anche essere vuoti alla partenza
registroAlunni = {0:{"numeroReg":0,"nome":"ignoto","cognome":"ignoto","annoNascita":"1900"}}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index.html")
def hello1():
    return send_from_directory('.', 'index.html')

@app.route("/js/<nomeFileJs>")
def jsLoad(nomeFileJs):
    return send_from_directory('js', nomeFileJs)

@app.route("/css/<nomeFileCss>")
def cssLoad(nomeFileCss):
    return send_from_directory('css', nomeFileCss)
   
@app.route("/insertAlunno/" , methods=["GET"])  # metodo GET per chiamare dalla barra del browser
def inserisciAlunno ():
    # spedizione in formato GET ? .. & ... &
    numeroReg =  request.args.get('numeroReg')
    nome =       request.args.get('nome')
    cognome =    request.args.get('cognome')
    annoNascita =request.args.get('annoNascita') 
    dizAlunno = { "numeroReg": numeroReg, "nome": nome,
                  "cognome" : cognome , "annoNascita":annoNascita}
    registroAlunni[int(numeroReg)]= dizAlunno
    
    #print dizAlunno
    #print registroAlunni
    
    return ""   #restituisce status = 200  OK , ma nessuna stringa

@app.route("/insertAlunnoPOST/" , methods=["POST"])  # metodo POST diverso dal GET
def inserisciAlunnPOST():
    # spedizione in formato JSON ,   request.json e' il dizionario mandato
    numeroReg =  request.json['numeroReg']
    nome =       request.json['nome']
    cognome =    request.json['cognome']
    annoNascita =request.json['annoNascita' ]
    dizAlunno = { "numeroReg": numeroReg, "nome"        : nome,
                  "cognome" : cognome  , "annoNascita" :annoNascita}
    registroAlunni[int(numeroReg)]= dizAlunno
    return ""   #restituisce status = 200  OK , ma nessuna stringa
    
    
@app.route("/alunnoByNumeroReg/", methods=["POST"]) # metodo POST
def alunnoByNumeroReg():
    # spedizione in formato POST usando un oggetto JSON
    
    numeroReg =  request.json['numeroReg']
    
    dizAlunno = registroAlunni[int(numeroReg)]
    
    #print dizAlunno
    
    # in casi piu' complessi usare render_templates e quindi jsonify
    stringJson = jsonify( ** dizAlunno)   #aggiunge content-type => json
    
    #print stringJson
    
    return stringJson
    
if __name__ == "__main__":
    #app.debug=True
    app.run(port=4003)
