import numpy as np
import cv2 as cv


'''
This file takes an input image and reproduces it using a predefined set of colours.

Pixels are evaluated based on their Hue (colour) and Value (darkness). Pixels are
grouped together when they fall between an upper limit and lower limit for their Value
and a preset upper and lower limit for their Hue. These grouped pixels are used to
create a mask (sub-image) in the new, desired colour. The masks are then combined
to produce a new image made of the defined colours.

For generally good results, set the sliders to the following values:
242, 218, 185, 152, 116, 85, 48
'''

def nothing(x):
    print(x)


#########################################
####  Change to name of your image  #####
#########################################
image_name = 'Headshot.jpg'

cv.namedWindow('image')
img = cv.imread(image_name)
width, height, _ = img.shape
print(width, height)

# Absolute minimum and maximum threshold values
LOW = 0
HIGH = 255

### Define the desired output colours using BGR representation

# Reds
pink = (223, 223, 255)
pink2 = (185, 185, 255)
coral = (150, 150, 255)
coral2 = (115, 115, 255)
red = (85, 85, 255)
red2 = (40, 40, 234)
maroon = (12, 12, 181)

# Oranges
cream = (205, 249, 255)
cream2 = (167, 245, 255)
tan = (133, 241, 255)
tan2 = (63, 233, 255)
brown = (8, 226, 255)
brown2 = (0, 207, 235)
brown3 = (0, 188, 213)

# Greens
mint = (206, 255, 206)
lime = (150, 255, 150)
lime2 = (100, 240, 100)
green = (45, 225, 45)
green2 = (0, 198, 0)
forest = (57, 161, 0)
forest2 = (59, 120, 0)

# Blues
baby = (255, 246, 210)
baby2 = (253, 227, 176)
light = (253, 198, 134)
blue = (253, 157, 94)
blue2 = (255, 134, 51)
navy = (255, 91, 0)
navy2 = (238, 0, 0)

# Windows and Sliders ========================

cv.namedWindow('Tracking')
cv.createTrackbar('Thresh 1','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 2','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 3','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 4','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 5','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 6','Tracking',0,255, nothing)
cv.createTrackbar('Thresh 7','Tracking',0,255, nothing)

###  Create a rectangle the size of the image. Grouped pixels
###  will be "ANDed" with these rectangles to produce a new
###  image in the shape of the mask with the colour of the
###  rectangle

# REDS ///////////////////////////////////////
# pink
r1 = np.zeros([width,height,3], np.uint8)
r1 = cv.rectangle(r1, (0,0), (height, width), pink, -1)
# pink2
r2 = np.zeros([width,height,3], np.uint8)
r2 = cv.rectangle(r2, (0,0), (height, width), pink2, -1)
# coral
r3 = np.zeros([width,height,3], np.uint8)
r3 = cv.rectangle(r3, (0,0), (height, width), coral, -1)
# coral2
r4 = np.zeros([width,height,3], np.uint8)
r4 = cv.rectangle(r4, (0,0), (height, width), coral2, -1)
# red
r5 = np.zeros([width,height,3], np.uint8)
r5 = cv.rectangle(r5, (0,0), (height, width), red, -1)
# red2
r6 = np.zeros([width,height,3], np.uint8)
r6 = cv.rectangle(r6, (0,0), (height, width), red2, -1)
# maroon
r7 = np.zeros([width,height,3], np.uint8)
r7 = cv.rectangle(r7, (0,0), (height, width), maroon, -1)

# ORANGES ///////////////////////////////////////
# cream
o1 = np.zeros([width,height,3], np.uint8)
o1 = cv.rectangle(o1, (0,0), (height, width), cream, -1)
# pink2
o2 = np.zeros([width,height,3], np.uint8)
o2 = cv.rectangle(o2, (0,0), (height, width), cream2, -1)
# coral
o3 = np.zeros([width,height,3], np.uint8)
o3 = cv.rectangle(o3, (0,0), (height, width), tan, -1)
# coral2
o4 = np.zeros([width,height,3], np.uint8)
o4 = cv.rectangle(o4, (0,0), (height, width), tan2, -1)
# red
o5 = np.zeros([width,height,3], np.uint8)
o5 = cv.rectangle(o5, (0,0), (height, width), brown, -1)
# red2
o6 = np.zeros([width,height,3], np.uint8)
o6 = cv.rectangle(o6, (0,0), (height, width), brown2, -1)
# maroon
o7 = np.zeros([width,height,3], np.uint8)
o7 = cv.rectangle(o7, (0,0), (height, width), brown3, -1)

