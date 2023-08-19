
import openai

# Predefined answers
predefined_answers = {
    "What's the admission process at Lambton College?": "You can apply through our online portal, submit the necessary documents, and after a review, you'll be informed about your application status.",
    "What is the minimum GPA required to be eligible for a co-op at Lambton college in Toronto?": "2.8",
    "Are there any student clubs at Lambton?": "Lambton has various student clubs ranging from arts to academic to recreational to business. You can visit moodle to learn more about clubs at Lambton college in Toronto.",
    "How can I get a parking permit?": "Parking permits can be obtained from the reception desk by submitting the required fees."
    # ... add more questions and answers as needed
}

def ask_openai(question, context=None):
    CONTEXT_LIMIT = 4000  # Adjust based on your needs.
    
    # If context is too long, truncate it.
    if context and len(context) > CONTEXT_LIMIT:
        context = context[-CONTEXT_LIMIT:]
    
    # Set up the initial system message
    messages = [{"role": "system", "content": "You are I-Care Interactive chatbot designed to help newcomers at Lambton College in Toronto."}]
    
    # Add the context as a user message if it's provided
    if context:
        messages.append({"role": "user", "content": context})
    
    # Add the question as a user message
    messages.append({"role": "user", "content": question})
    
    # Make the chat completion call
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=1500  # you can adjust this to control response length
    )
    
    return response.choices[0].message['content'].strip()

def myanswer(question, dataset_text=None):
    return predefined_answers.get(question, ask_openai(question, dataset_text))

from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

openai.api_key = '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'

dataset_text = '/content/drive/MyDrive/Capstone/extracted_text.txt'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/ask', methods=['POST'])
def get_answer():
    question = request.json['question']
    answer = myanswer(question)  # Assuming you have the 'ask_openai' function from step 2
    return jsonify({"answer": answer})
    
if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)



