class Flashcard:
    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __repr__(self):
        return f"Flashcard({self.term}, {self.definition})"

    def __str__(self):
        print_string = f"Card:\n{self.term}\nDefinition:\n{self.definition}"
        return print_string


def main():
    card = Flashcard("purchase", "buy")
    print(card)


if __name__ == "__main__":
    main()
