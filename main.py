# creates a picture from a folder of pictures
# Take note that it takes a long time to create a picture from smaller
# sizes of the pictures (pixelSize) but it does look better
import numpy as np
from PIL import Image
import os
import datetime

# picture path
picPath = "Mom's Garden\\garden\\DSC05042.JPG"
img = Image.open(picPath)
# the approximate size of each of the pictures in the main picture
pixelSize = 25

imgSize = img.size
img = img.resize((int(img.size[0] / pixelSize), int(imgSize[1] / pixelSize)))
img_arr = np.array(img.convert("RGB"))
# print(len(img_arr), len(img_arr[0]))
img_list = []
img = img.resize(imgSize, Image.NONE)
# img.show()
# print(img_arr)
images = {}
# path of folders with pictures
folder_path = "Mom's Garden\\garden"
for filename in os.listdir(folder_path):
    # makes sure that it is a picture
    if filename[-3:len(filename)].lower() == "png" or filename[-3:len(filename)].lower() == "jpg":
        path = folder_path + "\\" + filename
        pic = Image.open(path)
        # gets the approximate pixel colors in each of the pictures in the folder
        pic = pic.resize((1, 1))
        pic_arr = np.array(pic.convert("RGB"))[0][0]
        # puts the pixel in a dictionary that has paths as keys
        images[path] = pic_arr.tolist()

# print(images)
images_vals = list(images.values())
images_keys = list(images.keys())

print("25%")


# checks if two pixels are close enough to be the same
def similar(main_pixel, img_pixel, k):
    if main_pixel[0] - k <= img_pixel[0] <= main_pixel[0] + k:
        if main_pixel[1] - k <= img_pixel[1] <= main_pixel[1] + k:
            if main_pixel[2] - k <= img_pixel[2] <= main_pixel[2] + k:
                return True
    return False


# makes a list of images based on each of the pixels using the dictionary
full = []
for i in range(len(img_arr)):
    row = []
    for j in range(len(img_arr[i])):
        pixel = img_arr[i][j].tolist()
        k = 5
        while k < 256:
            k += 25
            for val in images_vals:
                if similar(pixel, val, k):
                    row.append(val)
                    k = 300
                    break
    full.append(row)


# turns a 2d list of images into a main image based on the original image
def makeImg(imgList):
    data = np.zeros((len(imgList) * pixelSize, len(imgList[0]) * pixelSize, 3), dtype=np.uint8)
    for i in range(len(imgList)):
        for j in range(len(imgList[0])):
            pixel_array = np.array(imgList[i][j])
            for k in range(len(pixel_array)):
                row = pixel_array[k]
                for l in range(len(row)):
                    data[i * pixelSize + k][j * pixelSize + l] = pixel_array[k][l]
    print("99%")
    pic = Image.fromarray(data, "RGB")
    return pic


print("50%")
# makes a 2d list of images based on a 2d list of pixels
listImgs = []
for row in full:
    rowImgs = []
    for pix in row:
        pic = Image.open(images_keys[images_vals.index(pix)])
        pic = pic.resize((pixelSize, pixelSize)).convert("RGB")
        rowImgs.append(pic)
    listImgs.append(rowImgs)
print("75%")

picture = makeImg(listImgs)
# saves the image in the same directory
picture.save("pic from pics.jpg")
# displays the image
picture.show()


# everything below are previous trials and tests
# |
# |
# |
# v 


# def turnInToPixels(image, numPix):
#     regSize = image.size
#     pic = image.resize((numPix, numPix))
#     print(pic.size)
#     pic = pic.resize(regSize)
#     return pic
#
#
# img = Image.open("code.jpg")
# img = turnInToPixels(img, pix_size)
# img_arr = np.array(img.convert("RGB")).tolist()
# print(len(img_arr) * len(img_arr[0]))


# given a list of pictures
# convert all to jpg
# then find size of image trying to make
# then find the size that should be for the rest of the images by dividing
#   the size by number of photos or something (this is optional)
# then get the average colour of each photo by doing the resize and then just make a dictionary (or something)
# then make a function to get the approximate nearest value so like maybe make a dictionary of the colours


# 100
# 50
# 50

# for i in range(0, len(img_arr[0]), pixelSize):
#     for j in range(0, len(img_arr), pixelSize):
#         print(i, j)


