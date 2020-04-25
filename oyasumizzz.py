#!/usr/bin/env python
import subprocess
import datetime
import twitter

# APIキーとアクセストークンを定数に登録しておきます。
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'

# コマンドを楽にするためにオブジェクトにキーの登録をしておきます。
api = twitter.Api(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# カメラの初期化を行い、写真を一枚パシャリ。fswebcamの引数の-Fや-Sは環境の明るさに合わせて変更してください。
now = datetime.datetime.now()
fileName = '*******YOUR DIRECTORY*******' + \
    now.strftime('%Y%m%d_%H%M%S') + '.jpg'
cmd = 'fswebcam -r 1280x720 -F 10 -S 100 --no-banner ' + fileName
subprocess.run(cmd, shell=True)

# ツイートする内容はここで変更
message = 'おやすみ〜  # raspberrypi'

＃写真をtwitterへ投稿
photo = open(fileName, 'rb')
response = api.upload_media(media=photo)
api.PostUpdate(message, media=fileName)

# いらなくなった写真を削除
cmd = 'rm ' + fileName
subprocess.run(cmd, shell=True)
