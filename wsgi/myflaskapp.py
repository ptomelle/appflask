from flask import Flask,request, send_from_directory

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

@app.route("/elaboraReq1")
def  elaboraReq1():
	#  variabile var1, non la stringa 'var1'
	var1 = request.args.get('var1')
	#  variabile var2, non la stringa 'var2'
	var2 = request.args.get('var2')

        stringHtml= '<html><body>' + \
            '<H3>' +request.query_string +'</H3><br/>' +\
            '<H3>' + 'valore dei parametri ' +\
           'var1=' + var1 +\
              ' '+\
            'var2=' + var2  +\
	    '</H3></body></html>'
        return stringHtml
    


@app.route("/elaboraInput")
@app.route("/static/elaboraInput")
def elaboraInput():
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
    
     


if __name__ == "__main__":
    app.run()
