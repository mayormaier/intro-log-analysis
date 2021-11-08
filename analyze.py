# ANDREW MAIER ADM5859 LOG ANALYSIS

with open("Log-A.strace", "r") as log_a, open("Log-B.strace", "r") as log_b:
    a_content = log_a.readlines()
    b_content = log_b.readlines()

    # Task 1
    read_expression = " read("
    count = 0
    for line in a_content:
        if read_expression in line:
            print("Read from Log A: " + line)
            count += 1
    print(str(count) + " read events in Log A")

    count = 0
    for line in b_content:
        if read_expression in line:
            print("Read from Log B: " + line)
            count += 1
    print(str(count) + " read events in Log B")

    # Task 2
    keyboard_expression = "tty"
    count = 0
    for line in a_content:
        if read_expression in line and keyboard_expression in line:
            print("Keyboard Read Event from Log A: " + line)
            count += 1
    print(str(count) + " keyboard read events in Log A")

    count = 0
    for line in b_content:
        if read_expression in line and keyboard_expression in line:
            print("Keyboard Read Event from Log B: " + line)
            count += 1
    print(str(count) + " keyboard read events in Log B")

    # Task 3
    pipe_expression = "pipe"
    count = 0
    for line in a_content:
        if read_expression in line and keyboard_expression not in line and pipe_expression not in line:
            print("File read event from Log A: " + line)
            count += 1
    print(str(count) + " file read events in Log A")

    count = 0
    for line in b_content:
        if read_expression in line and keyboard_expression not in line and pipe_expression not in line:
            print("File read event from Log B: " + line)
            count += 1
    print(str(count) + " file read events in Log B")
