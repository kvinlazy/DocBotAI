# AI Health Chatbot

## Description
AI Health Chatbot is a Streamlit web application powered by OpenAI's GPT model to help answer medical-related questions. It's designed to assist users by providing general information about medical conditions, symptoms, treatments, and more. **Important**: This chatbot is not a substitute for professional medical advice. Always consult a healthcare provider for critical issues.

## Features
- **Interactive User Interface**: Built with Streamlit to provide a seamless and easy-to-use experience.
- **AI-Powered Medical Answers**: Integration with OpenAI’s GPT model to provide insightful answers to user queries.
- **Rate Limit & Quota Handling**: Efficient handling of OpenAI API rate limits and usage quota with retries.
- **Medical Disclaimer**: Clearly informs users that the bot is not a replacement for professional medical consultation.

## Requirements
To run this project, you will need:
- Python 3.7 or higher
- Streamlit 1.0 or higher
- OpenAI Python SDK (openai)

### Install Requirements:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/repository-name.git
   cd repository-name
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your OpenAI API key in the script (or use environment variables for security).

4. Start the Streamlit application:
   ```bash
   streamlit run app.py
   ```

## How it Works:
1. Users input their medical question into the text input box.
2. The question is sent to OpenAI’s GPT model (e.g., `gpt-3.5-turbo`).
3. The model generates a response based on the query.
4. The response is displayed, and the chat history is shown.
5. If there are API errors, the app retries or notifies users of quota limits.

## Example Use Case:
1. A user asks, "What are the symptoms of diabetes?"
2. The AI Health Chatbot processes the question and provides a response such as: "Common symptoms of diabetes include frequent urination, increased thirst, and blurred vision."
3. The response is shown, and the conversation history remains visible to the user.

## Medical Disclaimer
This AI Health Chatbot is for educational purposes only and is **not a substitute for professional medical advice**. Always consult a qualified healthcare professional for any medical concerns or emergencies.


### Additional Notes:
- **Security**: Always ensure that your OpenAI API key is kept secure and not exposed in public repositories. You may choose to use environment variables or a secrets manager to handle this securely.
- You can consider implementing **logging** or **error handling** features to improve the user experience, especially when there are errors in the AI response or rate limits are hit.