# GREENS ///////////////////////////////////////
# mint
g1 = np.zeros([width,height,3], np.uint8)
g1 = cv.rectangle(g1, (0,0), (height, width), mint, -1)
# lime
g2 = np.zeros([width,height,3], np.uint8)
g2 = cv.rectangle(g2, (0,0), (height, width), lime, -1)
# lime2
g3 = np.zeros([width,height,3], np.uint8)
g3 = cv.rectangle(g3, (0,0), (height, width), lime2, -1)
# green
g4 = np.zeros([width,height,3], np.uint8)
g4 = cv.rectangle(g4, (0,0), (height, width), green, -1)
# green2
g5 = np.zeros([width,height,3], np.uint8)
g5 = cv.rectangle(g5, (0,0), (height, width), green2, -1)
# forest
g6 = np.zeros([width,height,3], np.uint8)
g6 = cv.rectangle(g6, (0,0), (height, width), forest, -1)
# forest2
g7 = np.zeros([width,height,3], np.uint8)
g7 = cv.rectangle(g7, (0,0), (height, width), forest2, -1)

# BLUES ///////////////////////////////////////
# baby
b1 = np.zeros([width,height,3], np.uint8)
b1 = cv.rectangle(b1, (0,0), (height, width), baby, -1)
# baby2
b2 = np.zeros([width,height,3], np.uint8)
b2 = cv.rectangle(b2, (0,0), (height, width), baby2, -1)
# light
b3 = np.zeros([width,height,3], np.uint8)
b3 = cv.rectangle(b3, (0,0), (height, width), light, -1)
# blue
b4 = np.zeros([width,height,3], np.uint8)
b4 = cv.rectangle(b4, (0,0), (height, width), blue, -1)
# blue2
b5 = np.zeros([width,height,3], np.uint8)
b5 = cv.rectangle(b5, (0,0), (height, width), blue2, -1)
# navy
b6 = np.zeros([width,height,3], np.uint8)
b6 = cv.rectangle(b6, (0,0), (height, width), navy, -1)
# navy2
b7 = np.zeros([width,height,3], np.uint8)
b7 = cv.rectangle(b7, (0,0), (height, width), navy2, -1)

