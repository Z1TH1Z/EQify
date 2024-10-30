import tkinter as tk
import google.generativeai as genai
from Artistid import get_current_track
from Artistid import SPOTIFY_ACCESS_TOKEN
# Configure your Gemini API key
genai.configure(api_key='AIzaSyBJJZelvIVRTzay0LjcSVRTou5U2nYlMxA')  # Replace with your actual API key

track_info = get_current_track(SPOTIFY_ACCESS_TOKEN)
track_name  =track_info['name']
print(track_name)
artists = track_info['artists']
def get_response_from_gemini(user_message):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash")  # Specify the model to use
        response = model.generate_content(user_message)
        return response.text  # Return the generated text
    except Exception as e:
        return f"Error: {str(e)}"  # Return error message if API call fails


def send_message():
    user_message = "Lyrics of"+ user_input.get()
    if user_message:
        #chat_display.insert(tk.END, f"You: {user_message}\n")  # Display user message
        user_input.delete(0, tk.END)  # Clear input field

        # Get response from Gemini API
        bot_response = get_response_from_gemini(user_message)
        chat_display.insert(tk.END, f"Gemini: {bot_response}\n")  # Display bot response


# Create the main window
root = tk.Tk()
root.title("Gemini Chatbot")

# Create and place widgets
chat_display = tk.Text(root, wrap=tk.WORD, width=50, height=20)
chat_display.pack(pady=10)

user_input = tk.Entry(root, width=50)
user_input.pack(pady=10)

send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()