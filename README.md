
# Sign Detection - The Sole Sign Language Translator For You

Visit the working prototype [here](https://signpredictor.azurewebsites.net/)

## Motivation
To imitate a system that could in real-time convert sign language to voice. Such a system would be of immense use for the mute and deaf community when it comes to  interactions 
in their daily life.

## Acheived State
A simple platform that takes in a photo and predicts the Alphabet represented in the photo taken.

## Limitations

1. Not real-time
2. Azure Based Limitations (5000 images training only)
3. Current AI Model not that accurate

## Technologies Used

 <img src='https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white'>
 <img src='https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white'>
 <img src='https://img.shields.io/badge/microsoft%20azure-0089D6?style=for-the-badge&logo=microsoft-azure&logoColor=white'>
 
 ## Azure Services Used
 1. Azure Custom Vision (Prediction and Training)
 2. Azure Web App Service for Hosting
 
 ## DataSet Used
 
 The ASL dataset from [Kaggle](https://www.kaggle.com/grassknoted/asl-alphabet) was used for this project. Not all the images were used but 190 images of all the 26 alphabets were taken 
 randomly and used for training the azure custom vision model.
