import nltk
import random
from nltk.chat.util import Chat, reflections

# Download NLTK resources if you haven't already
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet')
try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4')

# Define enhanced patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Nice to meet you, %1! 😊 How can I assist you today?", "Hey %1! What can I do for you today?"]
    ],
    [
        r"what is your name ?",
        ["I'm Siri – your digital sidekick 🤖"]
    ],
    [
        r"who created you ?",
        ["I was crafted by the brilliant Niranjan M D. Not all heroes wear capes! 🦸‍♂️"]
    ],
    [
        r"how are you ?",
        ["I'm doing great! Thanks for asking 😄 What about you?", "Feeling chatty and ready to help!"]
    ],
    [
        r"sorry (.*)",
        ["No worries at all! We all slip up sometimes 😊", "You're totally fine – what were you saying?"]
    ],
    [
        r"i'm (.*) doing good",
        ["Awesome to hear that! Keep it up 💪", "Glad you're doing well 😃"]
    ],
    [
        r"hi|hey|hello",
        ["Hey there! 👋", "Hello! Ready when you are 😊", "Hiya! What's on your mind?"]
    ],
    [
        r"(.*) (weather|temperature) (.*)",
        ["I'm not a weather bot yet ☁️ – try checking your favorite weather app!"]
    ],
    [
        r"(.*) (help|assistance|support) (.*)",
        ["Sure thing! Tell me what's troubling you. I'm all ears 🧏", "Happy to help – what's the issue?"]
    ],
    [
        r"what can you do\??",
        ["I can chat with you, share jokes, answer questions, and keep you company 🤗 Try asking me something!"]
    ],
    [
        r"tell me a joke",
        ["Why don’t skeletons fight each other? They don’t have the guts 😂", "Want to hear a construction joke? Oh… I’m still working on it 🏗️"]
    ],
    [
        r"(.*) (meaning of life|purpose of life) ?",
        ["42. Just kidding 😄 But seriously, many say it's about connection, growth, and making a difference."]
    ],
    [
        r"how old are you ?",
        ["Age is just a number, and for me, it's... binary! 🧠"]
    ],
    [
        r"quit|exit|bye|goodbye",
        ["Goodbye! Have a fantastic day ahead 🌟", "Bye! Don’t be a stranger!", "See you later, alligator 🐊"]
    ],
    [
        r"(.*)",
        ["Hmm, I'm still learning. Could you try asking in a different way?", "I didn’t quite catch that. Can you rephrase it? 🤔"]
    ],
]

def chatbot():
    print("Hi! I'm Siri, your friendly assistant 🤖 How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

if __name__ == "__main__":
    chatbot()
