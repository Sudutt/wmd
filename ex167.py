import cv2
import glob

flag=0  #Success of correct Path
while flag==0:
    try:
        global loc
        loc=input("Enter path: ")
        images = glob.glob(loc+"\\*.jpg")
        flag=1
    except:
        pass

if images==[]:
    print("Empty directory. No images found.")

for image in images:
    img=cv2.imread(image,0)
    cv2.imshow(image,img)#Here "image" is the filename, while "img" is the cv2 object- a numpy.ndarray
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    re=cv2.resize(img,(100,100))
    cv2.imshow(image+"_resized",re)
    cv2.waitKey(3000)
    cv2.destroyAllWindows()
    cur=image.rindex("\\")
    cv2.imwrite(image[:cur+1]+"resized_"+image[cur+1:],re)
