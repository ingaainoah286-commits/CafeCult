from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Historie:Elevhefte flask kurs fra uke..."

if __name__=="__main__":
    app.run(debug=True)



@app.route("/bestilling", methods=["GET", "POST"])

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

if request.method == "POST":


    return render_template(



    )

return render_template(


)

@app.route("/login", methods=[""])

if request.method == "POST":


    return render_template(



    )

return render_template(


)

@app.route("/registreringsside", methods=[""])

if request.method == "POST":


    return render_template(



    )

return render_template(


)

@app.route("/SipShop", methods=[""])

if request.method == "POST":


    return render_template(



    )

return render_template(


)

if __name__=="__main__":
    app.run(debug=True)

