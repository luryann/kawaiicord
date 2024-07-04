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

def generate_response(message):
    # Update mood occasionally
    if random.random() < 0.3:
        update_mood()

    # Lowercase message for easier keyword matching
    message_lower = message.lower()
    context["previous_message"] = message
    context["conversation_history"][context["user_name"]].append(message)

    # Response templates with a flirty tone and e-girl lingo
    templates = {
        "general": [
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
        ],
        "greeting": [
            "hii {user_name}! how are you? ^-^",
            "heyyy {user_name}! what's up? :3",
            "hello there! how's it going? uwu",
            "hiya! hope you're having a great day! ^_^"
        ],
        "love": [
            "aww, love you too {user_name}! <3",
            "you're the best! mwah! :*",
            "hehe, you're making my heart melt! >///<",
            "love you lots {user_name}! ^-^"
        ],
        "game": [
            "ohh, what games do you play {user_name}? :3",
            "gaming is life! what are your favorites? xd",
            "i love games too! let's play together sometime! ^-^",
            "what's your top game right now? *-*"
        ],
        "compliment": [
            "aww, thank you {user_name}! you're so sweet! ^-^",
            "hehe, you're making me blush! >///<",
            "you're too kind {user_name}! <3",
            "thanks a lot! you're amazing too! :3",
            "aww, that's so nice of you! ^-^"
        ],
        "feeling": [
            "i'm feeling great, thanks for asking {user_name}! ^_^",
            "a bit tired, but i'm happy to chat with you! :3",
            "feeling awesome! how about you? :d",
            "i'm good! how are you doing {user_name}? ^-^"
        ],
        "thankful": [
            "aww, thanks a bunch! you're the best! ^-^",
            "thank you so much! <3",
            "hehe, that's so sweet of you to say! :3",
            "thanks, i appreciate it! ^-^"
        ],
        "flirty": [
            "oh, stop it you, {user_name}! ^-^",
            "aww, you're making me blush, {user_name}! >///<",
            "haha, you're such a charmer! :3",
            "oh {user_name}, you're so funny! ^-^",
            "you always know how to make me smile! <3"
        ]
    }

    # Emoji and decoration options
    emojis = ["^-^", ":3", "uwu", "xd", ">///<", "*-*", "^_^", "n_n", "<3", ":d", "❤", "✨"]

    # Keyword-based responses
    keyword_responses = {
        "hello": templates["greeting"],
        "hi": templates["greeting"],
        "hey": templates["greeting"],
        "love": templates["love"],
        "game": templates["game"],
        "games": templates["game"],
        "beautiful": templates["compliment"],
        "pretty": templates["compliment"],
        "cute": templates["compliment"],
        "feeling": templates["feeling"],
        "how are you": templates["feeling"],
        "thanks": templates["thankful"],
        "thank you": templates["thankful"]
    }

    # Process message with NLP
    words = nlp_process(message)

    # Select appropriate template based on keywords
    for word in words:
        if word in keyword_responses:
            template = random.choice(keyword_responses[word])
            break
    else:
        # Choose a general or flirty response based on mood
        template = random.choice(templates["flirty"]) if context["mood"] == "flirty" else random.choice(templates["general"])

    # Fill in template with dynamic content
    response = template.format(
        synonym1=get_synonym("cool"),
        synonym2=get_synonym("funny"),
        synonym3=get_synonym("sweet"),
        synonym4=get_synonym("interesting"),
        emoji=random.choice(emojis),
        user_name=context["user_name"]
    )

    return response

@click.command()
@click.option('--message', prompt='Enter your message', help='The message you want to send to the e-girl.')
@click.option('--name', default='user', help='Your name for a personalized experience.')
def chat(message, name):
    """
    CLI application to chat with an e-girl bot on Discord using predefined rules and templates.
    """
    context["user_name"] = name
    try:
        response = generate_response(message)
        click.echo(f"E-girl: {response}")
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == '__main__':
    chat()
