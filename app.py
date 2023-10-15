from flask import Flask, request, render_template
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route('/')
def hello_world():
    message = "Hello, Flask! This message is displayed in the browser."
    return render_template('index.html', message=message)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/creators')
def creators():
    return render_template('creators.html')

@app.route("/generate_image", methods=["GET", "POST"])
def generate_image():
    img_urls = []

    if request.method == "POST":
        # Get user input from the form
        user_texts = request.form.getlist("user_text[]")
        combined_prompt = ""
        
        for text in user_texts:
            if text.strip():
                combined_prompt += text + ". "
                image_url = generate_image_with_text(combined_prompt)
                img_urls.append(image_url)
        
        return render_template("storyscreen.html", image_urls=img_urls, captions = user_texts)

    return render_template("storyinput.html")


def generate_image_with_text(text, num_images=3):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt="Make a story from this text:\n" + text,
        max_tokens=250,  # Adjust the number of tokens for your desired summary length
    )

    story = response.choices[0].text
    
    image_urls = []

    # Generate images for the story
    for _ in range(num_images):
        image_response = openai.Image.create(prompt="Generate a whimsical image from this context: \n" + story, n=1, size="256x256")
        image_urls.append(image_response["data"][0]["url"])

    return image_urls


if __name__ == "__main__":
    app.run(debug=True, port=8080)
