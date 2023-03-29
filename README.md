# Pothole Recognition
### By Taro Iyadomi
##### March 7 - March 29, 2023

[:star: Link to Demo :star:](https://replit.com/@taroii/pothole-detection?v=1) 

This project is part of AI Camp's Summer 2023 Data Science Internship training program. The goal of this project is to build a computer vision application from start to finish, using technologies like SerpAPI, PyTorch, HuggingFace, and Flask.  

Using images of roads with potholes and without potholes, the goal of our model is to detect the existence of potholes in those images. Naturally, these images have varying degrees of pothole-intensity (ie how big the pothole is), so we can enhance this model to classify the potholes into different intensity categories, as well as calculate their likelihoods of causing tire damage for sedans, crossovers, SUVs, etc.  

As we see many companies collecting street data for self-driving cars, perhaps some of that data can be utilized by local governmental organizations to help improve the condition of roads by being able to quantify which roads need the most care (we can use # of potholes or average pothole intensity) as well as where these potholes occur. For example, this can be done using Google’s Streetview, since we can use images of roads for our model and map those results to specific streets to help accomplish this task.  
