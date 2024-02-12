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
    
    def copy_and_sort_file_types(self,all_files):
        return [file for file in all_files if file.endswith('.csv') or file.endswith('.mp4') or file.endswith('.h5') or file.endswith()]




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
    
    # Method to get user input for animal IDs and treatments
    def get_user_input(self):
        self.animal_data = {} # Initialize an empty dictionary to store animal IDs and treatments
        while True:
            animal_id = input('Enter the animal ID (or type "done" to finish): ')
            if animal_id.lower() == 'done':
                break  
            elif animal_id in self.directory_df['directory'].values:
                print('Animal ID already exists. Please try again.')  
            else:
                treatments = self.get_treatments(animal_id)  # Get treatments for the animal ID
                if treatments:
                    self.animal_data[animal_id] = treatments  # Store the treatments in the animal_data dictionary

    # Method to get treatments for a given animal ID
    def get_treatments(self, animal_id):
        while True:
            treatments = input(f'Enter the three treatments for animal ID {animal_id}, separated by commas: ').split(',') #future: write a method that will loop through
            if len(treatments) == 3:
                return treatments 
            else:
                print('Invalid number of treatments. Please enter exactly three treatments.') 

    # Method to organize files based on animal IDs and treatments
    def organize_files(self):
        for animal_id, treatments in self.animal_data.items():  # Iterate over each animal ID and its treatments
            for treatment in treatments:
                treatment_folder = os.path.join(self.project_folder, treatment.strip())  # Create a path for the treatment folder
                if not os.path.exists(treatment_folder):
                    os.makedirs(treatment_folder)  
                animal_folder = os.path.join(treatment_folder, animal_id.strip())  # Create a path for the animal folder within the treatment folder
                if not os.path.exists(animal_folder):
                    os.makedirs(animal_folder) 
                for file in self.directory_df[self.directory_df['directory'].str.contains(animal_id)].values:
                    file_path = os.path.join(file[1], file[0])  # Get the full path of the file
                    os.rename(file_path, os.path.join(animal_folder, file[0]))  # Move the file to the appropriate folder
    
    

    
       