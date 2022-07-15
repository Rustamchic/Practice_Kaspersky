import numpy as np
#HSV
blue_min = np.array((90, 55, 10), np.uint8)
blue_max = np.array((132, 255, 255), np.uint8)

red_min = np.array((125, 29, 28), np.uint8)
red_max = np.array((186, 227, 255), np.uint8)

yellow_min = np.array((26, 100, 100), np.uint8)
yellow_max = np.array((36, 255, 255), np.uint8)

green_min = np.array((45, 170, 150), np.uint8)
green_max = np.array((65, 255, 255), np.uint8)

#BGR
color_blue = (255, 0, 0)
color_red = (0, 0, 128)

#BINS_FOR_HISTS

hbins = 180
sbins = 255
hrange = [0,180]
srange = [0,256]
ranges = hrange+srange

flags = ["blue.png", "red.png", "yellow.png", "green.png"]