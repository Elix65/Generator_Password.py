import random
def gen_password():
    MAYUS = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z')
    MINUS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z')
    CHARS = ('*', '+', '-', '/', '@', '_', '?', '!', '[', '{', '(', ')', '}', ']', ',', ';', '.', '>', '<', '~', '°', '^', '&', '$', '#', '"','ñ',)
    NUMBERS = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    combination = MAYUS + MINUS + CHARS + NUMBERS
    password = []
    for i in range(15):
        character_random = random.choice(combination)
        password.append(character_random)
    password = "".join(password)
    return password



def run():
    password = gen_password()
    print('The new password is: '+ password)


if __name__ == '__main__':
    run()