from flask import Flask, request, jsonify
from hn_app import hn_utils

#Dummy data
sentence1 = "I hate everyone at Hacker News, you all suck and I hope you have a rotten day"
sentence2 = "I love everyone at Hacker News! you all make me feel warm and fuzzy inside"
sentence3 = "I mostly like everyone at Hacker News, but sometimes this site is toxic"

#Dummy list
sentence_list = [sentence1, sentence2, sentence3]
negative_list = [sentence1, sentence1, sentence2]

def create_app():
    app = Flask(__name__)

    @app.route('/sentence/<sentence>', methods=['GET'])
    def myfunc(sentence):
      return jsonify({"Sentence": sentence,
                      "Analysis": str(hn_utils.custom_score(sentence))})

    return app

if __name__ == "__main__":
    app = create_app()
