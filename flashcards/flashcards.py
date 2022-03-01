import json
from collections import defaultdict
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
    flash_cards_dict = {}
    stats_cards_dict = defaultdict(int)

    def __init__(self, term: str, definition: str) -> None:
        self.term = term
        self.definition = definition

    def __repr__(self):
        return f"Flashcard({self.term}, {self.definition})"

    def __str__(self):
        print_string = f"Card:\n{self.term}\nDefinition:\n{self.definition}"
        return print_string


def add_card() -> None:
    global log_message

    card_msg = "The card:"
    print(card_msg)
    log_message += card_msg + "\n"
    while True:
        try:
            tmp_term = input()
            log_message += tmp_term + "\n"
            if tmp_term in list(Flashcard.flash_cards_dict.keys()):
                raise TermAlreadyExists(tmp_term)
        except TermAlreadyExists as err:
            print(err, "Try again:", sep=' ')
            log_message += f"{err} Try again:" "\n"
        else:
            break

    print("The definition of the card:")
    while True:
        try:
            tmp_definition = input()
            log_message += tmp_definition + "\n"
            if tmp_definition in list(Flashcard.flash_cards_dict.values()):
                raise DefinitionAlreadyExists(tmp_definition)
        except DefinitionAlreadyExists as err:
            print(err, "Try again:", sep=' ')
            log_message += f"{err} Try again:" "\n"
        else:
            break

    tmp_card = Flashcard(tmp_term, tmp_definition)
    tmp_card.flash_cards_dict[tmp_term] = tmp_definition

    added_msg = f'The pair ("{tmp_term}":"{tmp_definition}") has been added.'
    print(added_msg)
    log_message += added_msg + "\n \n"
    print()


def remove_card() -> None:
    global log_message

    card_msg = "Which card?"
    print(card_msg)
    log_message += card_msg + "\n"
    card_term = input()
    log_message += card_term + "\n"

    if card_term in Flashcard.flash_cards_dict:
        del Flashcard.flash_cards_dict[card_term]
        card_removed_msg = "The card has been removed."
        print(card_removed_msg)
        log_message += card_removed_msg + "\n \n"
    else:
        card_removed_error_msg = f'Can\'t remove "{card_term}": there is no such card.'
        print(card_removed_error_msg)
        log_message += card_removed_error_msg + "\n \n"
    print()


def import_card() -> None:
    global log_message

    file_msg = "File name:"
    print(file_msg)
    log_message += file_msg + "\n"

    file_to_read = input()
    log_message += file_to_read + "\n"
    try:
        with open(file_to_read, 'r') as import_file:
            data = import_file.read()
    except FileNotFoundError:
        file_msg_error = "File not found."
        print(file_msg_error)
        log_message += file_msg_error + "\n"
    else:
        cards = json.loads(data)
        for card in cards:
            Flashcard.flash_cards_dict[card] = cards[card]
        cards_loaded_msg = f"{len(cards)} cards have been loaded"
        print(cards_loaded_msg)
        log_message += cards_loaded_msg + "\n \n"


def export_card() -> None:
    global log_message

    file_msg = "File name:"
    print(file_msg)
    log_message += file_msg + "\n"

    file_to_write = input()
    log_message += file_to_write + "\n"

    with open(file_to_write, 'w') as export_file:
        export_file.write(json.dumps(Flashcard.flash_cards_dict))

    cards_saved_msg = f"{len(Flashcard.flash_cards_dict)} cards have been saved"
    print(cards_saved_msg)
    log_message += cards_saved_msg + "\n \n"
    print()


def check_cards() -> None:
    global log_message

    ask_msg = "How many times to ask?"
    print(ask_msg)
    log_message += ask_msg + "\n"

    nb_times_to_ask = input()
    log_message += nb_times_to_ask + "\n"

    if nb_times_to_ask.isdigit():
        nb_times_to_ask = int(nb_times_to_ask)

        flash_cards = Flashcard.flash_cards_dict
        definitions = list(flash_cards.values())
        terms = list(flash_cards.keys())

        for _ in range(nb_times_to_ask):
            term = choice(list(flash_cards))
            definition = flash_cards[term]

            definition_msg = f'Print the definition of "{term}":'
            print(definition_msg)
            log_message += definition_msg + "\n"

            temp_definition = input()
            log_message += temp_definition + "\n"

            if temp_definition == definition:
                good_answer_msg = "Correct!"
                print(good_answer_msg)
                log_message += good_answer_msg + "\n \n"

            elif temp_definition in definitions:
                Flashcard.stats_cards_dict[term] += 1
                wrong_answer1_msg = f'Wrong. The right answer is "{definition}", but your definition is correct for "{terms[definitions.index(temp_definition)]}".'
                print(wrong_answer1_msg)
                log_message += wrong_answer1_msg + "\n \n"
            else:
                Flashcard.stats_cards_dict[term] += 1
                wrong_answer2_msg = f'Wrong. The right answer is "{definition}".'
                print(wrong_answer2_msg)
                log_message += wrong_answer2_msg + "\n \n"
            print()
    return


def log() -> None:
    global log_message

    file_msg = 'File name:'
    print(file_msg)
    log_message += file_msg + "\n"
    log_file = input()
    log_message += log_file + "\n"
    with open(log_file, 'w') as file:
        file.write(log_message)
    log_success_msg = "The log has been saved."
    print(log_success_msg)
    print()


def hardest_card() -> None:
    global log_message

    stats = Flashcard.stats_cards_dict
    no_hardest_card_msg = "There are no cards with errors."
    if len(stats) == 0:
        print(no_hardest_card_msg)
        log_message += no_hardest_card_msg + "\n"
        return
    stat = list(stats.keys())
    stat_values = list(stats.values())
    maximum = max(stat_values)
    maximum_terms = [stat[key] for (key, value) in enumerate(stat_values) if value == maximum]
    if maximum == 0:
        print(no_hardest_card_msg)
        log_message += no_hardest_card_msg + "\n \n"
        return

    if len(maximum_terms) == 1:
        no_hardest_card_msg1 = f'The hardest card is "{maximum_terms[0]}". You have {maximum} errors answering it'
        print(no_hardest_card_msg1)
        log_message += no_hardest_card_msg1 + "\n \n"
    elif len(maximum_terms) > 2:
        terms = ""

        for term in maximum_terms:
            terms += f' "{term}"'

        no_hardest_card_msg2 = f"The hardest cards are{terms}"
        print(no_hardest_card_msg2)
        log_message += no_hardest_card_msg2 + "\n \n"
    print()
    return


def reset_stats() -> None:
    global log_message

    stats = Flashcard.stats_cards_dict

    for stat in stats:
        stats[stat] = 0

    reset_msg = "Card statistics have been reset."
    print(reset_msg)
    log_message += reset_msg + "\n \n"

    print()


def play() -> None:
    global log_message

    while True:
        menu_msg = "Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):"
        print(menu_msg)
        log_message += menu_msg + "\n"
        user_choice = input()
        log_message += user_choice + "\n"

        if user_choice not in ["add", "remove", "import", "export", "ask", "exit", "log", "hardest card",
                               "reset stats"]:
            return play()
        if user_choice == "exit":
            exit_msg = "Bye bye!"
            print(exit_msg)
            log_message += exit_msg + "\n"
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
        elif user_choice == "log":
            log()
        elif user_choice == "hardest card":
            hardest_card()
        elif user_choice == "reset stats":
            reset_stats()


log_message = ""


def main():
    play()


if __name__ == "__main__":
    main()
