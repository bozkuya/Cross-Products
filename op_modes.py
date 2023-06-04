
import time
import random
from Speech import convert_speech_text
from word2number import w2n
from numeric_string import check

# arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)

speed_translate = {'low': 50, 'medium': 75,'high': 100}
spin_type_translate = {'game': 1, 'Google': -1}
spin_intensity_translate = {'low': 50, 'medium': 100, 'high': 150}
direction_translate = {'left': -15, 'middle': 0, 'right': 15}
height_translate = {'low': 40, 'medium': 50, 'high': 60}  # pan tilt default offset exists
loader_translate = {'low': 50, 'medium': 150, 'high': 250}

def system_input(input_list):

    for input in input_list:
        # arduino.write(bytes(input, 'utf-8'))
        print(str(input))
        time.sleep(0.05)

    # MZ 80 check for throw


def repetition_mode():

    print("Parameters are required ... ")
    # ball speed, spin type, spin intensity, direction, height, loader speed(difficulty), times

                            #we are THE launcher - from the launcher perspective
    input_list = []         # motor side, motor bottom, servo horizontal, servo vertical, motor loader

    while True:
        print("Provide ball speed: low / medium / high")  # low, medium, high
        speed_text = convert_speech_text()
        if speed_text in ("low","medium","high"): # check if user input is valid
            break
        else:
            print("Input is not valid, Try Again!")

    while True:
        print("Provide ball spin type: game / Google")  # top, back
        spin_text = convert_speech_text()
        if spin_text in ("game","Google"): # check if user input is valid
            break
        else:
            print("Input is not valid, Try Again!")

    while True:
        print("Provide ball spin intensity: low / medium / high")  # low, medium, high
        intensity_text = convert_speech_text()
        if intensity_text in ("low","medium","high"): # check if user input is valid
            break
        else:
            print("Input is not valid, Try Again!")

    while True:
        print("Provide throw direction: left / middle / right")  # left, middle, right
        direction_text = convert_speech_text()
        if direction_text in ("left", "middle", "right"):  # check if user input is valid
            break
        else:
            print("Input is not valid, Try Again!")

    while True:
        print("Provide throw height: low / medium / high")  # low, medium, high
        height_text = convert_speech_text()
        if height_text in ("low", "medium", "high"):  # check if user input is valid
            break
        else:
            print("Input is not valid, Try Again!")

    while True:
        print("Choose difficulty level: low / medium / high")  # low, medium, high
        difficulty_text = convert_speech_text()
        if difficulty_text in ("low", "medium", "high"):  # check if user input is valid
            break
        else:
            print("Input is not valid, Try Again!")

    # top motors no spin assumed
    motor_side_input = speed_translate[speed_text] + spin_intensity_translate[intensity_text] * spin_type_translate[spin_text]
    if motor_side_input < 50:
        motor_side_input = 50
    elif motor_side_input > 255:
        motor_side_input = 255
    input_list.append(motor_side_input)

    motor_bottom_input = speed_translate[speed_text] + spin_intensity_translate[intensity_text] * (-1) * spin_type_translate[spin_text]
    if motor_bottom_input < 50:
        motor_bottom_input = 50
    elif motor_bottom_input > 255:
        motor_bottom_input = 255
    input_list.append(motor_bottom_input)

    servo_hor_input = direction_translate[direction_text]
    input_list.append(servo_hor_input)

    servo_ver_input = height_translate[height_text]
    input_list.append(servo_ver_input)

    motor_loader_input = loader_translate[difficulty_text]
    input_list.append(motor_loader_input)

    return input_list

def randomizer(list_to_random):

    r_side = int(random.uniform(-20, 20))
    r_bottom = int(random.uniform(-20, 20))
    r_servo_hor = int(random.uniform(-3, 3))
    r_servo_ver = int(random.uniform(-5, 5))
    r_loader = 0        # loader speed is NOT randomized

    list_to_random[0] += r_side
    list_to_random[1] += r_bottom
    list_to_random[2] += r_servo_hor
    list_to_random[3] += r_servo_ver
    list_to_random[4] += r_loader

    return list_to_random


