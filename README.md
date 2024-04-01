# Extracting Data from Bangla Handwritten forms using Computer Vision and Optical Character Recognition
 This project aims to automate the process of extracting data from handwritten Bangla forms using Computer Vision and Optical Character Recognition (OCR) techniques. The system employs a Convolutional Neural Network (CNN) model for character recognition, integrated with a Django backend for handling server-side operations. On the frontend, the application utilizes Python, React, and React Native for user interfaces across web and mobile platforms.
Introduction
The projects's primary goal is to extract data from handwritten forms written in Bangla. The system follows Client-Server Architecture. The server-side is developed using Python's Django framework. The server-side handles all the processing, like image processing and text recognition. We have used Python's OpenCV and PIL library for image processing. Then we used  OCR technology to recognize the values in the different fields of the forms. We trained our own OCR model using CNN to detect handwritten numbers in the forms. We used Ekush Data set to train our OCR model. The Client-side of the system consists of three applications. The first is a desktop application built using python; the second is a web application built using React framework; and the third is a mobile application for android devices. A designing software is also included in the desktop application, which users use to design forms. All the client-side applications communicate with the server-side using REST API. The users send captured images of the handwritten forms to the server from any client-side application. The server processes the image and sends the extracted data as a response. The data are presented to the users via GUI. These data can be stored in the database or on the user's local machine.

Usage
Start the Django backend server:

bash
Copy code
python manage.py runserver
Start the React frontend (for web):

bash
Copy code
cd frontend
npm start
For the mobile app (React Native):

bash
Copy code
cd mobile
npm start
Access the application through a web browser or deploy the mobile app to a device for mobile usage.
