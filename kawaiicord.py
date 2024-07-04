# File: DiscoEgirl.py
import random
import click

# Context and memory for conversation
context = {
    "previous_message": "",
    "user_name": "User",
    "mood": "happy"
}

def update_mood():
    moods = ["happy", "playful", "teasing", "curious", "friendly"]
    context["mood"] = random.choice(moods)

def get_synonym(word):
    synonyms = {
        "cool": ["awesome", "amazing", "fantastic"],
        "funny": ["hilarious", "lol-worthy", "amusing"],
        "sweet": ["adorable", "cute", "lovely"],
        "interesting": ["fascinating", "intriguing", "captivating"]
    }
    return random.choice(synonyms.get(word, [word]))

def generate_response(message):
    # Update mood occasionally
    if random.random() < 0.3:
        update_mood()

    # Lowercase message for easier keyword matching
    message_lower = message.lower()
    context["previous_message"] = message

    # Response templates
    templates = {
        "general": [
            "Omg, that's {synonym1}! {emoji}",
            "Haha, you're {synonym2}! {emoji}",
            "Aww, you're so {synonym3}! {emoji}",
            "Lol, I totally agree! {emoji}",
            "Hehe, you're making me blush! {emoji}",
            "Oh wow, tell me more! {emoji}",
            "Eee, that's so {synonym4}! {emoji}",
            "Hehe, you're the best! {emoji}",
            "Aww, you're adorable! {emoji}",
            "Haha, you're making me giggle! {emoji}"
        ],
        "greeting": [
            "Hii {user_name}! How are you? ^-^",
            "Heyyy {user_name}! What's up? :3",
            "Hello there! How's it going? UwU",
            "Hiya! Hope you're having a great day! ^_^"
        ],
        "love": [
            "Aww, love you too {user_name}! <3",
            "You're the best! Mwah! :*",
            "Hehe, you're making my heart melt! >///<",
            "Love you lots {user_name}! ^-^"
        ],
        "game": [
            "Ohh, what games do you play {user_name}? :3",
            "Gaming is life! What are your favorites? xD",
            "I love games too! Let's play together sometime! ^-^",
            "What's your top game right now? *-*"
        ],
        "compliment": [
            "Aww, thank you {user_name}! You're so sweet! ^-^",
            "Hehe, you're making me blush! >///<",
            "You're too kind {user_name}! <3",
            "Thanks a lot! You're amazing too! :3"
        ],
        "feeling": [
            "I'm feeling great, thanks for asking {user_name}! ^_^",
            "A bit tired, but I'm happy to chat with you! :3",
            "Feeling awesome! How about you? :D",
            "I'm good! How are you doing {user_name}? ^-^"
        ]
    }

    # Emoji and decoration options
    emojis = ["^-^", ":3", "UwU", "xD", ">///<", "*-*", "^_^", "n_n", "<3", ":D"]

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
        "how are you": templates["feeling"]
    }

    # Select appropriate template
    for keyword, responses in keyword_responses.items():
        if keyword in message_lower:
            template = random.choice(responses)
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

    return response

@click.command()
@click.option('--message', prompt='Enter your message', help='The message you want to send to the e-girl.')
@click.option('--name', default='User', help='Your name for a personalized experience.')
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
