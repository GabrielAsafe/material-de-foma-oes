import cv2
import os
import time


def prepare():

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    nose_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_nose.xml')
    mouth_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_mcs_mouth.xml')
    eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_tree_eyeglasses.xml')



    #Tempo de espera em segundos antes de capturar a foto
    tempo_espera = 7  # Ajuste conforme necessário

    # Marca de tempo inicial
    tempo_inicial = time.time()



    # Open the camera (default camera or a specific camera index)
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera

    while True:
        # Read a frame from the camera
        ret, frame = cap.read()

        # Convert the frame to grayscale for face detection
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform face detection
        faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.3, minNeighbors=5)

        # Check if at least one face is detected
        if len(faces) > 0:
            # Assuming only one face is detected (you can modify this part if multiple faces are detected)
            (x, y, w, h) = faces[0]

            # Crop the region of interest (ROI) around the detected face
            roi = frame[y:y+h, x:x+w]

        # Perform nose detection within the face region
            noses = nose_cascade.detectMultiScale(roi)
            for (nx, ny, nw, nh) in noses:
                #cv2.rectangle(roi, (nx, ny), (nx+nw, ny+nh), (0, 0, 0), 0)
                croppedn = roi[ny:ny+nh,nx:nx+nw]
            cv2.imwrite(os.getcwd()+ "/nariz.jpg",croppedn)

            # Perform mouth detection within the face region
            mouths = mouth_cascade.detectMultiScale(roi)
            for (mx, my, mw, mh) in mouths:
                #cv2.rectangle(roi, (mx, my), (mx+mw, my+mh), (0, 0, 0), 0)
                croppedm = roi[my:my+mh,mx:mx+mw]
            
            cv2.imwrite(os.getcwd()+ "/boca.jpg",croppedm)


            # Perform mouth detection within the face region
            eye = eye_cascade.detectMultiScale(roi)
            for (mx, my, mw, mh) in eye:
                #cv2.rectangle(roi, (mx, my), (mx+mw, my+mh), (0, 0, 0), 0)
                cropped = roi[my:my+mh,mx:mx+mw]
            cv2.imwrite(os.getcwd()+ "/olho.jpg",cropped)


        # Display the original frame
        cv2.imshow('Original Frame', frame)

        # Verificar se o tempo de espera passou
        if time.time() - tempo_inicial > tempo_espera:
            # Capturar uma foto
            cv2.imwrite('path/to/save/foto_capturada.jpg', frame)
            print(f"Foto capturada após {tempo_espera} segundos.")
            break

        # Break the loop if the 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()
