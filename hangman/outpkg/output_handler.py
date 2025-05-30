from colorama import Fore, Style
from hangman.corepkg.repository import hangman_pics

def display_game_rules():
    print(f"{Fore.CYAN}{'='*50}")
    print(f"{Fore.YELLOW}🎮 행맨 게임 룰 🎮")
    print(f"{Fore.CYAN}{'='*50}")
    print(f"{Fore.WHITE}1. 숨겨진 단어를 맞추는 게임입니다.")
    print(f"2. 한 번에 한 글자씩 입력하세요.")
    print(f"3. 틀릴 때마다 목숨이 1씩 감소합니다다.")
    print(f"4. {Fore.GREEN}모음(a, e, i, o, u)을 틀려도 목숨이 깎이지 않습니다!{Fore.WHITE}")
    print(f"5. 목숨이 모두 떨어지기 전에 단어를 맞추면 승리!")
    print(f"{Fore.CYAN}{'='*50}{Style.RESET_ALL}")
    print()

def display_current_word(word, guessed_letters):
    display = " ".join([ch if ch in guessed_letters else "_" for ch in word])
    print(f"\n단어: {Fore.GREEN}{display}{Style.RESET_ALL}")

def display_used_letters(used_letters):
    print(f"입력한 글자들: {Fore.YELLOW}{' '.join(used_letters)}{Style.RESET_ALL}")

def display_remaining_attempts(remaining):
    print(f"{Fore.CYAN}남은 기회: {remaining}{Style.RESET_ALL}")
    print(hangman_pics[6 - remaining])

def display_game_over(word, success):
    if success:
        print(f"{Fore.GREEN}축하합니다! 단어를 맞추셨습니다: {word}{Style.RESET_ALL}")
    else:
        print(f"{Fore.RED}실패! 정답은 '{word}'였습니다.{Style.RESET_ALL}")