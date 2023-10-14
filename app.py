from flask import Flask, request, render_template
import openai
import os
from time import time
import random
import string

openai.api_key = "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"

app = Flask(__name__)

# Ensure the 'static' directory exists
if not os.path.exists('static'):
    os.makedirs('static')

@app.route("/", methods=["GET", "POST"])
def generate_image():
    if request.method == "POST":
        # Get user input from the form
        user_text = request.form.get("user_text")

        return render_template("index.html", image_url=generate_image_with_text(user_text))

    return render_template("index.html")

def generate_image_with_text(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Make a story from this text:\n" + text,
        max_tokens=250  # Adjust the number of tokens for your desired summary length
    )

    story = response.choices[0].text

    # Create a blank image
    image_response = openai.Image.create(prompt=story, n=1, size="1024x1024")

    image_url = image_response.data[0].url
    # Return the image URL
    return image_url


if __name__ == "__main__":
    app.run(debug=True, port=8080)
