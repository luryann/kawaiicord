# File: DiscoEgirl.py
import random
import click
from collections import defaultdict

# Context and memory for conversation
context = {
    "previous_message": "",
    "user_name": "user",
    "mood": "happy",
    "conversation_history": defaultdict(list)
}

def update_mood():
    moods = ["happy", "playful", "teasing", "curious", "friendly", "excited", "chill"]
    context["mood"] = random.choice(moods)

def get_synonym(word):
    synonyms = {
        "cool": ["awesome", "amazing", "fantastic", "rad", "lit", "dope"],
        "funny": ["hilarious", "lol-worthy", "amusing", "giggle-inducing", "witty"],
        "sweet": ["adorable", "cute", "lovely", "charming", "endearing"],
        "interesting": ["fascinating", "intriguing", "captivating", "cool", "engaging"],
        "great": ["awesome", "fantastic", "superb", "excellent"],
        "good": ["nice", "pleasant", "decent", "great"]
    }
    return random.choice(synonyms.get(word, [word]))

def random_apostrophe(word):
    if random.choice([True, False]):
        return word
    return word.replace("'", "")

def random_capitalize(text):
    return ''.join(random.choice([char.upper(), char.lower()]) for char in text)

def nlp_process(message):
    # Very basic NLP processing
    words = message.lower().split()
    return words

def generate_response(message):
    # Update mood occasionally
    if random.random() < 0.3:
        update_mood()

    # Lowercase message for easier keyword matching
    message_lower = message.lower()
    context["previous_message"] = message
    context["conversation_history"][context["user_name"]].append(message)

    # Response templates
    templates = {
        "general": [
            "omg, that's {synonym1}! {emoji}",
            "haha, youre {synonym2}! {emoji}",
            "aww, youre so {synonym3}! {emoji}",
            "lol, i totally agree! {emoji}",
            "hehe, youre making me blush! {emoji}",
            "oh wow, tell me more! {emoji}",
            "eee, that's so {synonym4}! {emoji}",
            "hehe, youre the best! {emoji}",
            "aww, youre adorable! {emoji}",
            "haha, youre making me giggle! {emoji}",
            "wow, that's really {synonym4}! {emoji}",
            "hehe, thats so cool! {emoji}"
        ],
        "greeting": [
            "hii {user_name}! how are you? ^-^",
            "heyyy {user_name}! whats up? :3",
            "hello there! how's it going? uwu",
            "hiya! hope youre having a great day! ^_^"
        ],
        "love": [
            "aww, love you too {user_name}! <3",
            "youre the best! mwah! :*",
            "hehe, youre making my heart melt! >///<",
            "love you lots {user_name}! ^-^"
        ],
        "game": [
            "ohh, what games do you play {user_name}? :3",
            "gaming is life! what are your favorites? xd",
            "i love games too! lets play together sometime! ^-^",
            "whats your top game right now? *-*"
        ],
        "compliment": [
            "aww, thank you {user_name}! youre so sweet! ^-^",
            "hehe, youre making me blush! >///<",
            "youre too kind {user_name}! <3",
            "thanks a lot! youre amazing too! :3",
            "aww, thats so nice of you! ^-^"
        ],
        "feeling": [
            "im feeling great, thanks for asking {user_name}! ^_^",
            "a bit tired, but im happy to chat with you! :3",
            "feeling awesome! how about you? :d",
            "im good! how are you doing {user_name}? ^-^"
        ],
        "thankful": [
            "aww, thanks a bunch! youre the best! ^-^",
            "thank you so much! <3",
            "hehe, thats so sweet of you to say! :3",
            "thanks, i appreciate it! ^-^"
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

    # Process message with basic NLP
    words = nlp_process(message)

    # Select appropriate template based on keywords
    for word in words:
        if word in keyword_responses:
            template = random.choice(keyword_responses[word])
            break
    else:
        template = random.choice(templates["general"])

    # Fill in template with dynamic content
    response = template.format(
        synonym1=get_synonym("cool"),
        synonym2=get_synonym("funny"),
        synonym3=get_synonym("sweet"),
        synonym4=get_synonym("interesting"),
        emoji=random.choice(emojis),
        user_name=context["user_name"]
    )

    # Randomize apostrophes and capitalization
    response = random_apostrophe(response)
    response = random_capitalize(response)

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
