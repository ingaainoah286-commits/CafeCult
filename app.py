from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Historie:Elevhefte flask kurs fra uke..."

if __name__=="__main__":
    app.run(debug=True)



@app.route("/bestilling", methods=["GET", "POST"])
def bestilling ():
    produkter =["Merch","Order"]
    
    if request.method == "POST":

        navn = request.form["navn"]
        produkt= request.form["produkt"]
        storrelse= request.form["storrelse"]
        antall= request.form["antall"]
        kommentar= request.form.get("kommentar", "")
        
        return render_template(

            "bekreftelse.html",
            navn=navn,
            produkt=produkt,
            storrelse=storrelse,
            antall=antall,
            kommentar=kommentar   
        )

    return render_template(

        "bestilling.html",
        produkter=produkter

    )

if __name__=="__main__":
    app.run(debug=True)

@app.route("/GramPost", methods=[""])
def GramPost ():

    if request.method == "POST":


        return render_template(



        )

    return render_template(


    )

@app.route("/login", methods=[""])
def login ():


    if request.method == "POST":


        return render_template(

            kurs = request.form["kurs"]

            kursliste = ["Python","Flask";"Javascript","Linux"]

            nivaa = request.form["nivaa"]



        )

    return render_template(


    )

@app.route("/registreringsside", methods=[""])
def registrerinsside ():

    if request.method == "POST":


        return render_template(



        )

    return render_template(


    )

@app.route("/SipShop", methods=[""])
def SipShop ():

    #GET og POST fra flask arbeider ved å...

    if request.method == "POST":


        return render_template(



        )   

    return render_template(


    )

    if __name__=="__main__":
        app.run(debug=True)


#Bilder i Flask (20), fra Elevhefte Flask Kurs VG2, dato 2026-10-7, Uke 41-42.


