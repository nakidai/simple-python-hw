from ctypes import cdll, c_char_p, c_int, create_string_buffer
from os.path import dirname, abspath, join
from sys import argv


def main() -> None:
    args = [c_char_p(x.encode('utf-8') + b'\0') for x in argv] + [c_char_p(0)]
    hw = cdll.LoadLibrary(join(dirname(abspath(__file__)), "hw.so"))
    exit(hw.main(c_int(len(argv)), (c_char_p * len(args))(*args)))


if __name__ == "__main__":
    main()