def sequence_verbal_mode():

    sequence_count = get_throw_count()

    sequence_throw_list = []
    for times in range(sequence_count):
        one_throw_info = repetition_mode()
        sequence_throw_list.append(one_throw_info)

    return sequence_throw_list


def game_mode():

    # if file exists:
        # load_last_100()
    #else:
    generated_data_sample = generate_last_100()

    match_count = get_throw_count()

    for k in range(match_count):

        ball_speed_low = 0
        ball_speed_low_fail = 0
        ball_speed_medium = 0
        ball_speed_medium_fail = 0
        ball_speed_high = 0
        ball_speed_high_fail = 0

        spin_type_top = 0
        spin_type_top_fail = 0
        spin_type_back = 0
        spin_type_back_fail = 0

        spin_intensity_low = 0
        spin_intensity_low_fail = 0
        spin_intensity_medium = 0
        spin_intensity_medium_fail = 0
        spin_intensity_high = 0
        spin_intensity_high_fail = 0

        direction_left = 0
        direction_left_fail = 0
        direction_middle = 0
        direction_middle_fail = 0
        direction_right = 0
        direction_right_fail = 0

        height_low = 0
        height_low_fail = 0
        height_medium = 0
        height_medium_fail = 0
        height_high = 0
        height_high_fail = 0


        last_100_throws = generated_data_sample

        for throw_index, current_throw in enumerate(last_100_throws):

            recency_coeff = int(throw_index / 20) + 1
            # print("bu coeff: " +  str(recency_coeff))
    # ***************************************************

            if current_throw[1][0] == 50:
                ball_speed_low += recency_coeff
                if current_throw[0] is False:
                    ball_speed_low_fail += recency_coeff

            if current_throw[1][0] == 75:
                ball_speed_medium += recency_coeff
                if current_throw[0] is False:
                    ball_speed_medium_fail += recency_coeff

            if current_throw[1][0] == 100:
                ball_speed_high += recency_coeff
                if current_throw[0] is False:
                    ball_speed_high_fail += recency_coeff

    # **********************************************************

            if current_throw[1][1] == 1:
                spin_type_top += recency_coeff
                if current_throw[0] is False:
                    spin_type_top_fail += recency_coeff

            if current_throw[1][1] == -1:
                spin_type_back += recency_coeff
                if current_throw[0] is False:
                    spin_type_back_fail += recency_coeff

    # ***********************************************************

            if current_throw[1][2] == 50:
                spin_intensity_low += recency_coeff
                if current_throw[0] is False:
                    spin_intensity_low_fail += recency_coeff

            if current_throw[1][2] == 100:
                spin_intensity_medium += recency_coeff
                if current_throw[0] is False:
                    spin_intensity_medium_fail += recency_coeff

            if current_throw[1][2] == 150:
                spin_intensity_high += recency_coeff
                if current_throw[0] is False:
                    spin_intensity_high_fail += recency_coeff

    # *************************************************************

            if current_throw[1][3] == -15:
                direction_left += recency_coeff
                if current_throw[0] is False:
                    direction_left_fail += recency_coeff

            if current_throw[1][3] == 0:
                direction_middle += recency_coeff
                if current_throw[0] is False:
                    direction_middle_fail += recency_coeff

            if current_throw[1][3] == 15:
                direction_right += recency_coeff
                if current_throw[0] is False:
                    direction_right_fail += recency_coeff

    # ***************************************************************

            if current_throw[1][4] == 40:
                height_low += recency_coeff
                if current_throw[0] is False:
                    height_low_fail += recency_coeff

            if current_throw[1][4] == 50:
                height_medium += recency_coeff
                if current_throw[0] is False:
                    height_medium_fail += recency_coeff

            if current_throw[1][4] == 60:
                height_high += recency_coeff
                if current_throw[0] is False:
                    height_high_fail += recency_coeff

    # ****************************************************************

        # calculating the ratios

        ball_speed_low_fail_rate = ball_speed_low_fail / ball_speed_low
        ball_speed_medium_fail_rate = ball_speed_medium_fail / ball_speed_medium
        ball_speed_high_fail_rate = ball_speed_high_fail / ball_speed_high

        ball_speed_fail_exclude_high = ball_speed_low_fail_rate + ball_speed_medium_fail_rate
        ball_speed_fail_total = ball_speed_low_fail_rate + ball_speed_medium_fail_rate + ball_speed_high_fail_rate

        spin_type_top_fail_rate = spin_type_top_fail / spin_type_top
        spin_type_back_fail_rate = spin_type_back_fail / spin_type_back
        spin_type_fail_total = spin_type_top_fail_rate + spin_type_back_fail_rate

        spin_intensity_low_fail_rate = spin_intensity_low_fail / spin_intensity_low
        spin_intensity_medium_fail_rate = spin_intensity_medium_fail / spin_intensity_medium
        spin_intensity_high_fail_rate = spin_intensity_high_fail / spin_intensity_high

        spin_intensity_fail_exclude_high = spin_intensity_low_fail_rate + spin_intensity_medium_fail_rate
        spin_intensity_fail_total = spin_intensity_low_fail_rate + spin_intensity_medium_fail_rate + spin_intensity_high_fail_rate

        direction_left_fail_rate = direction_left_fail / direction_left
        direction_middle_fail_rate = direction_middle_fail / direction_middle
        direction_right_fail_rate = direction_right_fail / direction_right

        direction_fail_exclude_right = direction_left_fail_rate + direction_middle_fail_rate
        direction_fail_total = direction_left_fail_rate + direction_middle_fail_rate + direction_right_fail_rate

        height_low_fail_rate = height_low_fail / height_low
        height_medium_fail_rate = height_medium_fail / height_medium
        height_high_fail_rate = height_high_fail / height_high

        height_fail_exclude_high = height_low_fail_rate + height_medium_fail_rate
        height_fail_total = height_low_fail_rate + height_medium_fail_rate + height_high_fail_rate

    # *********************************************************************************

    #       Calculate the boundaries

        ball_speed_bottom_boundary = (ball_speed_low_fail / ball_speed_fail_total) * 100
        ball_speed_top_boundary = (ball_speed_fail_exclude_high / ball_speed_fail_total) * 100

        spin_type_boundary = (spin_type_top_fail / spin_type_fail_total) * 100

        spin_intensity_bottom_boundary = (spin_intensity_low_fail_rate / spin_intensity_fail_total) * 100
        spin_intensity_top_boundary = (spin_intensity_fail_exclude_high / spin_intensity_fail_total) * 100

        direction_bottom_boundary = (direction_left_fail_rate / direction_fail_total) * 100
        direction_top_boundary = (direction_fail_exclude_right / direction_fail_total) * 100

        height_bottom_boundary = (height_low_fail_rate / height_fail_total) * 100
        height_top_boundary = (height_fail_exclude_high / height_fail_total) * 100

    # *********************************************************************************************

        new_throw_record = []

        random_for_ball_speed = random.randint(0,100)
        if random_for_ball_speed < ball_speed_bottom_boundary:
            new_ball_speed = 50
        elif random_for_ball_speed < ball_speed_top_boundary:
            new_ball_speed = 75
        else:
            new_ball_speed = 100

        new_throw_record.append(new_ball_speed)

        random_for_spin_type = random.randint(0, 100)
        if random_for_spin_type < spin_type_boundary:
            new_ball_spin_type = 1
        else:
            new_ball_spin_type = -1

        new_throw_record.append(new_ball_spin_type)

        random_for_spin_intensity = random.randint(0, 100)
        if random_for_spin_intensity < spin_intensity_bottom_boundary:
            new_spin_intensity = 50
        elif random_for_spin_intensity < spin_intensity_top_boundary:
            new_spin_intensity = 100
        else:
            new_spin_intensity = 150

        new_throw_record.append(new_spin_intensity)

        random_for_direction = random.randint(0, 100)
        if random_for_direction < direction_bottom_boundary:
            new_direction = -15
        elif random_for_direction < direction_top_boundary:
            new_direction = 0
        else:
            new_direction = 15

        new_throw_record.append(new_direction)

        random_for_height = random.randint(0, 100)
        if random_for_height < height_bottom_boundary :
            new_height = 40
        elif random_for_height < height_top_boundary:
            new_height = 50
        else:
            new_height = 60

        new_throw_record.append(new_height)

        new_input_arduino = []         # this includes arduino inputs

        motor_side_input = new_ball_speed + new_spin_intensity * new_ball_spin_type
        if motor_side_input < 50:
            motor_side_input = 50
        elif motor_side_input > 255:
            motor_side_input = 255
        new_input_arduino.append(motor_side_input)

        motor_bottom_input = new_ball_speed + new_spin_intensity * (-1) * new_ball_spin_type
        if motor_bottom_input < 50:
            motor_bottom_input = 50
        elif motor_bottom_input > 255:
            motor_bottom_input = 255
        new_input_arduino.append(motor_bottom_input)

        new_input_arduino.append(new_direction)
        new_input_arduino.append(new_height)
        new_input_arduino.append("150")             # constant loader speed

        system_input(new_input_arduino)
        # MZ 80 is ball launched
        # wait for success / fail

        deneme_success = random.randint(0,1)

        if deneme_success == 1:
            debug_bool = True
        else:
            debug_bool = False

        throw_status = debug_bool         # This will be return of user succes / fail

        generated_throw_with_status = []

        generated_throw_with_status.append(throw_status)
        generated_throw_with_status.append(new_throw_record)

        last_100_throws.append(generated_throw_with_status)
        last_100_throws.pop(0)






