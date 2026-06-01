import os
import re

# 1. डेटा क्लिनिंग आणि प्रीप्रोसेसिंग फंक्शन
def clean_text(text):
    # सर्व अक्षरे लहान (lowercase) करणे
    text = text.lower()
    # विरामचिन्हे आणि स्पेशल कॅरेक्टर्स काढून टाकणे
    text = re.sub(r'[^\w\s]', '', text)
    return text

# 2. मुख्य स्पॅम क्लासिफायर क्लास (AI Logic)
class SpamClassifier:
    def __init__(self):
        # स्पॅम आणि चांगल्या मेसेजमधील महत्त्वाचे शब्द (Keywords)
        self.spam_words = ["win", "free", "money", "click", "prize", "offer", "cash", "urgent", "lottery", "subscribe"]
        self.ham_words = ["hello", "project", "meeting", "class", "study", "code", "assignment", "work", "team", "thanks"]

    def predict(self, message):
        cleaned_message = clean_text(message)
        words = cleaned_message.split()

        spam_score = 0
        ham_score = 0

        # शब्दांचे वर्गीकरण आणि स्कोअरिंग
        for word in words:
            if word in self.spam_words:
                spam_score += 1
            if word in self.ham_words:
                ham_score += 1

        # अंतिम निर्णय (Rule-based Classification)
        if spam_score > ham_score:
            return "SPAM 🔴"
        else:
            return "NOT SPAM (HAM) 🟢"

# 3. मुख्य प्रोग्राम एक्झिक्यूशन (Main Loop)
def main():
    print("==================================================")
    print("       AI SPAM CLASSIFIER PROJECT (PYTHON)       ")
    print("==================================================")
    
    classifier = SpamClassifier()

    while True:
        print("\n--------------------------------------------------")
        user_message = input("Enter a message to check (or type 'exit' to quit): ")
        
        if user_message.lower() == 'exit':
            print("\nExiting the project. Thank you!")
            print("==================================================")
            break

        if not user_message.strip():
            print("❌ Message cannot be empty! Please try again.")
            continue

        # प्रेडिक्शन करणे
        result = classifier.predict(user_message)
        print(f"Result: The message is classified as -> {result}")

if __name__ == "__main__":
    main()
