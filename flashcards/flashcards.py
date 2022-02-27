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


def set_of_cards():
    print("Input the number of cards:")
    Flashcard.nb_flash_cards = int(input())

    for i in range(1, Flashcard.nb_flash_cards + 1):

        print(f"The term for card #{i}:")
        while True:
            try:
                tmp_term = input()
                if tmp_term in list(Flashcard.flash_cards_dict.keys()):
                    raise TermAlreadyExists(tmp_term)
            except TermAlreadyExists as err:
                print(err, "Try again:", sep=' ')
            else:
                break

        print(f"The definition for card #{i}:")
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
    return


def check_set_of_cards():
    flash_cards = Flashcard.flash_cards_dict
    definitions = list(flash_cards.values())
    terms = list(flash_cards.keys())
    for (term, definition) in flash_cards.items():
        print(f'Print the definition of "{term}":')
        temp_definition = input()
        if temp_definition == definition:
            print("Correct!")
        elif temp_definition in definitions:
            print(
                f'Wrong. The right answer is "{definition}", but your definition is correct for "{terms[definitions.index(temp_definition)]}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')
    return


def main():
    set_of_cards()
    check_set_of_cards()


if __name__ == "__main__":
    main()
