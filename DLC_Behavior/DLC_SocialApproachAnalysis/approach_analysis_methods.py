import sys
import os
import pandas as pd
from PIL import Image
import numpy as np
import cv2

class ApproachAnalysis_Organizer:
    # Constructor method to initialize the class
    def __init__(self, project_folder):
        self.project_folder = project_folder # Set the project folder
        self.directory_df = self.initialize_directory_df()  # Initialize the directory DataFrame

    def initialize_directory_df(self):
        directories = [d for d in os.listdir(self.project_folder) if os.path.isdir(os.path.join(self.project_folder, d))]
        directory_data = [{'directory_name': d, 'directory_path': os.path.join(self.project_folder, d)} for d in directories]
        return pd.DataFrame(directory_data, columns=['directory_name', 'directory_path'])
    
    def list_directories(self):
        return [d for d in os.listdir(self.project_folder) if os.path.isdir(os.path.join(self.project_folder, d))]
    
    def list_files(self, folder_name):
        folder_path = os.path.join(self.project_folder, folder_name)
        all_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                all_files.append(os.path.join(root, file))
        return all_files
    
class UserInput(ApproachAnalysis_Organizer):
    def __init__(self, project_folder):
        self.project_folder = project_folder # Set the project folder
        self.directory_df = self.initialize_directory_df()  # Initialize the directory DataFrame
        self.animal_data = {} # Initialize an empty dictionary to store animal IDs and treatments

    # Method to get user input for animal IDs and treatments
    def get_user_input(self):
        self.directory_df = self.initialize_directory_df()  # Initialize the directory DataFrame
        while True:
            animal_id = input('Enter the animal ID (or type "done" to finish): ')
            if animal_id.lower() == 'done':
                break  
            elif animal_id in self.directory_df['directory_name'].values:
                print(f'Animal ID {animal_id} already exists. Please enter a different animal ID.')
            else:
                treatments = self.get_treatments(animal_id)
                self.animal_data[animal_id] = treatments  
                    

                    os.makedirs(animal_folder) 
                for file in self.directory_df[self.directory_df['directory'].str.contains(animal_id)].values:
                    file_path = os.path.join(file[1], file[0])  # Get the full path of the file
                    os.rename(file_path, os.path.join(animal_folder, file[0]))  # Move the file to the appropriate folder
    
    

    
       