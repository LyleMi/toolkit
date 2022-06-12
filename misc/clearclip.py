import os
import random
import pyperclip

def main():
    for i in range(random.randint(5, 10)):
        pyperclip.copy(os.urandom(random.randint(30, 60)).decode(errors="ignore"))

if __name__ == '__main__':
    main()
