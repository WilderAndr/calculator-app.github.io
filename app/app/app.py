from flask import Flask, render_template, request

app = Flask(__name__)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        num1 = float(request.form["num1"])
        num2 = float(request.form["num2"])
        operation = request.form["operation"]
        
        if operation == "suma":
            result = suma(num1, num2)
        elif operation == "resta":
            result = resta(num1, num2)
        elif operation == "multiplicacion":
            result = multiplicacion(num1, num2)
        elif operation == "division":
            result = division(num1, num2)
    
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
