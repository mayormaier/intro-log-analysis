# ANDREW MAIER ADM5859 LOG ANALYSIS

with open("Log-A.strace", "r") as log_a, open("Log-B.strace", "r") as log_b:
    a_content = log_a.readlines()
    b_content = log_b.readlines()

    read_expression = " read("
    keyboard_expression = "tty"
    pipe_expression = "pipe"

    def count_read_events(log, log_content):
        print("counting read events from log", log)
        count = 0
        for line in log_content:
            if read_expression in line:
                print("Read event from Log", log, ":" + line)
                count += 1
        return count

    def count_keyboard_read_events(log, log_content):
        print("counting keyboard read events from log", log)
        count = 0
        for line in log_content:
            if read_expression in line and keyboard_expression in line:
                print("Keyboard Read Event from Log", log, ":" + line)
                count += 1
        return count

    def count_file_read_events(log, log_content):
        print("counting file read events from log", log)
        count = 0
        for line in log_content:
            if read_expression in line and keyboard_expression not in line and pipe_expression not in line:
                print("File Read Event from Log", log, ":" + line)
                count += 1
        return count

    def find_files_accessed(log, log_content):
        filename_list = list()
        for line in log_content:
            if read_expression in line and keyboard_expression not in line and pipe_expression not in line:
                filename_start = line.find('<')
                filename_end = line.find('>')
                filename = str(line[filename_start + 1:filename_end])
                filename_list.append(filename)
        return filename_list

    def count_filename_occurrences(all_files_accessed):
        filenames = list()
        filenames_count = list()
        for file in all_files_accessed:
            if file in filenames:
                index = filenames.index(file)
                value = filenames_count[index]
                value += 1
                filenames_count.pop(index)
                filenames_count.insert(index, value)
            else:
                filenames.append(file)
                filenames_count.append(1)

        for x in range(len(filenames)):
            print("Filename:", filenames[x], "Count:", filenames_count[x])

    # Task 1
    A_read_events = count_read_events("A", a_content)
    B_read_events = count_read_events("B", b_content)

    # Task 2
    A_keyboard_events = count_keyboard_read_events("A", a_content)
    B_keyboard_events = count_keyboard_read_events("B", b_content)

    # Task 3
    A_file_read_events = count_file_read_events("A", a_content)
    B_file_read_events = count_file_read_events("B", b_content)

    # Task 4
    A_files_accessed = find_files_accessed("A", a_content)
    B_files_accessed = find_files_accessed("B", b_content)

    print(A_read_events, "read events in Log A")
    print(B_read_events, "read events in Log B")

    print(A_keyboard_events, "keyboard read events in Log A")
    print(B_keyboard_events, "keyboard read events in Log B")

    print(A_file_read_events, "file read events in Log A")
    print(B_file_read_events, "file read events in Log B")

    print("\nfiles accessed in log A:")
    for file in A_files_accessed:
        print(file)

    print("\nfiles accessed in log B:")
    for file in B_files_accessed:
        print(file)

    # Bonus Task
    print("\nCounts of files accessed in log A")
    count_filename_occurrences(A_files_accessed)
    print("\nCounts of files accessed in log B")
    count_filename_occurrences(B_files_accessed)


