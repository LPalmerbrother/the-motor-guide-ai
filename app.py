import os
from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Home page → chat UI
@app.route('/')
def index():
    return render_template('index.html')

# /ask endpoint → OpenAI call
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get('question', '')
    messages = [
        {"role": "system",
         "content": "You are The Motor Guide AI—an expert auto mechanic. Answer clearly, suggest steps, and wrap part names with AFFILIATE_LINK(part name)."}
    ]
    messages.append({"role": "user", "content": question})
    resp = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )
    answer = resp.choices[0].message.content
    return jsonify(answer=answer)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
