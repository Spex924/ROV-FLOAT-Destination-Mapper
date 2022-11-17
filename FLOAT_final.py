import numpy as np
import cv2
import math
coordinates = {}
blocks_moved = {}
current_speed = float(input("Enter current speed in ms^-1: "))
current_direction = int(input("Enter current direction in degrees: "))
#print(slope)
time = float(input("Enter time taken until resurface in hours: "))*60*60

distance = round((current_speed*time)/1000, 2)
distance_axis = distance/2
def click_event(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        global current_speed
        global current_direction
        global time
        global distance_axis
        global distance
        cv2.rectangle(img, (x-13, y-13), (x+13, y+13), (0,0,0), cv2.FILLED)
        coordinates['x'] = math.ceil(x/pixelstoblocks_ratio)
        coordinates['y'] = math.ceil(y/pixelstoblocks_ratio_height)
        if current_direction < 90 and current_direction > 0:
            horizontal_side = np.sin(np.deg2rad(current_direction))*distance_axis
            vertical_side = np.cos(np.deg2rad(current_direction))*distance_axis
            blocks_moved['x'] = math.ceil(horizontal_side)
            blocks_moved['y'] = math.ceil(vertical_side)
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['x']} blocks east and {blocks_moved['y']} blocks north")

            result_coor = [x+(math.ceil((grid_width/acc_width)*(math.ceil(blocks_moved['x']*pixelstoblocks_ratio)))), y-(math.ceil((grid_height/acc_height)*math.ceil(blocks_moved['y']*pixelstoblocks_ratio_height)))]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)


        elif current_direction > 90 and current_direction < 180:
            vertical_side = np.sin(np.deg2rad(current_direction))*distance_axis
            horizontal_side = np.cos(np.deg2rad(current_direction))*distance_axis
            hor = abs(round(horizontal_side, 0))
            blocks_moved['x'] = math.ceil(abs(horizontal_side))
            blocks_moved['y'] = math.ceil(vertical_side)
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['x']} blocks south and {blocks_moved['y']} blocks east")

            result_coor = [x+(math.ceil((grid_width/acc_width)*(math.ceil(blocks_moved['y']*pixelstoblocks_ratio)))), y+(math.ceil((grid_height/acc_height)*math.ceil(blocks_moved['x']*pixelstoblocks_ratio_height)))]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)

        elif current_direction > 180 and current_direction < 270:
            horizontal_side = np.sin(np.deg2rad(current_direction))*distance_axis
            vertical_side = np.cos(np.deg2rad(current_direction))*distance_axis
            ver = abs(round(horizontal_side, 0))
            hor = abs(round(vertical_side, 0))
            blocks_moved['x'] = math.ceil(abs(horizontal_side))
            blocks_moved['y'] = math.ceil(abs(vertical_side))
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['x']} blocks south and {blocks_moved['y']} blocks west")

            result_coor = [x-(math.ceil((grid_width/acc_width)*(math.ceil(blocks_moved['y']*pixelstoblocks_ratio)))), y+(math.ceil((grid_height/acc_height)*math.ceil(blocks_moved['x']*pixelstoblocks_ratio_height)))]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)

        elif current_direction < 360 and current_direction > 270:
            vertical_side = np.sin(np.deg2rad(current_direction-270))*distance_axis
            horizontal_side = np.cos(np.deg2rad(current_direction-270))*distance_axis
            ver = abs(round(horizontal_side, 1))
            blocks_moved['x'] = math.ceil(horizontal_side)
            blocks_moved['y'] = math.ceil(vertical_side)
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['x']} blocks west and {blocks_moved['y']} blocks north")

            result_coor = [x-(math.ceil((grid_width/acc_width)*(math.ceil(blocks_moved['x']*pixelstoblocks_ratio)))), y-(math.ceil((grid_height/acc_height)*math.ceil(blocks_moved['y']*pixelstoblocks_ratio_height)))]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)

        elif current_direction == 0 or current_direction == 360:
            vertical_side = distance_axis
            blocks_moved['x'] = math.ceil(vertical_side)
            blocks_moved['y'] = coordinates['y']
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['x']} blocks north")
            result_coor = [x, y-(math.ceil((grid_height/acc_height)*math.ceil(blocks_moved['x']*pixelstoblocks_ratio_height)))]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)

        elif current_direction == 90:
            horizontal_side = distance_axis
            blocks_moved['x'] = coordinates['x']
            blocks_moved['y'] = math.ceil(horizontal_side)
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['y']} blocks east")
            result_coor = [x+(math.ceil((grid_width/acc_width)*(math.ceil(blocks_moved['y']*pixelstoblocks_ratio)))), y]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)
        elif current_direction == 180:
            blocks_moved['x'] = math.ceil(abs(distance_axis))
            blocks_moved['y'] = coordinates['y']
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['x']} blocks south")
            result_coor = [x, y+(math.ceil((grid_height/acc_height)*math.ceil(blocks_moved['x']*pixelstoblocks_ratio_height)))]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)
        elif current_direction == 270:
            hor = abs(round(distance_axis, 2))
            blocks_moved['x'] = coordinates['x']
            blocks_moved['y'] = math.ceil(distance_axis)
            print(blocks_moved)
            print(f"The float moved a distance of {distance} km at {current_direction} degrees, which means it moved {blocks_moved['y']} blocks west")
            result_coor = [x-(math.ceil((grid_width/acc_width)*(math.ceil(blocks_moved['y']*pixelstoblocks_ratio)))), y]
            cv2.rectangle(img, (result_coor[0]-13,result_coor[1]-13), (result_coor[0]+13, result_coor[1]+13), (0,0,0), cv2.FILLED)
            cv2.line(img, (x,y), (result_coor[0], result_coor[1]), (0,0,0), 2)
        cv2.imshow('g', img)

img = cv2.imread('gridmap.png')
img2 = cv2.imread('g.png')
grid_height = img2.shape[0]
grid_width = img2.shape[1]
acc_height = img.shape[0]
acc_width = img.shape[1]
img = cv2.resize(img, (1366, 768))
pixelstoblocks_ratio = float(int(img.shape[1])/48)
pixelstoblocks_ratio_height = float(int(img.shape[0])/24)
print(pixelstoblocks_ratio, pixelstoblocks_ratio_height)
#print(img.shape[0], img.shape[1])
cv2.imshow('image', img)
cv2.setMouseCallback('image', click_event)
#for i in range(48):
#    for j in range(24):
#        cv2.rectangle(img, (math.ceil(i*pixelstoblocks_ratio), math.ceil(j*pixelstoblocks_ratio_height)), (math.ceil(i*pixelstoblocks_ratio+(pixelstoblocks_ratio)), math.ceil(j*pixelstoblocks_ratio_height+(pixelstoblocks_ratio_height))), (255,0,0), 2)
if cv2.waitKey(0) & 0xFF == ord('q'):
    quit()
cv2.destroyAllWindows()
