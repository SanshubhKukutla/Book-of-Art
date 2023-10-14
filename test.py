from flask import Flask, request, render_template
import openai

openai.api_key = "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"

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def generate_image():
    img_urls = []

    if request.method == "POST":
        # Get user input from the form
        user_texts = request.form.getlist("user_text[]")
        print(user_texts)
        for text in user_texts:
            image_url = generate_image_with_text(text)
            img_urls.append(image_url)
        print(img_urls)
        return render_template("index.html", image_urls=img_urls)

    return render_template("index.html")


def generate_image_with_text(text):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Make a story from this text:\n" + text,
        max_tokens=250,  # Adjust the number of tokens for your desired summary length
    )

    story = response.choices[0].text

    # Create a blank image
    image_response = openai.Image.create(prompt=story, n=1, size="512x512")

    image_url = image_response.data[0].url
    # Return the image URL
    return image_url


if __name__ == "__main__":
    app.run(debug=True, port=8080)
