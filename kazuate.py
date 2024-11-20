print("Hello, Python!")
import random

def guess_number():
    # 1から100までのランダムな数字を選択
    number_to_guess = random.randint(1, 100)
    tries = 0

    print("1から100までの数字を当ててください！")

    # プレイヤーが正しい数字を当てるまでループ
    while True:
        try:
            user_guess = int(input("数字を入力してください: "))
            tries += 1

            if user_guess < number_to_guess:
                print("もっと大きいです。")
            elif user_guess > number_to_guess:
                print("もっと小さいです。")
            else:
                print(f"正解です！{tries}回で当たりました！")
                break
        except ValueError:
            print("有効な数字を入力してください。")

if __name__ == "__main__":
    guess_number()
    