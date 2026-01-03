"""A tiny, self-contained demo showing variables, conditionals,
and classes in a friendly "hello world" style.

Run this file directly to see example output.
"""


class Greeter:
    """Simple greeter demonstrating a class with state.

    Attributes:
        name: The name to greet.
        excited: Whether the greeting is excited.
    """

    def __init__(self, name, excited=False):
        self.name = name
        self.excited = excited

    def greet(self, lang='en'):
        """Return a greeting in the requested language.

        Includes a conditional to vary punctuation based on ``excited``.
        """

        if lang == 'es':
            base = f"Hola, {self.name}"
        elif lang == 'fr':
            base = f"Bonjour, {self.name}"
        else:
            base = f"Hello, {self.name}"

        if self.excited:
            return base + "!"
        return base + "."


def main(name=None):
    # variable examples
    user = name or "World"
    enthusiasm = True  # change to False to see the calmer greeting

    # create a class instance using variables above
    greeter = Greeter(user, excited=enthusiasm)

    # conditional example (ternary-like)
    mood = ";)" if enthusiasm else ""

    print(greeter.greet())         # default (English)
    print(greeter.greet('es'))     # Spanish
    print(greeter.greet('fr'))     # French
    print(f"Signed: {user} {mood}")


if __name__ == "__main__":
    main()
