# ANDREW MAIER ADM5859 LOG ANALYSIS

with open("Log-A.strace", "r") as log_a, open("Log-B.strace", "r") as log_b:
    a_content = log_a.readlines()
    b_content = log_b.readlines()

    # Task 1
    read_expression = " read("
    count = 0
    for line in a_content:
        if read_expression in line:
            print("Read event from Log A: " + line)
            count += 1
    a_read_events_count = count

    count = 0
    for line in b_content:
        if read_expression in line:
            print("Read event from Log B: " + line)
            count += 1
    b_read_events_count = count

    # Task 2
    keyboard_expression = "tty"
    count = 0
    for line in a_content:
        if read_expression in line and keyboard_expression in line:
            print("Keyboard Read Event from Log A: " + line)
            count += 1
    a_keyboard_read_events_count = count

    count = 0
    for line in b_content:
        if read_expression in line and keyboard_expression in line:
            print("Keyboard Read Event from Log B: " + line)
            count += 1
    b_keyboard_read_events_count = count

    # Task 3
    pipe_expression = "pipe"
    count = 0
    for line in a_content:
        if read_expression in line and keyboard_expression not in line and pipe_expression not in line:
            print("File read event from Log A: " + line)
            count += 1
    a_file_read_events_count = count

    count = 0
    for line in b_content:
        if read_expression in line and keyboard_expression not in line and pipe_expression not in line:
            print("File read event from Log B: " + line)
            count += 1
    b_file_events_count = count

    print(str(a_read_events_count) + " read events in Log A")
    print(str(b_read_events_count) + " read events in Log B")
    print(str(a_keyboard_read_events_count) + " keyboard read events in Log A")
    print(str(b_keyboard_read_events_count) + " keyboard read events in Log B")
    print(str(a_file_read_events_count) + " file read events in Log A")
    print(str(b_file_events_count) + " file read events in Log B")
