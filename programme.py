# Example using Python and Flask
from flask import Flask, request, jsonify
import openai
import csv

app = Flask(__name__)

# Initialize OpenAI API key
openai.api_key = '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'

# Define endpoint for answering questions
@app.route('/answer', methods=['POST'])
def answer_question():
    data = request.get_json()
    user_question = data['question']

    # Query ChatGPT API
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_question,
        max_tokens=100
    )

    # Extract answer
    answer = response.choices[0].text.strip()

    # Store in CSV file
    with open('/app/data/questions.csv', 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([user_question, answer])

    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
