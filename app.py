import streamlit as st
from langchain_ollama import ChatOllama

# To install ollama and langchain together, use the following command:
# pip install ollama langchain

# Set the title of the Streamlit app
st.title("AI-POWERED-DOCUMENTATION-ASSISTANCE!!")

# Display a welcome message
st.write("HI dhanu this your first project")

# Create a form for user input
with st.form("llm-form"):
    # Text area for user to enter text
    text = st.text_area("Enter your text")
    # Submit button for the form
    submit = st.form_submit_button("Submit")

# Function to generate a response using the ChatOllama model
def generate_response(input_text):
    # Initialize the ChatOllama model
    model = ChatOllama(model="llama3.2:1b", base_url="http://localhost:11434")
    # Invoke the model with the input text and get the response
    response = model.invoke(input_text)
    # Return the content of the response
    return response.content

# Initialize chat history in session state if not already present
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# If the form is submitted and text is entered
if submit and text:
    # Generate a response using the input text
    response = generate_response(text)
    # Append the user input and model response to chat history
    st.session_state['chat_history'].append({"user": text, "ollama": response})
    # Display the response
    st.write(response)

       
st.write("## Chat History")
for chat in reversed(st.session_state['chat_history']):
    st.write(f"**🧑 User**: {chat['user']}")
    st.write(f"**🧠 Assistant**: {chat['ollama']}")
    st.write("---")