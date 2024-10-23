def eat_or_sleep(value):
    match value:
          case "apple":
            return "eat apple"
          case "orange":
            return "eat orange"
          case "banana":
            return "eat banana"
          case "sleep":
            return "sleep!GoodBye!"

# ループを開始
while True:
    # ユーザーからの入力を取得
    user_input = input("Enter something (apple, orange, banana, or sleep): ")
    
    # 入力をeat_or_sleep関数に渡して結果を表示
    result = eat_or_sleep(user_input)
    print(result)
    
    # "sleep"が入力された場合、ループを終了
    if user_input == "sleep":
        break