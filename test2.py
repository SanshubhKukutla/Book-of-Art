import openai

# Replace 'YOUR_API_KEY' with your actual OpenAI API key
api_key = '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'

# Input sentences
input_sentences = [
    "Once upon a time, in a small village nestled in the mountains, there lived a young girl named Emma.",
    "Emma had always been curious and adventurous, often exploring the woods surrounding the village.",
    "One day, while she was out on her usual adventure, she stumbled upon a hidden cave entrance.",
    "Inside the cave, she found an ancient treasure chest that was said to hold unimaginable riches.",
    "Little did she know that her discovery would lead her on the adventure of a lifetime."
]

# Combine the sentences into a single prompt
story_context = "\n".join(input_sentences)
# Generate the story using the OpenAI API
openai.api_key = api_key
response = openai.Completion.create(
    engine="text-davinci-002",
    prompt="Generate a 5 paragraph story from the following context: \n" + story_context,
    max_tokens=900  # Adjust the max_tokens to control the length of the generated story
)

# Extract the generated story
generated_story = response.choices[0].text

# Split the story into paragraphs
paragraphs = generated_story.split(". ")

# Print the story with paragraphs
for paragraph in paragraphs:
    if paragraph != "":
        print(paragraph)
        images = openai.Image.create(prompt="Generate a painting from the following context: \n" + paragraph, n=1, size="1024x1024")
        print("Generated Image URL:", images["data"][0]["url"])

