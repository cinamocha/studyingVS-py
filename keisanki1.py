import tkinter as tk
from tkinter import ttk

#計算の関数
#計算するボタンを押したときの挙動
def calc():
  try:
    num1 = float(entry1.get())      #数字1
    num2 = float(entry2.get())      #数字2
    ope = operation.get()     #演算子
    
    if ope == '+':
      result.set(num1 + num2)
    
    elif ope == '-':
      result.set(num1 - num2)
    
    elif ope == '*':
      result.set(num1 * num2)
    
    elif ope == '/':
      result.set(num1 / num2)
    
    else:
      result.set('無効です')
    
  except ValueError:
    result.set('数値を入力してください')
  
  except ZeroDivisionError:
    result.set('0で割ることはできません')

#ウィンドウの作成
root = tk.Tk()
root.title('計算初号機')
#ウィンドウのサイズを指定してみる
root.geometry('570x200')

#色の指定、16進数カラーコード
style = ttk.Style()
style.theme_use('default')
style.configure('Tcomcobox' , 
                fieldbackground = '#dff5e1',    #入力の背景
                background = '#a1d6e2' ,      #ドロップダウンメニューの背景
                foreground = '#000000' ,      #テキスト
                selectbackground = '#79bac1' ,      #選択の背景
                selectforeground = '#ffffff')       #選択の文字

#入力欄1
entry1 = tk.Entry(root , width = 15 , font=('Arial' ,14))     #サイズとフォント変えてみた
entry1.grid(row = 0 , column = 0 , padx = 10 , pady = 10)

#演算子のところ
operation = tk.StringVar()
operation.set('+')      #デフォルト
ope_menu = ttk.Combobox(root , textvariable=operation , font = ('Arial' , 14) , width=5)  #ttkモジュールで演算子のメニューをかっこよくした！
ope_menu['values'] = ['+' , '-' , '*' , '/'] 
ope_menu.grid(row = 0 , column = 1 , padx = 10 , pady = 10)

#入力欄2
entry2 = tk.Entry(root ,width = 15 , font=('Arial' ,14))
entry2.grid(row = 0 , column = 2 , padx= 10 , pady = 10)

#計算するボタン
calc_button = tk.Button(root , text = '計算する' , command = calc , font = ('Arial' , 14))
calc_button.grid(row = 0 , column = 3 , padx = 10 , pady = 10)

#結果
result = tk.StringVar()
result_label = tk.Label(root , textvariable = result , width = 20 , font = ('Arial' , 30))
result_label.grid(row = 1 , column = 0 , columnspan = 4 , pady = 15)

#ウィンドウの表示
root.mainloop()