from flask import Flask, render_template
app = Flask(__name__)


@app.route("/")
def index():
    # we are hardcoding this just to demonstrate how we can do conditionals in our template files, in future we won't be hardcoding this.
    signed_in = False
    return render_template('index.html', signed_in=signed_in)


if __name__ == '__main__':
    app.run()
