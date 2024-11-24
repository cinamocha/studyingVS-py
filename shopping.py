shopping_list = []

#メニューの作成

def menu():
  print('1:アイテムの追加')
  print('2:アイテムの削除')
  print('3:リストの表示')
  print('4:終了')
  
#ループ

while True:
  menu()
  select = input('数字を入力してください。')
  select = int(select)
  
  #アイテムの追加
  
  if select == 1:
    item = input('追加するアイテムを入力してください。')
    shopping_list.append(item)
    print(f'{item}が追加されました！')
    
  #アイテムの削除、存在するか確認
  
  elif select == 2:
    kesu = input('削除するアイテムを入力してください。')
    
    if kesu in shopping_list:
      shopping_list.remove(kesu)
      print(f'{kesu}を削除しました！')
    
    else:
      print('そのアイテムは存在しません。')
  
  #リストの表示
  
  elif select == 3:
    print('現在のショッピングリスト')
    
    if len(shopping_list) > 0:
      for index , valu in enumerate(shopping_list , start = 1):
        print(f'{index} : {valu}')
    
    else:
      print('リストは空です。')
  
  #終了
  
  elif select == 4:
    print('終了します。')
    break
  
  else:
    print('1~4の数字で入力してください。')