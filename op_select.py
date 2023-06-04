
import op_modes
from Speech import convert_speech_text


def operation_mode_select():

    while True:
        print("Please select a operatıon mode: \n"
              "1. repetition mode  \n"
              "2. randomized repetition mode  \n"
              "3. sequence mode  \n"
              "4. randomized sequence mode  \n"
              "5. game mode")

        # recognize speech using google
        user_speech = convert_speech_text()

        if (user_speech == "repetition mode"):
            print("repetiton_mode is activated")
            user_input = op_modes.repetition_mode()
            number_of_throw = op_modes.get_throw_count()
            for count in range(number_of_throw):
                op_modes.system_input(user_input)
                # wait MZ 80 for acknowledge
            break

        elif (user_speech == "randomized repetition mode"):
            print("random_repetiton_mode")
            user_input = op_modes.repetition_mode()
            number_of_throw = op_modes.get_throw_count()
            for count in range(number_of_throw):
                random_list = op_modes.randomizer(user_input)
                op_modes.system_input(random_list)
                # wait MZ 80 for acknowledge
            break

        elif (user_speech == "sequence mode"):
            print("sequence_mode is activated")
            while True:
                print("Select sequence source: verbal / written")  # verbal , written
                seq_source = convert_speech_text()
                if seq_source in ("verbal", "written"):  # check if user input is valid
                    break
                else:
                    print("Input is not valid, Try Again!")

            if seq_source == "verbal":
                user_sequence = op_modes.sequence_verbal_mode()
                for throw_parameters in user_sequence:
                    op_modes.system_input(throw_parameters)
                    # MZ 80 wait
                break
            else:
                pass                # a function getting list from GUI
                #user_sequence =

        elif (user_speech == "randomized sequence mode"):
            print("random_sequence_mode is activated")
            while True:
                print("Select sequence source: verbal / written")  # verbal , written
                seq_source = convert_speech_text()
                if seq_source in ("verbal", "written"):  # check if user input is valid
                    break
                else:
                    print("Input is not valid, Try Again!")

            if seq_source == "verbal":
                user_sequence = op_modes.sequence_verbal_mode()
                for throw_parameters in user_sequence:
                    random_list = op_modes.randomizer(throw_parameters)
                    op_modes.system_input(random_list)
                    # wait MZ 80 for acknowledge
                break
            else:
                pass                # a function getting list from GUI
                # user_sequence =

            break

        elif (user_speech == "game mode"):
            print("game_mode is activated")
            op_modes.game_mode()
            #op_modes.game_mode()
            break

        else:
            print("Not a valid mode !")
