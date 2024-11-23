import tkinter as tk
import random

#クラスの作成、土台作り
class Kazuategame:
  def __init__(self,root):   #クラスの初期設定、決まり文句
    self.root = root         #上で受け取ったrootを使えるようにするため
    self.root.title('数あてゲーム')   #titleメソッド
    self.target_number = random.randint(1 , 100) #100までの数字の設定
    self.create_widgets()   #下で定義されるcreate_widgetsメソッド
  
  #create_widgetsの中でボタンなどの部品の作成
  #tk.Labelはテキストを表示するウィジェット
  #pack()はウィジェットを画面に配置する、上から積み重ねるように自動的に決めるメソッド
  def create_widgets(self):
    self.label = tk.Label(self.root , text = '1~100までの数字を当ててください！')
    self.label.pack(pady=10)
    
    #tk.Entryはユーザーが入力できるテキストボックスの作成
    self.entry = tk.Entry(self.root)   #ここでのself.rootはメインウィンドウ全体を表すオブジェクト=どのウィンドウに配置するかの指定
    self.entry.pack(pady=5)
    
    self.result_label = tk.Label(self.root , text = '')
    self.result_label.pack(pady=10)
    
    #tk.Buttonはボタンを作るメソッド、commandで呼び出す関数の指定
    self.submit_button = tk.Button(self.root , text = '送信' , command=self.check_guess)
    self.submit_button.pack(pady=5)
    
    self.reset_button = tk.Button(self.root , text = 'リセット' , command=self.reset_game)
    self.reset_button.pack(pady=5)
    
  #送信ボタンを押したときの関数
  def check_guess(self):
    try:
      guess = int(self.entry.get())   #self.entry.get()メソッド、ここでユーザーの入力した数字がstrで取得できる。
      
      if guess < self.target_number:
        self.result_label.config (text = 'もっと大きいです！' ,fg = 'blue')
      
      elif guess > self.target_number:
        self.result_label.config (text = ' もっと小さいです！' ,fg = 'blue')
      
      else:
        self.result_label.config (text = '正解です！' ,fg = 'green')
      
    except ValueError:
      self.result_label.config (text = '1~100の数字を入力してください' ,fg = 'red')
  
  #リセットボタンを押したときの関数
  def reset_game(self):
    self.target_number = random.randint(1,100)
    self.entry.delete(0 , tk.END)
    self.result_label.config(text = '')

root = tk.Tk()
game = Kazuategame(root)
root.mainloop()   #ウィンドウを表示し続けるループ処理、決まり文句