# Smile_detector_using_opencv
 This is a simple project and an extension of the face detector where in we are detecting the smile of the person.
 
 This project uses some important concept of **Haarcascade**,_" Haar cascade is an algorithm that can detect objects in images, irrespective of their scale in image and location"._
 
 **Opencv** which is an popular open source computer vision and machine learning software library.
 
 The project first uses opencv method to use the camera of your device or an sample input video , then uses haarcascade_fronatalface_alt2 to train itself to detect the face . Then once trained it retirves the face from the faces read by opencv's method "webcam.read()".
 Then once the face's coordinates are retrieved then the other trained cascade classifier for smile detection detects smile and retrives it's coordinates.
 A rectangle of red colour is drawn around the face and of colour green around the smile.
 And at last the frame is shown with all the operation done.