while(1):
    img = cv.imread(image_name)

    # Read threshold values from the user
    LV1 = cv.getTrackbarPos('Thresh 1','Tracking')
    LV2 = cv.getTrackbarPos('Thresh 2','Tracking')
    LV3 = cv.getTrackbarPos('Thresh 3','Tracking')
    LV4 = cv.getTrackbarPos('Thresh 4','Tracking')
    LV5 = cv.getTrackbarPos('Thresh 5','Tracking')
    LV6 = cv.getTrackbarPos('Thresh 6','Tracking')
    LV7 = cv.getTrackbarPos('Thresh 7','Tracking')
    
    # Create threshold and mask
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    ### Group the pixels based on their Hues and Values

    # HUES - R0:14, O15-30 G31:90,  B91:150, R151:179
    # Red LOW H
    rLow1 = np.array([0, LOW, LV1+1])
    rUp1 = np.array([14, HIGH, HIGH])
    rLow2 = np.array([0, LOW, LV2+1])
    rUp2 = np.array([14, HIGH, LV1])
    rLow3 = np.array([0, LOW, LV3+1])
    rUp3 = np.array([14, HIGH, LV2])
    rLow4 = np.array([0, LOW, LV4+1])
    rUp4 = np.array([14, HIGH, LV3])
    rLow5 = np.array([0, LOW, LV5+1])
    rUp5 = np.array([14, HIGH, LV4])
    rLow6 = np.array([0, LOW, LV6+1])
    rUp6 = np.array([14, HIGH, LV5])
    rLow7 = np.array([0, LOW, LV7+1])
    rUp7 = np.array([14, HIGH, LV6])

    # Red HIGH H
    r2Low1 = np.array([151, LOW, LV1+1])
    r2Up1 = np.array([179, HIGH, HIGH])
    r2Low2 = np.array([151, LOW, LV2+1])
    r2Up2 = np.array([179, HIGH, LV1])
    r2Low3 = np.array([151, LOW, LV3+1])
    r2Up3 = np.array([179, HIGH, LV2])
    r2Low4 = np.array([151, LOW, LV4+1])
    r2Up4 = np.array([179, HIGH, LV3])
    r2Low5 = np.array([151, LOW, LV5+1])
    r2Up5 = np.array([179, HIGH, LV4])
    r2Low6 = np.array([151, LOW, LV6+1])
    r2Up6 = np.array([179, HIGH, LV5])
    r2Low7 = np.array([151, LOW, LV7+1])
    r2Up7 = np.array([179, HIGH, LV6])

    # Orange
    oLow1 = np.array([15, LOW, LV1+1])
    oUp1 = np.array([30, HIGH, HIGH])
    oLow2 = np.array([15, LOW, LV2+1])
    oUp2 = np.array([30, HIGH, LV1])
    oLow3 = np.array([15, LOW, LV3+1])
    oUp3 = np.array([30, HIGH, LV2])
    oLow4 = np.array([15, LOW, LV4+1])
    oUp4 = np.array([30, HIGH, LV3])
    oLow5 = np.array([15, LOW, LV5+1])
    oUp5 = np.array([30, HIGH, LV4])
    oLow6 = np.array([15, LOW, LV6+1])
    oUp6 = np.array([30, HIGH, LV5])
    oLow7 = np.array([15, LOW, LV7+1])
    oUp7 = np.array([30, HIGH, LV6])

    # Green
    gLow1 = np.array([31, LOW, LV1+1])
    gUp1 = np.array([90, HIGH, HIGH])
    gLow2 = np.array([31, LOW, LV2+1])
    gUp2 = np.array([90, HIGH, LV1])
    gLow3 = np.array([31, LOW, LV3+1])
    gUp3 = np.array([90, HIGH, LV2])
    gLow4 = np.array([31, LOW, LV4+1])
    gUp4 = np.array([90, HIGH, LV3])
    gLow5 = np.array([31, LOW, LV5+1])
    gUp5 = np.array([90, HIGH, LV4])
    gLow6 = np.array([31, LOW, LV6+1])
    gUp6 = np.array([90, HIGH, LV5])
    gLow7 = np.array([31, LOW, LV7+1])
    gUp7 = np.array([90, HIGH, LV6])

    # Blue
    bLow1 = np.array([91, LOW, LV1+1])
    bUp1 = np.array([150, HIGH, HIGH])
    bLow2 = np.array([91, LOW, LV2+1])
    bUp2 = np.array([150, HIGH, LV1])
    bLow3 = np.array([91, LOW, LV3+1])
    bUp3 = np.array([150, HIGH, LV2])
    bLow4 = np.array([91, LOW, LV4+1])
    bUp4 = np.array([150, HIGH, LV3])
    bLow5 = np.array([91, LOW, LV5+1])
    bUp5 = np.array([150, HIGH, LV4])
    bLow6 = np.array([91, LOW, LV6+1])
    bUp6 = np.array([150, HIGH, LV5])
    bLow7 = np.array([91, LOW, LV7+1])
    bUp7 = np.array([150, HIGH, LV6])

    # Create the masks for each Value
    # 1 Values
    rmask = cv.inRange(hsv, rLow1, rUp1)
    r2mask = cv.inRange(hsv, r2Low1, r2Up1)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red1_mask = cv.bitwise_and(r1,r1,mask = redmask)
    omask = cv.inRange(hsv, oLow1, oUp1)
    orange1_mask = cv.bitwise_and(o1,o1,mask = omask)
    bmask = cv.inRange(hsv, bLow1, bUp1)
    blue1_mask = cv.bitwise_and(b1,b1,mask = bmask)
    gmask = cv.inRange(hsv, gLow1, gUp1)
    green1_mask = cv.bitwise_and(g1,g1,mask = gmask)

    # 2 Values
    rmask = cv.inRange(hsv, rLow2, rUp2)
    r2mask = cv.inRange(hsv, r2Low2, r2Up2)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red2_mask = cv.bitwise_and(r2,r2,mask = redmask)
    omask = cv.inRange(hsv, oLow2, oUp2)
    orange2_mask = cv.bitwise_and(o2,o2,mask = omask)
    bmask = cv.inRange(hsv, bLow2, bUp2)
    blue2_mask = cv.bitwise_and(b2,b2,mask = bmask)
    gmask = cv.inRange(hsv, gLow2, gUp2)
    green2_mask = cv.bitwise_and(g2,g2,mask = gmask)

    # 3 Values
    rmask = cv.inRange(hsv, rLow3, rUp3)
    r2mask = cv.inRange(hsv, r2Low3, r2Up3)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red3_mask = cv.bitwise_and(r3,r3,mask = redmask)
    omask = cv.inRange(hsv, oLow3, oUp3)
    orange3_mask = cv.bitwise_and(o3,o3,mask = omask)
    bmask = cv.inRange(hsv, bLow3, bUp3)
    blue3_mask = cv.bitwise_and(b3,b3,mask = bmask)
    gmask = cv.inRange(hsv, gLow3, gUp3)
    green3_mask = cv.bitwise_and(g3,g3,mask = gmask)

    # 4 Values
    rmask = cv.inRange(hsv, rLow4, rUp4)
    r2mask = cv.inRange(hsv, r2Low4, r2Up4)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red4_mask = cv.bitwise_and(r4,r4,mask = redmask)
    omask = cv.inRange(hsv, oLow4, oUp4)
    orange4_mask = cv.bitwise_and(o4,o4,mask = omask)
    bmask = cv.inRange(hsv, bLow4, bUp4)
    blue4_mask = cv.bitwise_and(b4,b4,mask = bmask)
    gmask = cv.inRange(hsv, gLow4, gUp4)
    green4_mask = cv.bitwise_and(g4,g4,mask = gmask)

    # 5 Values
    rmask = cv.inRange(hsv, rLow5, rUp5)
    r2mask = cv.inRange(hsv, r2Low5, r2Up5)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red5_mask = cv.bitwise_and(r5,r5,mask = redmask)
    omask = cv.inRange(hsv, oLow5, oUp5)
    orange5_mask = cv.bitwise_and(o5,o5,mask = omask)
    bmask = cv.inRange(hsv, bLow5, bUp5)
    blue5_mask = cv.bitwise_and(b5,b5,mask = bmask)
    gmask = cv.inRange(hsv, gLow5, gUp5)
    green5_mask = cv.bitwise_and(g5,g5,mask = gmask)

    # 6 Values
    rmask = cv.inRange(hsv, rLow6, rUp6)
    r2mask = cv.inRange(hsv, r2Low6, r2Up6)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red6_mask = cv.bitwise_and(r6,r6,mask = redmask)
    omask = cv.inRange(hsv, oLow6, oUp6)
    orange6_mask = cv.bitwise_and(o6,o6,mask = omask)
    bmask = cv.inRange(hsv, bLow6, bUp6)
    blue6_mask = cv.bitwise_and(b6,b6,mask = bmask)
    gmask = cv.inRange(hsv, gLow6, gUp6)
    green6_mask = cv.bitwise_and(g6,g6,mask = gmask)

    # 7 Values
    rmask = cv.inRange(hsv, rLow7, rUp7)
    r2mask = cv.inRange(hsv, r2Low7, r2Up7)
    redmask = cv.addWeighted(rmask,1,r2mask,1,0)
    red7_mask = cv.bitwise_and(r7,r7,mask = redmask)
    omask = cv.inRange(hsv, oLow7, oUp7)
    orange7_mask = cv.bitwise_and(o7,o7,mask = omask)
    bmask = cv.inRange(hsv, bLow7, bUp7)
    blue7_mask = cv.bitwise_and(b7,b7,mask = bmask)
    gmask = cv.inRange(hsv, gLow7, gUp7)
    green7_mask = cv.bitwise_and(g7,g7,mask = gmask)
    
    ########### Combine Masks ###########
    A1 = cv.addWeighted(red1_mask,1,red2_mask,1,0)
    A2 = cv.addWeighted(red3_mask,1,red4_mask,1,0)
    A3 = cv.addWeighted(red5_mask,1,red6_mask,1,0)
    A4 = cv.addWeighted(red7_mask,1,blue1_mask,1,0)
    A5 = cv.addWeighted(blue2_mask,1,blue3_mask,1,0)
    A6 = cv.addWeighted(blue4_mask,1,blue5_mask,1,0)
    A7 = cv.addWeighted(blue6_mask,1,blue7_mask,1,0)
    A8 = cv.addWeighted(green1_mask,1,green2_mask,1,0)
    A9 = cv.addWeighted(green3_mask,1,green4_mask,1,0)
    A0 = cv.addWeighted(green5_mask,1,green6_mask,1,0)
    B1 = cv.addWeighted(green7_mask,1,A1,1,0)
    B2 = cv.addWeighted(A2,1,A3,1,0)
    B3 = cv.addWeighted(A4,1,A5,1,0)
    B4 = cv.addWeighted(A6,1,A7,1,0)
    B5 = cv.addWeighted(A8,1,A9,1,0)
    C1 = cv.addWeighted(A0,1,B1,1,0)
    C2 = cv.addWeighted(B2,1,B3,1,0)
    C3 = cv.addWeighted(B4,1,B5,1,0)
    D1 = cv.addWeighted(C1,1,C2,1,0)
    E1 = cv.addWeighted(orange1_mask,1,orange2_mask,1,0)
    E2 = cv.addWeighted(orange3_mask,1,orange4_mask,1,0)
    E3 = cv.addWeighted(orange5_mask,1,orange6_mask,1,0)
    E4 = cv.addWeighted(orange7_mask,1,E1,1,0)
    E5 = cv.addWeighted(E2,1,E3,1,0)
    E6 = cv.addWeighted(E4,1,E5,1,0)
    E7 = cv.addWeighted(E6,1,C3,1,0)
    final_mask = cv.addWeighted(E7,1,D1,1,0)
    
    ### Reveal the final image, made of ALL masks
    cv.imshow('FINAL', final_mask)
    
    k = cv.waitKey(1)  & 0xFF
    if k == 27:
        break
        
    img = cv.imshow('image',img)
    
cv.destroyAllWindows()
