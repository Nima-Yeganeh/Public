import openai

# set your OpenAI API key
openai.api_key = "sk-joeRLSZjsL9bOXI2PT3BlbkFJEc4ys7pAJe7SL82uqxtE"

# define a prompt to generate response
prompt = "Let's talk about cats. What would you like to know?"

# define a function to generate a response to a given input
def generate_response(input_text):
    # concatenate the input with the prompt
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

# generate responses for some example questions
question1 = "What is the average lifespan of a cat?"
response1 = generate_response(question1)
print(f"Question: {question1}\nResponse: {response1}\n")

question2 = "What are some common health problems in cats?"
response2 = generate_response(question2)
print(f"Question: {question2}\nResponse: {response2}\n")

question3 = "How can I train my cat to use the litter box?"
response3 = generate_response(question3)
print(f"Question: {question3}\nResponse: {response3}\n")
