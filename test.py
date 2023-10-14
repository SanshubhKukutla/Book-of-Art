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
        return render_template("appTest.html", image_urls=img_urls)

    return render_template("appTest.html")


def generate_image_with_text(text, num_images=3):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Make a story from this text:\n" + text,
        max_tokens=250,  # Adjust the number of tokens for your desired summary length
    )

    story = response.choices[0].text
    print(story)
    image_urls = []

    # Generate images for the story
    for _ in range(num_images):
        image_response = openai.Image.create(prompt=story, n=1, size="256x256")
        image_urls.append(image_response["data"][0]["url"])

    return image_urls


if __name__ == "__main__":
    app.run(debug=True, port=8080)
