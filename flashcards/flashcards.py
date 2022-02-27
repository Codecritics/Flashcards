import json
from random import choice


class TermAlreadyExists(Exception):
    def __init__(self, term):
        self.message = 'The term "%s" already exists.' % str(term)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class DefinitionAlreadyExists(Exception):
    def __init__(self, definition):
        self.message = 'The definition "%s" already exists.' % str(definition)
        super().__init__(self.message)

    def __str__(self):
        return self.message


class Flashcard:
    nb_flash_cards = 0
    flash_cards_dict = {}

    def __init__(self, term, definition):
        self.term = term
        self.definition = definition

    def __repr__(self):
        return f"Flashcard({self.term}, {self.definition})"

    def __str__(self):
        print_string = f"Card:\n{self.term}\nDefinition:\n{self.definition}"
        return print_string


def add_card():
    print("The card:")
    while True:
        try:
            tmp_term = input()
            if tmp_term in list(Flashcard.flash_cards_dict.keys()):
                raise TermAlreadyExists(tmp_term)
        except TermAlreadyExists as err:
            print(err, "Try again:", sep=' ')
        else:
            break

    print("The definition of the card:")
    while True:
        try:
            tmp_definition = input()
            if tmp_definition in list(Flashcard.flash_cards_dict.values()):
                raise DefinitionAlreadyExists(tmp_definition)
        except DefinitionAlreadyExists as err:
            print(err, "Try again:", sep=' ')
        else:
            break

    tmp_card = Flashcard(tmp_term, tmp_definition)
    tmp_card.flash_cards_dict[tmp_term] = tmp_definition
    print(f'The pair ("{tmp_term}":"{tmp_definition}") has been added.')
    print()


def remove_card():
    print("Which card?")
    card_term = input()

    if card_term in Flashcard.flash_cards_dict:
        del Flashcard.flash_cards_dict[card_term]
        print("The card has been removed.")
    else:
        print(f'Can\'t remove "{card_term}": there is no such card.')
    print()


def import_card():
    print("File name:")
    file_to_read = input()
    try:
        with open(file_to_read, 'r') as import_file:
            data = import_file.read()
    except FileNotFoundError:
        print("File not found.")
    else:
        cards = json.loads(data)
        for card in cards:
            Flashcard.flash_cards_dict[card] = cards[card]
        print(f"{len(cards)} cards have been loaded")


def export_card():
    print("File name:")
    file_to_write = input()

    with open(file_to_write, 'w') as export_file:
        export_file.write(json.dumps(Flashcard.flash_cards_dict))

    print(f"{len(Flashcard.flash_cards_dict)} cards have been saved")


def check_cards():
    print("How many times to ask?")
    nb_times_to_ask = input()
    if nb_times_to_ask.isdigit():
        nb_times_to_ask = int(nb_times_to_ask)

        flash_cards = Flashcard.flash_cards_dict
        definitions = list(flash_cards.values())
        terms = list(flash_cards.keys())

        for _ in range(nb_times_to_ask):
            term = choice(list(flash_cards))
            definition = flash_cards[term]

            print(f'Print the definition of "{term}":')
            temp_definition = input()
            if temp_definition == definition:
                print("Correct!")
            elif temp_definition in definitions:
                print(
                    f'Wrong. The right answer is "{definition}", but your definition is correct for "{terms[definitions.index(temp_definition)]}".')
            else:
                print(f'Wrong. The right answer is "{definition}".')
            print()
    return


def play():
    while True:
        print("Input the action (add, remove, import, export, ask, exit):")
        user_choice = input()
        if user_choice not in ["add", "remove", "import", "export", "ask", "exit"]:
            return play()
        if user_choice == "exit":
            print("Bye bye!")
            break
        elif user_choice == "add":
            add_card()
        elif user_choice == "remove":
            remove_card()
        elif user_choice == "export":
            export_card()
        elif user_choice == "import":
            import_card()
        elif user_choice == "ask":
            check_cards()


def main():
    play()


if __name__ == "__main__":
    main()
