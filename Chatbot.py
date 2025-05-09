import re
import nltk
from nltk.tokenize import word_tokenize

# Download NLTK resources once
nltk.download('punkt')

def preprocess(text):
    # Lowercase and remove punctuation
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def chatbot_response(user_input):
    user_input = preprocess(user_input)

    responses = {
        r"\b(hello|hi|hey)\b": "Hello! Welcome to FoodieBot 🍔. How can I assist you today?",
        r"\bhow are you\b": "I'm great! I'm here to help you order tasty food.",
        r"\b(menu|food|order)\b": "We have pizza, burgers, biryani, pasta, and more. What would you like?",
        r"\b(cancel order|order cancel)\b": "You can cancel your order within 5 minutes of placing it.",
        r"\b(track|where is my order)\b": "You can track your order in 'My Orders' section.",
        r"\b(payment|pay|method)\b": "We accept UPI, cards, and cash on delivery.",
        r"\b(offer|discount|coupon)\b": "Use code FOOD10 to get 10% off your first order!",
        r"\b(delivery time|when)\b": "Delivery takes about 30–45 minutes.",
        r"\b(address|change address)\b": "You can change it in your profile settings.",
        r"\b(support|help|customer care)\b": "Call us at 1800-456-FOOD for support.",
        r"\b(rating|review)\b": "Our top-rated items include Paneer Butter Masala and Chicken Biryani.",
        r"\b(bye|exit|goodbye)\b": "Goodbye! Enjoy your food! 🍽️"
    }

    for pattern, response in responses.items():
        if re.search(pattern, user_input):
            return response

    return "Sorry, I didn't catch that. Could you try asking in another way?"

# Chatbot loop
print("Welcome to FoodieBot! Type 'exit' to end the conversation.")

while True:
    user_message = input("You: ")
    if preprocess(user_message) in ["bye", "exit", "goodbye"]:
        print("Chatbot: Goodbye! Enjoy your food! 🍽️")
        break
    response = chatbot_response(user_message)
    print("Chatbot:", response)
