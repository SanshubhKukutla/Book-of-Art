from flask import Flask, request, render_template, redirect, url_for
import openai

openai.api_key = "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"

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_image():
    if request.method == "POST":
        # Get user input from the form
        user_texts = request.form.getlist("user_text[]")
        print(user_texts)
        
        # Redirect to the loading screen while generating images
        return render_template("loadingscreen.html")

        img_urls = []
        for text in user_texts:
            image_url = generate_image_with_text(text)
            img_urls.append(image_url)
        print(img_urls)
        return render_template("storyscreen.html", image_urls=img_urls, captions=user_texts)

    return render_template("storyinput.html")

# ... your generate_image_with_text function and if __name__ block remain the same ...

if __name__ == "__main__":
    app.run(debug=True, port=8080)