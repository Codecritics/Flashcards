class Flashcard:
    nb_flash_cards = 0
    lst_flash_cards = []

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
        tmp_term = input()
        print(f"The definition for card #{i}:")
        tmp_definition = input()

        tmp_card = Flashcard(tmp_term, tmp_definition)
        tmp_card.lst_flash_cards.append(tmp_card)
    return


def check_set_of_cards():
    for i in range(len(Flashcard.lst_flash_cards)):
        curr_card = Flashcard.lst_flash_cards[i]
        print(f'Print the definition of "{curr_card.term}":')
        temp_definition = input()
        if temp_definition == curr_card.definition:
            print("Correct!")
        else:
            print(f'Wrong. The right answer is "f{curr_card.definition}".')
    return


def main():
    set_of_cards()
    check_set_of_cards()


if __name__ == "__main__":
    main()
