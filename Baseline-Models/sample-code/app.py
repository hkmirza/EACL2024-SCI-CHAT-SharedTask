import random
from flask import Flask, request, jsonify
from transformers import BlenderbotTokenizer, BlenderbotForConditionalGeneration
from transformers import (
    AutoModelForCausalLM, AutoTokenizer,
    BlenderbotSmallForConditionalGeneration,
    GPT2Tokenizer, GPT2LMHeadModel, AutoModelForSeq2SeqLM,
)

app = Flask(__name__)

# Load the BlenderBot model and tokenizer
tokenizer = BlenderbotTokenizer.from_pretrained("facebook/blenderbot-400M-distill")
model = BlenderbotForConditionalGeneration.from_pretrained("facebook/blenderbot-400M-distill")


@app.route("/ask", methods=["POST"])
def ask_question():
    data = request.json
    user_message = data["user_message"]

    # Generate a response using the BlenderBot model
    inputs = tokenizer(user_message, return_tensors="pt")
    bot_response = model.generate(**inputs)

    # Decode the response and send it back
    response_text = tokenizer.decode(bot_response[0], skip_special_tokens=True)
    
    return jsonify({"bot_response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