def generate_last_100():

    last_100_throws = []

    for k in range(100):
        generated_throw = []
        throw_with_succes = []

        speed_convert = {0: speed_translate["low"], 1: speed_translate["medium"], 2: speed_translate["high"]}
        spin_type_convert = {0: spin_type_translate["game"], 1: spin_type_translate["Google"]}
        spin_intensity_convert = {0: spin_intensity_translate["low"], 1: spin_intensity_translate["medium"], 2: spin_intensity_translate["high"]}
        direction_convert = {0: direction_translate["left"], 1: direction_translate["middle"], 2: direction_translate["right"]}
        height_convert = {0: height_translate["low"], 1: height_translate["medium"], 2: height_translate["high"]}

        rand_speed_index = random.randint(0,2)
        rand_spin_type_index = random.randint(0, 1)
        rand_spin_intensity_index = random.randint(0, 2)
        rand_direction_index = random.randint(0, 2)
        rand_height_index = random.randint(0, 2)

        generated_throw.append(speed_convert[rand_speed_index])
        generated_throw.append(spin_type_convert[rand_spin_type_index])
        generated_throw.append(spin_intensity_convert[rand_spin_intensity_index])
        generated_throw.append(direction_convert[rand_direction_index])
        generated_throw.append(height_convert[rand_height_index])

        rand_success = random.randint(0, 1)

        if rand_success == 1:
            parameter_successes = True
        else:
            parameter_successes = False

        throw_with_succes.append(parameter_successes)
        throw_with_succes.append(generated_throw)

        last_100_throws.append(throw_with_succes)

    with open('last_100_throws.txt', 'r+') as file:
        from_file = []
        for each_throw in last_100_throws:
            file.writelines(str(each_throw[0]) + " " + str(each_throw[1]) + "\n")

            from_file.append(file.readline())
        print(from_file)


    return last_100_throws







def load_last_100():
    pass




def get_throw_count():
    while True:
        print("Provide number of throws")  # low, medium, high
        count = convert_speech_text()

        if check(count):
            return int(count)

        else:
            while True:
                try:
                    range = w2n.word_to_num(count)
                    return range

                except Exception as e:
                    print("Error :  " + str(e))
                    break




