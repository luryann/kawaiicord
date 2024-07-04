# File: egirl_cli.py
import random
import click

@click.command()
@click.option('--message', prompt='Enter your message', help='The message you want to send to the e-girl.')
def chat(message):
    """
    CLI application to chat with an e-girl bot on Discord using predefined rules and templates.
    """
    try:
        response = generate_response(message)
        click.echo(f"E-girl: {response}")
    except Exception as e:
        click.echo(f"Error: {e}")

def generate_response(message):
    """
    Generate a response based on predefined rules and templates to emulate e-girl lingo.
    """
    # Lowercase message for easier keyword matching
    message_lower = message.lower()

    # General responses
    general_responses = [
        "Omg, that's so cool! ^-^",
        "Haha, you're funny! :3",
        "Aww, you're so sweet! UwU",
        "Lol, I totally agree! xD",
        "Hehe, you're making me blush! >///<",
        "Oh wow, tell me more! *-*",
        "Eee, that's so interesting! ^_^",
        "Hehe, you're the best! n_n",
        "Aww, you're adorable! <3",
        "Haha, you're making me giggle! :D"
    ]

    # Responses for greetings
    greeting_responses = [
        "Hii! How are you? ^-^",
        "Heyyy! What's up? :3",
        "Hello there! How's it going? UwU",
        "Hiya! Hope you're having a great day! ^_^"
    ]

    # Responses for love and affection
    love_responses = [
        "Aww, love you too! <3",
        "You're the best! Mwah! :*",
        "Hehe, you're making my heart melt! >///<",
        "Love you lots! ^-^"
    ]

    # Responses for games
    game_responses = [
        "Ohh, what games do you play? :3",
        "Gaming is life! What are your favorites? xD",
        "I love games too! Let's play together sometime! ^-^",
        "What's your top game right now? *-*"
    ]

    # Responses for compliments
    compliment_responses = [
        "Aww, thank you! You're so sweet! ^-^",
        "Hehe, you're making me blush! >///<",
        "You're too kind! <3",
        "Thanks a lot! You're amazing too! :3"
    ]

    # Responses for feeling
    feeling_responses = [
        "I'm feeling great, thanks for asking! ^_^",
        "A bit tired, but I'm happy to chat with you! :3",
        "Feeling awesome! How about you? :D",
        "I'm good! How are you doing? ^-^"
    ]

    # Responses based on keywords
    keyword_responses = {
        "hello": greeting_responses,
        "hi": greeting_responses,
        "hey": greeting_responses,
        "love": love_responses,
        "game": game_responses,
        "games": game_responses,
        "beautiful": compliment_responses,
        "pretty": compliment_responses,
        "cute": compliment_responses,
        "feeling": feeling_responses,
        "how are you": feeling_responses
    }

    # Check for keywords in the message and select appropriate responses
    for keyword, responses in keyword_responses.items():
        if keyword in message_lower:
            return random.choice(responses)

    # Default to general responses if no specific keyword is found
    return random.choice(general_responses)

if __name__ == '__main__':
    chat()
