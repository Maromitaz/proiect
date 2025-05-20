from flask import Flask, render_template

app = Flask(
    __name__, 
    template_folder="web"
    )

@app.route("/")
def index():
    return render_template("templates/index.html", is_web = True)

if(__name__ == "__main__"):
    app.run(debug=True)