import cv2
import os 

# Load the pre-trained face cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load the image
image_path = os.getcwd()


image = cv2.imread(image_path + "/a.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

# Iterate through the detected faces
for (x, y, w, h) in faces:
    # Extract the face region


    print(x,y,w,h)
    face_roi = image[y:y + h, x:x + w]

    # Perform face manipulation or fitting here
    # You can resize, rotate, or apply other transformations to fit the face in the car front

# Display the original and modified images
try:
    cv2.imshow('Original Image', image)
    cv2.imshow('Modified Image', face_roi)
except:
    pass

cv2.waitKey(0)
cv2.destroyAllWindows()
