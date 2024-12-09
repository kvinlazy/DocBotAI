import streamlit as st
import openai
import time 

# Set up OpenAI API key
openai.api_key = "Your_Key_API"  # Replace with your OpenAI API key

# Title of the app
st.title("AI Doctor Chatbot")
st.subheader("Ask any medical question, and I'll try my best to assist!")

# Function to query OpenAI ChatGPT model with rate limit and quota handling
def query_openai(messages):
    prompt = messages[-1]['content']  # Use the last message as the prompt
    
    while True:
        try:
            # Make the API call to the ChatGPT model
            response = openai.Completion.create(
                model="gpt-3.5-turbo",  # You can use "gpt-4" if you have access
                prompt=prompt,  # Send the prompt (the last user message)
                max_tokens=150,  # Limit the number of tokens in the response
                temperature=0.7  # Control the randomness of the response
            )
            
            # If we successfully get a response, return it
            return response['choices'][0]['text'].strip()
        
        except openai.error.RateLimitError as e:
            # If rate limit is exceeded, wait for a while and retry
            st.warning(f"Rate limit exceeded. Retrying in 30 seconds... {e}")
            time.sleep(30)  # Wait for 30 seconds before retrying
            
        except openai.error.OpenAIError as e:
            # If quota is exceeded, inform the user and stop the process
            if "insufficient_quota" in str(e):
                st.error("Your API usage limit has been exceeded. Please check your plan and billing details.")
                return None  # Stop further processing
            else:
                # General error handling for other OpenAI errors
                st.error(f"An error occurred: {e}")
                return None

# Initialize session state for chat history if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Unique text input for user query
user_input = st.text_input("Your Question:", "", key="unique_question_input")

if user_input:
    # Append user input to session state messages
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Send input to OpenAI's model
    with st.spinner("Thinking..."):
        ai_response = query_openai(st.session_state.messages)
    
    # Append AI response to the chat history, if available
    if ai_response:
        st.session_state.messages.append({"role": "assistant", "content": ai_response})

# Display the chat history
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.write(f"**You:** {msg['content']}")
    else:
        st.write(f"**AI Doctor:** {msg['content']}")

# Display medical disclaimer
st.markdown("### Medical Disclaimer")
st.markdown("This is an AI tool and **not a substitute for professional medical advice**.")
