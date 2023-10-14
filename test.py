import openai


# Set your OpenAI API key
openai.api_key = "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"


input_text = """
      In a tiny coastal town, there was a lighthouse that had stood tall for generations. It was a guiding beacon for sailors, ships, and a symbol of hope for the villagers.

One stormy night, a young girl named Lily watched the lighthouse's beam flicker and fade. She knew that it needed a new lightbulb. Lily decided to take action. She gathered her allowance, which she had saved for a special toy, and bought the lightbulb.

The villagers were amazed by Lily's generosity. With their help, they replaced the lightbulb, and the lighthouse's beam shone brightly again. It guided sailors safely home and warmed the villagers' hearts.

Lily realized that sometimes, the light we share with others shines brighter than any lighthouse.
"""

# Use the OpenAI API to summarize the text
response = openai.Completion.create(
    engine="davinci",
    prompt="Please summarize the following text:\n" + input_text,
    max_tokens=50,  # Adjust the number of tokens for your desired summary length
)

# Extract and print the generated summary
summary = response.choices[0].text

print(summary)

# Generate an image
response = openai.Image.create(prompt=input_text, n=1, size="1024x1024")

# Retrieve the image URL
image_url = response["data"][0]["url"]

# Now you can use 'image_url' to view or download the generated image
print("Generated Image URL:", image_url)
