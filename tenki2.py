import requests

#前の天気情報のコードに湿度と風速を追加し、出力の仕方を変える！！！

#openweathermapのapi key
API_KEY = 'APIを入力'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

#ユーザーの入力、今回は天気を知りたい都市
city = input('天気を知りたい都市を入力してください: ')

#APIにリクエストを送る
#paramsは辞書みたいなもの、APIリクエストのパラメータを設定、割と定型文
params = {
  'q':city , 
  'appid':API_KEY , 
  'units':'metric' , 
  'lang':'ja'
}
response = requests.get(BASE_URL , params=params)

#レスポンスの処理
if response.status_code == 200:     #200は成功を意味するHTTPステータスコード
  data = response.json()
  temp = data['main']['temp']
  weather = data['weather'][0]['description']
  humidity = data['main']['humidity']
  wind_speed = data['wind']['speed']
  
  print(f'\n{city}の現在の天気情報')      #\nで改行
  print('--------------------')
  print(f'天気：{weather}')
  print(f'気温：{temp}度')
  print(f'湿度：{humidity}％')
  print(f'風速：{wind_speed}ｍ/ｓ')
  print('--------------------')

#例外処理
else:
  print('天気情報が取得できませんでした。都市名を確認してください。')
  print(f'エラーが発生しました。ステータスコード: {response.status_code}')
  print('詳細' , response.json())
