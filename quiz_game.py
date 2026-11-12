# quiz_game.py
class Quiz:
    """퀴즈 한 문제를 담는 클래스"""

    def __init__(self, question, choices, answer):
        """
        question : 문제 텍스트 (str)
        choices  : 선택지 4개  (list)
        answer   : 정답 번호   (int, 1~4)
        """
        self.question = question
        self.choices = choices
        self.answer = answer

    def show(self):
        """문제와 선택지를 출력한다."""
        print(f"\n  📜 {self.question}")
        print()
        for i, choice in enumerate(self.choices, start=1):
            print(f"    {i}. {choice}")
        print()

    def is_correct(self, user_answer):
        """입력한 번호가 정답이면 True, 아니면 False를 반환한다."""
        return self.answer == user_answer

class QuizGame:
    """세계사 인물 퀴즈 게임 전체를 관리하는 클래스"""

    def __init__(self):
        self.best_score = 0     # 최고 점수

        # 세계사 인물 퀴즈 데이터
        self.quizzes = [
            Quiz(
                "만유인력의 법칙을 발견한 영국의 과학자는?",
                ["갈릴레오 갈릴레이", "아이작 뉴턴", "알베르트 아인슈타인", "니콜라 테슬라"],
                2
            ),
            Quiz(
                "프랑스 혁명 이후 황제 자리에 오른 인물은?",
                ["루이 16세", "막시밀리앙 로베스피에르", "나폴레옹 보나파르트", "샤를 드골"],
                3
            ),
            Quiz(
                "상대성 이론을 발표한 물리학자는?",
                ["막스 플랑크", "닐스 보어", "알베르트 아인슈타인", "어니스트 러더퍼드"],
                3
            ),
            Quiz(
                "인도의 비폭력 독립운동을 이끈 지도자는?",
                ["자와할랄 네루", "마하트마 간디", "수바스 찬드라 보스", "발라강가다르 틸라크"],
                2
            ),
            Quiz(
                "미국 역사상 최초로 노예해방을 선언한 대통령은?",
                ["조지 워싱턴", "토머스 제퍼슨", "에이브러햄 링컨", "프랭클린 루스벨트"],
                3
            ),
        ]

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

    def play_quiz(self):
        """퀴즈를 진행하고 점수를 계산한다."""
        print("\n" + "=" * 35)
        print("  🚀 퀴즈를 시작합니다!")
        print("=" * 35)

        score = 0
        for quiz in self.quizzes:
            quiz.show()
            user_choice = self.input_number("  정답 번호를 입력하세요 >> ", 1, 4)

            if quiz.is_correct(user_choice):
                print("  ✅ 정답입니다!")
                score += 1
            else:
                print(f"  ❌ 틀렸습니다. 정답은 {quiz.answer}번입니다.")

        print("\n" + "=" * 35)
        print(f"  🏁 게임 종료! 당신의 점수는 {score}/{len(self.quizzes)}점입니다.")
        print("=" * 35)

        if score > self.best_score:
            print("  🎊 최고 기록 경신!")
            self.best_score = score

    def show_score(self):
        """현재 최고 점수를 출력한다."""
        print("\n" + "=" * 35)
        print("  🏆 점수 확인")
        print("=" * 35)

        total = len(self.quizzes)

        if self.best_score == 0:
            print("  아직 퀴즈를 풀지 않았습니다.")
            print("  퀴즈를 먼저 풀어보세요! 💪")
        else:
            print(f"  최고 점수 : {self.best_score} / {total} 점")

            # 점수에 따라 다른 메시지 출력
            if self.best_score == total:
                print("  등급      : ⭐ 역사 마스터!")
            elif self.best_score >= total * 0.8:
                print("  등급      : 🥇 역사 박사")
            elif self.best_score >= total * 0.6:
                print("  등급      : 🥈 역사 학도")
            else:
                print("  등급      : 🥉 역사 입문자")

        print("=" * 35)

    def add_quiz(self):
        print("\n=== 퀴즈 추가 ===")
        question = input("문제를 입력하세요: ")
        answer = input("정답을 입력하세요: ")
        self.quizzes.append({"question": question, "answer": answer})
        print("퀴즈가 추가되었습니다!")


    def run(self):
        """게임 메인 루프"""
        print("\n  🌍 세계사 인물 퀴즈 게임을 시작합니다!")

        while True:
            self.show_menu()
            choice = self.input_number("  번호를 선택하세요 >> ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()   # 
            elif choice == 3:
                print("  🚧 준비 중인 기능입니다.")
            elif choice == 4:
                self.show_score()  #
            elif choice == 5:
                print("\n  👋 게임을 종료합니다. 수고하셨습니다!")
                break

if __name__ == "__main__":
    game = QuizGame()
    game.run()

