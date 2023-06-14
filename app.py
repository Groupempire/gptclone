from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
API_KEY = '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'  # Replace with your actual OpenAI API key
openai.api_key = API_KEY

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_response', methods=['POST'])
def generate_response():
    user_input = request.form['user_input']
    conversation = request.form['conversation']

    conversation += 'User: ' + user_input + '\n'
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=conversation,
        max_tokens=2000,
        temperature=0.7
    )
    ai_response = response.choices[0].text.strip()

    return jsonify({'ai_response': ai_response, 'conversation': conversation})

if __name__ == '__main__':
    app.run(debug=True)
