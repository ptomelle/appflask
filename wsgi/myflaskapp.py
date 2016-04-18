from flask import Flask,request, send_from_directory
from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"

@app.route("/index.html")
def hello1():
    return send_from_directory('.', 'index.html')

@app.route("/index1.html")
def hello2():
    return send_from_directory('/static/', 'index1.html')

@app.route("/elaboraInputHtml")
def elaboraInputHtml():
     #  variabile var1, non la stringa 'var1'
	var1 = request.args.get('firstname')
	#  variabile var2, non la stringa 'var2'
	var2 = request.args.get('lastname')

        stringHtml= '<html><body>' + \
            '<H3>' +request.query_string +'</H3><br/>' +\
            '<H3>' + 'valore dei parametri ' +\
           'firstname=' + var1 +\
              ' '+\
            'lastname=' + var2  +\
	    '</H3></body></html>'
        return stringHtml
    
@app.route("/elaboraInputJson")
def elaboraInputJson():
    # recupera i valori spediti dalla queryString
    var1 = request.args.get('firstname')
	#  variabile var2, non la stringa 'var2'
    var2 = request.args.get('lastname')
    
    stringJSON = ' { "firstName" :  ' +\
                  '"' +    var1 +  '"'+\
                 '   "lastName"  :  ' +\
                  '"' +    var2 +  '"'+\
                 '}'
                 
    return stringJSON
   
@app.route("/elaboraInputJson_1")
def elaboraInputJsontml():
    # recupera i valori spediti dalla queryString
    var1 = request.args.get('firstname')
	#  variabile var2, non la stringa 'var2'
    var2 = request.args.get('lastname')
    
    dizVar = {"firstname": var1, "lastname":var2}
    
    return render_template('elaboraInputJson.json.tml', name = dizVar)
    
   
    
    
   

if __name__ == "__main__":
    app.debug=True
    app.run(port=7000)
