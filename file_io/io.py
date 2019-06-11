# Basic read
def read_from_file():
    file_to_read = open('text_file_to_read_from.txt', 'r')

    for line in file_to_read:
        print(line)

    file_to_read.close()


# write only
def write_to_file():
    file_to_write = open('new_file.txt', 'w')
    for i in range(1, 11):
        # creates anew file or over-writes an existing one
        file_to_write.write(str(i))
    file_to_write.close()


# Read and write
def read_and_write_to_file():
    file_to_read_and_write = open('text_file_to_read_from.txt', 'r+')
    for line in file_to_read_and_write:
            print(line)

    # creates anew file or over-writes an existing one
    file_to_read_and_write.write("I just added a line")
    file_to_read_and_write.close()


def append_text_to_file():
    # Append text to an existing file
    file_to_append = open('file_to_append_text.txt', 'a')
    file_to_append.write("Added some text")
    file_to_append.close()

read_from_file()
write_to_file()
read_and_write_to_file()
append_text_to_file()

