import pandas as pd
df = pd.read_csv("stream_000001_left_640x480_14bit.thermal.uint.csv",
                 skiprows=7, 
                 sep=";")

# from numpy import genfromtxt
# my_data = genfromtxt("stream_000001_left_640x480_14bit.thermal.celsius.csv", 
#                      delimiter=';',
#                      skiprows=6)
import cv2
cv2.imwrite('bash1.png', df.values-7350)