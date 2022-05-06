from trainingModel import trainModel
import json
import os

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

if __name__ == "__main__":
    try:
        trainModelObj = trainModel()  # object initialization
        trainModelObj.trainingModel()  # training the model for the files in the table
    except Exception as e:
        ##print("Error occured: " + str(e))
        raise e