# quiz_game.py

class QuizGame:
    """세계사 인물 퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.quizzes = []       # 퀴즈 목록
        self.best_score = 0     # 최고 점수

    def show_menu(self):
        """메인 메뉴를 출력한다."""
        print()
        print("=" * 35)
        print("    🌍 세계사 인물 퀴즈 게임")
        print("=" * 35)
        print("  1. 퀴즈 풀기")
        print("  2. 퀴즈 추가")
        print("  3. 퀴즈 목록")
        print("  4. 점수 확인")
        print("  5. 종료")
        print("=" * 35)

    def input_number(self, prompt, min_val, max_val):
        """숫자 입력을 받아 유효성을 검사하고 반환한다."""
        while True:
            raw = input(prompt)
            value = raw.strip()

            if value == "":
                print("  ⚠️  입력값이 없습니다. 숫자를 입력해주세요.")
                continue
            try:
                number = int(value)
            except ValueError:
                print(f"  ⚠️  '{value}'은(는) 올바른 숫자가 아닙니다.")
                continue

            if number < min_val or number > max_val:
                print(f"  ⚠️  {min_val}~{max_val} 사이의 숫자를 입력해주세요.")
                continue

            return number

    def run(self):
        """게임 메인 루프"""
        print("\n  🌍 세계사 인물 퀴즈 게임을 시작합니다!")

        while True:
            self.show_menu()

            choice = self.input_number("  번호를 선택하세요 >> ", 1, 5)

            if choice == 1:
                print("\n  [퀴즈 풀기] 기능은 다음 단계에서 구현합니다.")
            elif choice == 2:
                print("\n  [퀴즈 추가] 기능은 다음 단계에서 구현합니다.")
            elif choice == 3:
                print("\n  [퀴즈 목록] 기능은 다음 단계에서 구현합니다.")
            elif choice == 4:
                print("\n  [점수 확인] 기능은 다음 단계에서 구현합니다.")
            elif choice == 5:
                print("\n  게임을 종료합니다. 수고하셨습니다! 👋")
                break


if __name__ == "__main__":
    game = QuizGame()
    try:
        game.run()
    except KeyboardInterrupt:
        print("\n\n  ⚠️  프로그램이 중단되었습니다. 안전하게 종료합니다.")
    except EOFError:
        print("\n\n  ⚠️  입력 스트림이 종료되었습니다. 안전하게 종료합니다.")