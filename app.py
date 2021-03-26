from src import createApp
import os
from src.tools.response_factory import create_response

app = createApp()


@app.route("/")
def index():
    mode=os.getenv("FLASK_ENV", "---")
    items=[dict(path=i.rule,methods=list(i.methods),endpoint=i.endpoint) for i in app.url_map._rules]
    return create_response(items)


if __name__ == '__main__':
    app.run()