# def colours_list(image, pixSize):
#     colours = []
#     # turn into array
#     pic_arr = np.array(image.convert("RGB"))
#     # iterates through "pixels" of the picture, so row first then height
#     for i in range(0, len(pic_arr), pixSize):
#         if (len(pic_arr) - i >= pixSize):
#             row = []
#             for j in range(0, len(pic_arr[i]), pixSize):
#                 if (len(pic_arr[i]) - j >= pixSize):
#                     arr = pic_arr[i:i + pixSize][0][j:j + pixSize]
#                     red, green, blue = 0, 0, 0
#                     for pixel in arr:
#                         red += pixel[0] / pixSize
#                         green += pixel[1] / pixSize
#                         blue += pixel[2] / pixSize
#                     color = [int(red), int(green), int(blue)]
#                     # print(color)
#                     row.append(color)
#             colours.append(row)
#     return colours
#
#
# def findCloseList(bigPixel, smalPixel, num):
#     fax = True
#     if not (bigPixel[0] - num <= smalPixel[0] <= bigPixel[0] + num):
#         fax = False
#     if not (bigPixel[1] - num <= smalPixel[1] <= bigPixel[1] + num):
#         fax = False
#     if not (bigPixel[2] - num <= smalPixel[2] <= bigPixel[2] + num):
#         fax = False
#     return fax
#
#
# # find the closest color
#
# def findClosestColor(pixels, img2, k):
#     img = img2.resize((1, 1))
#     img_pixel = np.array(img.convert("RGB")).tolist()[0][0]
#     for i in range(len(pixels)):
#         for j in range(len(pixels[0])):
#             if pixels[i][j] == img_pixel:
#                 pixels[i][j] = [-99999, -99999, -99999]
#                 return [i, j]
#             else:
#                 if findCloseList(pixels[i][j], img_pixel, k):
#                     pixels[i][j] = [-99999, -99999, -99999]
#                     return [i, j]
#                 else:
#                     return None
#
#
# def turnIntoImage(pixel_array, pix_size):
#     data = np.zeros((len(pixel_array), len(pixel_array[0]), 3), dtype=np.uint8)
#     for i in range(len(pixel_array)):
#         for j in range(len(pixel_array[0])):
#             data[i][j] = pixel_array[i][j]
#     img = Image.fromarray(data, "RGB")
#     img = img.resize((len(data[0]) * pix_size, len(data) * pix_size), Image.NONE)
#     return img
#
#
# pix_size = 1000
#
# img = Image.open("Mom's Garden\\garden\\DSC05042.JPG")
# print(img.size)
# # print(img.size)
# arr = colours_list(img, pix_size)
# pixelated = turnIntoImage(arr, pix_size)
# # pixelated.show()
#
# def imageUsingImages(images, numPix):
#     full = []
#     for row in images:
#         fullRow = []
#         for i in range(numPix):
#             for j in range(len(row)):
#                 img_arr = np.array(row[j].convert("RGB"))
#                 for pixel in img_arr[i]:
#                     fullRow.append(pixel)
#         full.append(fullRow)
#
#     return turnIntoImage(full, numPix)
#
#
# def createImage(pixelated, arr, pix_size):
#     img_arr = np.array(pixelated.convert("RGB")).tolist()
#     images = [[[] for i in range(int(len(img_arr)/pix_size))] for j in range(int(len(img_arr[0])/pix_size))]
#     for i in range(0, len(img_arr[0]), pix_size):
#         # print(i, end="")
#         for j in range(0, len(img_arr), pix_size):
#             # print(j)
#             k = 255
#             while k < 256:
#                 k += 25
#                 # print(k)
#                 for filename in os.listdir("Mom's Garden\\garden"):
#                     if filename[-3:len(filename)].lower() == "png" or filename[-3:len(filename)].lower() == "jpg":
#                         # print(filename)
#                         path = "Mom's Garden\\garden\\" + filename
#                         img = Image.open(path)
#                         index = findClosestColor(img_arr, img, k)
#                         # print(index)
#                         if index:
#                             # print("true")
#                             k = 256
#                             resizedImg = img.resize((pix_size, pix_size))
#                             # print(resizedImg)
#                             images[index[0]][index[1]] = resizedImg
#     return images
#
#
# img = createImage(pixelated, arr, pix_size)
# print(img)
# img_arr = np.array(pixelated.convert("RGB")).tolist()


# createImage(pixelated, arr, pix_size)

# for filename in os.listdir(folder_pics_path):
#     path = folder_pics_path + "\\" + filename
#     pic = Image.open(path)
#     pic_array.append(pic)
#     pix.append(pic.resize((size, size)))
#
# pixel_array = []
# for pic2 in pix:
#     pic = pic2.convert("RGB")
#     pic_arr = np.array(pic).tolist()
#     # print(pic_arr)
#     # for row in pic_arr:
#     #     pixel_array.append(row)
# print(datetime.datetime.now())
# for i in range(size):
#     pixels = []
#     for j in range(len(pix)):
#         for thing in np.array(pix[j].convert("RGB")).tolist()[i]:
#             pixels.append(thing)
#     pixel_array.append(pixels)
# print(datetime.datetime.now())
# data = np.zeros((len(pixel_array), len(pixel_array[0]), 3), dtype=np.uint8)
# for i in range(len(pixel_array)):
#     for j in range(len(pixel_array[0])):
#         data[i][j] = pixel_array[i][j]
# print(datetime.datetime.now())
#
# img = Image.fromarray(data, "RGB")
# img.show()

# print(pix)

# pic = Image.open("code.jpg")
#
# size = pic.size
#
# numPix = size[0]*size[1]
# pic_array = np.array(pic).tolist()
#
# red, green, blue = 0, 0, 0
#
# for row in pic_array:
#     for pixel in row:
#         red += pixel[0]
#         green += pixel[1]
#         blue += pixel[2]
#
# print(red, green, blue)
#
# redPix = int(red/numPix)
# greenPix = int(green/numPix)
# bluePix= int(blue/numPix)
#
# data = np.zeros((512,512,3), dtype=np.uint8)
#
# data[256,256] = [redPix, greenPix, bluePix]
#
# img = Image.fromarray(data, "RGB")
# img.save("code2.png")
# img.show()
#
# def get_image_res(image):
#     return image.size
#
#
# #
# # print(get_image_res(pic))
# #
# def resize_image(image, height, width):
#     # height first them width
#     resized_image = image.resize((height, width))
#     return resized_image

# resized_image= resize_image(pic, 1,1)
# resized_image.show()
