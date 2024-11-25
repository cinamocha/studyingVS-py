import requests

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
  print(f'{city}の現在の天気: {weather}、気温: {temp}度')

#例外処理
else:
  print('天気情報が取得できませんでした。都市名を確認してください。')
  print(f'エラーが発生しました。ステータスコード: {response.status_code}')
  print('詳細' , response.json())
