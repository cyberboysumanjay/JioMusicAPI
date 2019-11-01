from flask import Flask,request,jsonify,json
import jiomusic

app = Flask(__name__)
app.secret_key = 'thankyoutonystark#weloveyou3000'

@app.route('/')
def home():
   return "Thanks for testing JioMusic API. To get started head up to my GitHub for documentation."

@app.route('/result/', methods=['GET', 'POST'])
def result():
    query=request.args.get('query')
    if jiomusic.song_search(query=query) is not None:
        return jsonify(jiomusic.song_search(query=query))
    else:
        # Not catching any error because I hope this will never crash!
        # You should not get this message eveeeeeeeeeeeeer!
        return "Something went wrong!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=5001,use_reloader=True,threaded = True)
