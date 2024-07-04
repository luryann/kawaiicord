# File: DiscoEgirl.py
import random
import click
import spacy
from collections import defaultdict

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Context and memory for conversation
context = {
    "previous_message": "",
    "user_name": "user",
    "mood": "happy",
    "conversation_history": defaultdict(list)
}

# Sarah's personality details
sarah_details = {
    "name": "Sarah",
    "interests": ["gaming", "anime", "art", "lofi", "k-pop"],
    "cats": ["Mochi", "Leo"],
    "birthday": "July 28",
    "age": 21
}

def update_mood():
    moods = ["happy", "playful", "teasing", "curious", "flirty", "excited", "chill"]
    context["mood"] = random.choice(moods)

def get_synonym(word):
    synonyms = {
        "cool": ["awesome", "amazing", "fantastic", "rad", "lit", "dope"],
        "funny": ["hilarious", "lol-worthy", "amusing", "giggle-inducing", "witty"],
        "sweet": ["adorable", "cute", "lovely", "charming", "endearing"],
        "interesting": ["fascinating", "intriguing", "captivating", "cool", "engaging"],
        "great": ["awesome", "fantastic", "superb", "excellent"],
        "good": ["nice", "pleasant", "decent", "great"],
        "love": ["adore", "cherish", "heart", "luv"]
    }
    return random.choice(synonyms.get(word, [word]))

def nlp_process(message):
    doc = nlp(message.lower())
    words = [token.text for token in doc]
    return words

def add_extra_letters(word):
    if word in ["thank", "you", "cute", "sweet", "awesome"]:
        return word + random.choice(['', 'u', 'uu', 'y', 'yy'])
    return word

def generate_response(message):
    # Update mood occasionally
    if random.random() < 0.3:
        update_mood()

    # Process message with NLP
    words = nlp_process(message)

    # Keyword-based responses
    keyword_responses = {
        "hello": "hii {user_name}! how are you? ^-^",
        "hi": "heyyy {user_name}! what's up? :3",
        "hey": "hello there! how's it going? uwu",
        "love": "aww, love you too {user_name}! <3",
        "game": "ohh, what games do you play {user_name}? :3",
        "games": "gaming is life! what are your favorites? xd",
        "beautiful": "aww, thank you {user_name}! you're so sweet! ^-^",
        "pretty": "hehe, you're making me blush! >///<",
        "cute": "you're too kind {user_name}! <3",
        "feeling": "i'm feeling great, thanks for asking {user_name}! ^_^",
        "how are you": "a bit tired, but i'm happy to chat with you! :3",
        "thanks": "aww, thanks a bunch! you're the best! ^-^",
        "thank you": "thank you so much! <3"
    }

    # Response templates with Sarah's personality and interests
    general_templates = [
        "omg, that's {synonym1}! {emoji}",
        "haha, you're {synonym2}! {emoji}",
        "aww, you're so {synonym3}! {emoji}",
        "lol, i totally agree! {emoji}",
        "hehe, you're making me blush! {emoji}",
        "oh wow, tell me more! {emoji}",
        "eee, that's so {synonym4}! {emoji}",
        "hehe, you're the best! {emoji}",
        "aww, you're adorable! {emoji}",
        "haha, you're making me giggle! {emoji}",
        "wow, that's really {synonym4}! {emoji}",
        "hehe, that's so cool! {emoji}"
    ]

    # Emoji and decoration options
    emojis = ["^-^", ":3", "uwu", "xd", ">///<", "*-*", "^_^", "n_n", "<3", ":d", "❤", "✨"]

    # Select appropriate template based on keywords
    response_template = None
    for word in words:
        if word in keyword_responses:
            response_template = keyword_responses[word]
            break
    if not response_template:
        response_template = random.choice(general_templates)

    # Fill in template with dynamic content
    response = response_template.format(
        synonym1=get_synonym("cool"),
        synonym2=get_synonym("funny"),
        synonym3=get_synonym("sweet"),
        synonym4=get_synonym("interesting"),
        emoji=random.choice(emojis),
        user_name=context["user_name"]
    )

    # Add extra letters to positive comments
    response_words = response.split()
    response = ' '.join([add_extra_letters(word) for word in response_words])

    return response

def chat_with_sarah():
    """
    CLI application to chat with an e-girl bot on Discord using predefined rules and templates.
    """
    while True:
        message = click.prompt("Enter your message")
        context["user_name"] = click.prompt("Enter your name", default="user")
        try:
            response = generate_response(message)
            click.echo(f"{sarah_details['name']}: {response}")
        except Exception as e:
            click.echo(f"Error: {e}")
        cont = click.prompt("Do you want to send another message? (yes/no)", default="yes")
        if cont.lower() != 'yes':
            break

if __name__ == '__main__':
    chat_with_sarah()
