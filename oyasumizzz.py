#!/usr/bin/env python
import pygame
import pygame.camera
from pygame.locals import *
from twython import Twython

# APIキーとアクセストークンを定数に登録しておきます。
CONSUMER_KEY = '***************YOUR DATA*****************'
CONSUMER_SECRET = '***************YOUR DATA*****************'
ACCESS_KEY = '***************YOUR DATA*****************'
ACCESS_SECRET = '***************YOUR DATA*****************'

# コマンドを楽にするためにTwythonのオブジェクトにキーの登録をしておきます。
api = Twython(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET)

# カメラの初期化を行い、写真を一枚パシャリ。
pygame.init()
pygame.camera.init()
cam = pygame.camera.Camera("/dev/video0", (1280, 720))
cam.start()
image = cam.get_image()
now = datetime.datetime.now()
filename = now.strftime('%Y%m%d_%H%M%S') + '.jpg'
pygame.image.save(image, filename)

photo = open(filename, 'rb')
response = twitter.upload_media(media=photo)
api.update_status(status='おやすみ〜 #raspberrypi #zzz',
                  media_ids=[response['media_id']])
