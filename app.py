# 1 simple way
from turtle import *
import colorsys      # rung bnaney k liye
                      
speed(0)              # raftar ko tez kerney k liye
bgcolor('black')     # background color
h = 0                 # hue ibtidai rung ka ho
for i in range(16):      # loop  116 bar chalega
      for j in range(18):
            c = colorsys.hsv_to_rgb(h ,1, 1)   # hsv rgb changr kerne k liye
            color(c)
            h +=0.005
            rt(90)
            circle(150 - j * 6, 90)     # 100 radius circle
            lt(90)
            circle (150 - j * 6, 90)
            rt(180)
      circle(40, 24)      




# 2 simple way
from turtle import *
import colorsys

bgcolor('black')
speed(0)
h = 0

for i in range(116):         # صرف 116 بار loop
    c = colorsys.hsv_to_rgb(h, 1, 1)  # رنگ بنائیں
    color(c)
    h += 0.025              # ہر بار رنگ تبدیل ہو
    circle(100)             # ایک دائرہ بنائیں
    left(10)                # تھوڑا سا turtle کو گھمائیں  # turtle کو 10 ڈگری بائیں گھمائیں 
