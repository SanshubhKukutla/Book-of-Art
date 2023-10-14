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