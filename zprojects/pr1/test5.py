import openai
import time

# set your OpenAI API key
openai.api_key = "sk-joeRLSZjsL9bOXI2PT3BlbkFJEc4ys7pAJe7SL82uqxtE"

# define the initial prompt to start the conversation
INITIAL_PROMPT = "Hello! I'm a chatbot. How can I help you today?"

# define the function to generate a response to a given input
def generate_response(input_text, conversation_history):
    # concatenate the input with the conversation history
    prompt = f"{INITIAL_PROMPT}\nUser: {input_text}\nAI:{conversation_history}"
    # use the OpenAI API to generate a response to the prompt
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
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
print(INITIAL_PROMPT)
conversation_history = ""

while True:
    # get user input
    user_input = input("> ")
    # generate response to user input
    response = generate_response(user_input, conversation_history)
    # print the response
    print("Chatbot: " + response)
    # update the conversation history with the user input and the chatbot's response
    conversation_history += f"\nUser: {user_input}\nAI: {response}"
    # wait for a short moment before prompting for the next input
    time.sleep(0.5)
