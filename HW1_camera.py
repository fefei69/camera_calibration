import cv2
import numpy as np
f = open("imgpoints.txt", "r")
data = f.read()
data_into_list = data.split("\n") 
f.close()

black = np.zeros((640,480,3), np.uint8)
print(black.shape[0:2])
out = cv2.VideoWriter('checkboards.mp4',cv2.VideoWriter_fourcc(*'DIVX'), 10, (480,640))

first_checkboard_split = []
for j in range(9):
    for i in range(48*j,48*(j+1)):
        x = int(float(data_into_list[i].split(" ")[0]))
        y = int(float(data_into_list[i].split(" ")[1]))
        print(int(float(x)),int(float(y)))
        cv2.circle(black,(x,y),1,(255,0,0),1)
    out.write(black)
    #cv2.imshow('checkboards', black)
    #clear circles
    black = np.zeros((640,480,3), np.uint8)
        
    # cv2.imshow('black',black)
    # cv2.waitKey(0)

# print(black.shape)
# cv2.imshow('black',black)
# cv2.waitKey(0)
out.release()
cv2.destroyAllWindows()
