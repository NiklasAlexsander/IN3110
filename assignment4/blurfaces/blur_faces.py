import cv2
import sys, os
from blur3 import blur_3

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir, "modules"))


def main(size_of_loop):
    """
    Using cv2 face-detection to find the faces on the image 'beatles.jpg'.
    using a for-loop to go through as many blur-exections as inputed.
    Another blur on each face for each iteration. At the end a file will be
    saved in the same location as blur_faces.py is placed with a picture
    blurred, and if the faces still are being recognised by cv2, green rectangles
    will frame the faces. I reccomend around 300 iterations to get a picture
    where the recognition-algorithm fails. This will take around 3-6 minutes,
    depending on the hardware being used.

        args:
            size_of_loop(int): size of loop, number of blurs on each face found.
    """
    image = cv2.imread("beatles.jpg")
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

    print("running..")
    for m in range(size_of_loop):
        faces = faceCascade.detectMultiScale(image, scaleFactor=1.025, minNeighbors=5,
                                             minSize=(30, 30))
        for (x, y, w, h) in faces:
            image = blur_3.subsectBlur(image, x, y, w, h)
        print(m)

    faces = faceCascade.detectMultiScale(image, scaleFactor=1.025, minNeighbors=5,
                                         minSize=(30, 30))
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imwrite('blurred_face.jpg', image)


main(int(sys.argv[1]))
