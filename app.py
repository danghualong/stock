from src import createApp
import os

app = createApp()


@app.route("/")
def index():
    mode=os.getenv("FLASK_ENV","ZZ")
    return "Hello Flask {0}".format(mode)


if __name__ == '__main__':
    app.run()