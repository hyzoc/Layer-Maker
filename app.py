from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    message = "Layer Structure"
    lay1 = request.form["layer1"]
    lay2 = request.form["layer2"]
    th1 = request.form["thickness1"]
    th2 = request.form["thickness2"]
    return render_template("index.html", message = message, layer1 = lay1, layer2 = lay2, thickness1 = th1, thickness2 = th2,)

if __name__=='__main__':
  app.run(debug=True)