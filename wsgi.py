from flask import Flask
from MazeApp import MazeApp
application = Flask(__name__)


@application.route("/")
def run():
    return MazeApp()


if __name__ == "__main__":
    application.run()
