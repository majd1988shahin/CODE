#!/usr/bin/python3
"Ver- und entschlüsseln"

def encrypt(text, geheim):
    "encrypt a text"
    pass


def decrypt(chiffriert, geheim):
    "decrypt a text"
    pass

def main_test():
    "einfache kleine Tests für Sie zum probieren und ändern"
    print(encrypt("abcde", "abc"))
    print(decrypt(encrypt("abcde", "abc"), "abc"))
    print(encrypt("abcxyz", "ab"))


if __name__ == '__main__':
    main_test()
