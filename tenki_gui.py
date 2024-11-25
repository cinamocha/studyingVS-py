import tkinter as tk
import requests

API_KEY='APIを入力'
BASE_URL='https://api.openweathermap.org/data/2.5/weather'

#ウィンドウの作成
window = tk.Tk()
window.title('天気情報アプリ')

#タイトル
title_label = tk.Label(window , text = '天気情報を取得する' , font = ('Arial' , 16))
title_label.pack(pady = 10)

#都市入力欄
city_label = tk.Label(window , text = '都市名を入力')
city_label.pack(pady = 5)
city_entry = tk.Entry(window , width=20)
city_entry.pack(pady = 5)

#取得ボタン
get_weather_button = tk.Button(window , text = '天気を取得する')
get_weather_button.pack(pady = 10)

#結果表示用
result_label = tk.Label(window , text = '' , font = ('Arial' , 12))
result_label.pack(pady = 10)

def get_weather():
  city = city_entry.get()
  params = {
  'q':city , 
  'appid':API_KEY , 
  'units':'metric' , 
  'lang':'ja'
  }

response = requests.get(BASE_URL)

print('Respanse code', response.status_code)

if response.status_code == 200:     #200は成功を意味するHTTPステータスコード
  data = response.json()
  temp = data['main']['temp']
  weather = data['weather'][0]['description']
  humidity = data['main']['humidity']
  wind_speed = data['wind']['speed']
  
  result_label.config(text = f'{city} の現在の天気：\n'
                      f'天気：{weather}\n'
                      f'気温：{temp}度\n'
                      f'湿度：{humidity}％\n'
                      f'風速：{wind_speed}ｍ/ｓ')
  
else:
  print('Error Response:' , response.json())
  result_label.config(text = 'エラーが発生しました。\n 都市名を確認してください。')
  
#ウィンドウの表示
window.mainloop()
