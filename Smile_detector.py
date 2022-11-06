import cv2  # Importing opencv
from win32api import GetSystemMetrics # Importing GetsystemMetrices from win32api to get the size of the system or resolution of the screen

trained_face_data = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')  # Cascade for the frontal face detection 
trained_smile_data = cv2.CascadeClassifier('haarcascade_smile.xml')  # Cascade for detecting the smile of the person 

webcam = cv2.VideoCapture(0)  # Opens the webcam for capturing video at real time

#webcam = cv2.VideoCapture('test.mp4')  # Opens sample video provided to implement the detector
# Note : The video should be present in the same directory of the program created 


# Loop that will run till it has been externally terminated or there is no frame to be read 
while True:
    
    successful_frame_read, frame1 = webcam.read()  # Reading each of the frame from the source of video capture
    if not(successful_frame_read):  # If there is no frame to read
        break
    frame = cv2.resize(frame1, (GetSystemMetrics(0), GetSystemMetrics(1)))  # Resizing the frame recasting it to the systems screen size
    
    grayscaled_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Changing the color to gray
    
    face_coordinates = trained_face_data.detectMultiScale(grayscaled_img)  # Getting the face coordinates form the frame
    
    for (x, y, w, h) in face_coordinates:  # Iterating the (x, y, w, h) coordinate in the coordinates found for the face
        
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 4)  # Drawing the rectangle around the face
        
        the_face = frame[y:y+h, x:x+w]  # Retrieving only the part of the image where there is a face
        
        face_grayscaled = cv2.cvtColor(the_face, cv2.COLOR_BGR2GRAY)  # Changing the retrieved image to gray in color
        
        # Getting the smile coordinates from the face coordinates with a scale factor of 1.7 and neighbour of 20 recatngle each
        smile_coordinates = trained_smile_data.detectMultiScale(face_grayscaled, scaleFactor=1.7, minNeighbors=20)
        
        for (a, b, c, d) in smile_coordinates:  # Iterating the (a, b, c, d) coordinates in the smile coordinates
            
            cv2.rectangle(the_face, (a, b), (a+c, b+d), (0, 255, 0), 2)  # drawing rectangle around the smile
            
        if len(smile_coordinates) > 0:  # if the smile is found in the face
            
            # Then put the smiling text on the screen
            cv2.putText(frame, 'smiling', (x, y+h+40), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
            
    cv2.imshow('Smile Detector', frame)  # Showing the image with all the operations performed above 
    
    key = cv2.waitKey(1) # cv2.waitKey() allows users to display a window for given milliseconds or a key is pressed
    
    # continue till 'Enter' or 'Escape' is pressed
    if key == 13 or key == 27 :
        break

webcam.release()  # Realeasing the webcam 
cv2.destroyAllWindows()  # Destroying all the windows that were created
print("CODE  COMPLETED")

