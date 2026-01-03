"""OOP greetings demo: inheritance and polymorphism.

This file shows a simple base `Greeter` class and two subclasses
`Goodbye` and `Postcard` that override or extend behavior.
Designed for beginners: no dataclasses, clear methods and docstrings.
"""


class Greeter:
    """Base greeter class storing a name and providing `greet()`.

    Subclasses can override `greet()` to change behavior.
    """

    def __init__(self, name, excited=False):
        self.name = name
        self.excited = excited

    def greet(self, lang='en'):
        """Return a greeting string in the requested language.

        Args:
            lang: Two-letter language code; supports 'en', 'es', 'fr'.
        """

        if lang == 'es':
            base = f"Hola, {self.name}"
        elif lang == 'fr':
            base = f"Bonjour, {self.name}"
        else:
            base = f"Hello, {self.name}"

        return base + ('!' if self.excited else '.')


class Goodbye(Greeter):
    """A greeter that says goodbye instead of hello.

    Demonstrates overriding a parent method.
    """

    def greet(self, lang='en'):
        if lang == 'es':
            base = f"Adiós, {self.name}"
        elif lang == 'fr':
            base = f"Au revoir, {self.name}"
        else:
            base = f"Goodbye, {self.name}"

        return base + ('!' if self.excited else '.')


class Postcard(Greeter):
    """A greeter that can produce a postcard-style message.

    Shows how subclasses can add new methods/fields.
    """

    def __init__(self, name, excited=False, location='a lovely place'):
        super().__init__(name, excited=excited)
        self.location = location

    def greet(self, lang='en'):
        # Keep greet short and postcard-friendly
        if lang == 'es':
            base = f"Saludos, {self.name}"
        elif lang == 'fr':
            base = f"Salutations, {self.name}"
        else:
            base = f"Greetings, {self.name}"

        return base + ('!' if self.excited else '.')

    def send_postcard(self, sender):
        """Return a postcard message from `sender` to this greeter.

        Demonstrates an added method unique to the subclass.
        """

        return (
            f"Dear {self.name},\n"
            f"Having a great time in {self.location}.\n"
            f"Wish you were here!\n\n"
            f"— {sender}"
        )


def main():
    # create instances
    g = Greeter('Alex')
    bye = Goodbye('Sam', excited=True)
    pc = Postcard('Riley', location='Paris')

    # demonstrate polymorphism: same call, different behavior
    for obj in (g, bye, pc):
        print(type(obj).__name__, 'says:', obj.greet())

    # Postcard-specific behavior
    print('\nPostcard content:')
    print(pc.send_postcard('Taylor'))


if __name__ == '__main__':
    main()
