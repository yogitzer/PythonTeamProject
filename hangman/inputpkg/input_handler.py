def select_category():
    while True:
        category = input("주제를 선택하세요 1.anilmals 2.foods 3.sports(번호로 입력): ").lower()
        if category in ["1", "2", "3"]:
            return category
        print("잘못된 입력입니다. 다시 시도하세요.")

def ask_restart():
        while True:
            response = input("게임을 다시 시작하시겠습니까? (y/n): ").lower()
            if response in ["y", "n"]:
                return response == "y"
            print("y 또는 n으로 입력해주세요.")

def get_user_input(use_letters):
    vowels = {"a", "e", "i", "o", "u"}

    while True:
        letter = input("글자을 입력하세요: ").lower()
        if len(letter) == 1 and letter.isalpha():
            if letter in use_letters:
                print("이미 입력력한 글자입니다.")
            else:
                is_vowel = letter in vowels
                return letter, is_vowel
        else:
            print("한 글자의 알파벳을 입력하세요.")