import math

MAX_SPACES=20

def main():
    for i in range(MAX_SPACES):
        print_io_line(i)
    for i in range(MAX_SPACES):
        print_io_line(MAX_SPACES-i)

#print a single line of the io program
#first print space_before_io number of space
#print"io"
def print_io_line(space_before_io):
    print_n_space(space_before_io)
    print("io")

def print_n_space(n):
    for i in range(n):
        print_no_new_line(" ")

def print_no_new_line(to_print):
    print(to_print, end="")




if __name__ == '__main__':
    main()