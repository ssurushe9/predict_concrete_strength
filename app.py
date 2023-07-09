from flask import Flask,request,render_template,jsonify
from utils import get_concrete_strength
import config

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/concrete_strength",methods =["GET","POST"])
def strength():
    if request.method == "GET":
        data = request.args.get

        cement              = float(data("cement"))
        blast_furnace_slag  = float(data("blast_furnace_slag"))
        fly_ash             = float(data("fly_ash"))
        water               = float(data("water"))
        superplasticizer    = float(data("superplasticizer"))
        coarse_aggregate    = float(data("coarse_aggregate"))
        fine_aggregate      = float(data("fine_aggregate"))
        age                 = float(data("age"))

        concrete_strength = get_concrete_strength(cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age)
        # return jsonify({"Result":f"Predicted Concreate Strength == {concrete_strength}"})
        return render_template("index.html",Predicted_Concrete_Strength = concrete_strength)
    

    elif request.method == "POST":
        data = request.form

        cement              = data["cement"]
        blast_furnace_slag  = data["blast_furnace_slag"]
        fly_ash             = data["fly_ash"]
        water               = data["water"]
        superplasticizer    = data["superplasticizer"]
        coarse_aggregate    = data["coarse_aggregate"]
        fine_aggregate      = data["fine_aggregate"]
        age                 = data["age"]

        concrete_strength = get_concrete_strength(cement,blast_furnace_slag,fly_ash,water,superplasticizer,coarse_aggregate,fine_aggregate,age)
        # return jsonify({"Result":f"Predicted Concreate Strength == {concrete_strength}"})
        return render_template("index.html",Predicted_Concrete_Strength = concrete_strength)


if __name__ == "__main__":
    app.run(host = config.HOST_NUMBER,port = config.PORT_NUMBER,debug=True)