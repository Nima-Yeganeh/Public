import openai

# set your OpenAI API key
openai.api_key = "sk-joeRLSZjsL9bOXI2PT3BlbkFJEc4ys7pAJe7SL82uqxtE"

# prompt user for topic
topic = input("What would you like to talk about today? ")

# define a prompt to generate response
prompt = f"Let's talk about {topic}. What would you like to know?"

# define a function to generate a response to user input
def generate_response(input_text):
    # concatenate the user input with the prompt
    prompt_with_input = f"{prompt}\nUser: {input_text}\nAI:"
    # use the OpenAI API to generate a response to the prompt
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt_with_input,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.7,
    )
    # extract the generated response from the API response
    message = response.choices[0].text.strip()
    # return the generated response
    return message

# start the conversation
while True:
    # get user input
    user_input = input("User: ")
    # generate a response to the user input
    response = generate_response(user_input)
    # print the generated response
    print(response)
