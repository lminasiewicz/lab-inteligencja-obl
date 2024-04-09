import numpy as np
from os import listdir, makedirs, rename
from os.path import isdir
from random import random

def relocate_and_split(validation_ratio: float = 0.3, src_path: str = "dogs-cats-mini/") -> None:
    for file in listdir(src_path):
        file_src = src_path + "/" + file
        destination = "dogs-cats-mini/train/"
        if random() < validation_ratio:
            destination = "dogs-cats-mini/test/"

        if file.startswith("cat."):
            destination = destination + "cats/" + file[4:]
            rename(file_src, destination)
        if file.startswith("dog."):
            destination = destination + "dogs/" + file[4:]
            rename(file_src, destination)



def gather_in_main_folder(main_folder: str = "dogs-cats-mini/") -> None:
    catdirs = ["dogs-cats-mini/train/cats/", "dogs-cats-mini/test/cats/"]
    dogdirs = ["dogs-cats-mini/train/dogs/", "dogs-cats-mini/test/dogs/"]
    for dir in catdirs:
        for file in listdir(dir):
            file_src = dir + "/" + file
            new_name = "cat." + file
            destination = main_folder + "/" + new_name
            rename(file_src, destination)
    
    for dir in dogdirs:
        for file in listdir(dir):
            file_src = dir + "/" + file
            new_name = "dog." + file
            destination = main_folder + "/" + new_name
            rename(file_src, destination)



def main() -> None:
    dataset_folder = 'dogs-cats-mini/'
    subdirs = ['train/', 'test/']
    if not isdir(dataset_folder): raise FileNotFoundError("Dataset Folder not found in your current directory. Check if you're launching the code from the correct directory.")
    for subdir in subdirs:
        labeldirs = ['dogs/', 'cats/']
        for labeldir in labeldirs:
            newdir = dataset_folder + subdir + labeldir
            makedirs(newdir, exist_ok=True)
            print(newdir)
    
    # RUN ONLY ONE OF THESE
    relocate_and_split() # move all images from main folder to train/test and cat/dog folders
    # gather_in_main_folder() # move all images from train/test and cat/dog folders to main folder



if __name__ == "__main__":
    main()