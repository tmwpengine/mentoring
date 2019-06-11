# # This is gonna shit the bed!
# for _ in range(100000):
#     # There's a limit to the number of file descriptors a process can be assigned
#     # Lesson learned, always close files that are opened!!
#     file_opened = open('random.text', 'r')
#
# # So this version won't shit the bed
# for _ in range(100000):
#     file_opened = open('random.txt', 'w')
#     file_opened.close()
#
# # Commonly used built in context manager `open()`
# with open('random.txt', 'r') as file_to_read:
#     for line in file_to_read:
#         print(line)


# Custom context manager
class SpecialOpen:
    def __init__(self, file_path, operation):
        self.file_path = file_path
        self.operation = operation

    def __enter__(self):
        self.opened_file = open(self.file_path, self.operation)
        return self.opened_file

    def __exit__(self, *args):
        self.opened_file.close()


for _ in range(10):
    with SpecialOpen('random.txt', 'a') as file_to_write:
        file_to_write.write("some horse shit!")

