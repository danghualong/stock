from src import createApp
import os
from src.tools.response_factory import create_response
from src.model import NoFound



app = createApp()

@app.route("/")
def index():
    return create_response([1,3,4])


if __name__ == '__main__':
    app.run()