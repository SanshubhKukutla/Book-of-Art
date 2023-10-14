<<<<<<< HEAD
import openai


# Set your OpenAI API key
openai.api_key = "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"

stories = []
input_text = ""
count = 0

while True:
    input_text = input("Input story idea or q to quit: \n")

    if input_text.lower() == "q":
        break

    if count == 0:
        # Use the OpenAI API to summarize the text
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Make a story from this text:\n" + input_text,
            max_tokens=250,  # Adjust the number of tokens for your desired summary length
        )
    else:
        response = openai.Completion.create(
            engine="text-davinci-002",
            prompt="Make a story by using the previous story: "
            + stories[count - 1][0]
            + " and this text as a continuation:\n"
            + input_text,
            max_tokens=250,  # Adjust the number of tokens for your desired summary length
        )

    # Extract and print the generated summary
    summary = response.choices[0].text

    # Generate an image
    response = openai.Image.create(prompt=summary, n=1, size="1024x1024")

    # Retrieve the image URL
    image_url = response["data"][0]["url"]

    # Append image url to array
    stories.append([summary, image_url])

    count += 1

# Now you can use 'image_url' to view or download the generated image

for story in stories:
    print("Summary: " + story[0])
    print()
    print("Generated Image URL:", story[1])
=======
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
>>>>>>> 9ed9f61abd5a808dab3bfaed23d0e5b4a5893141
