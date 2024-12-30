import os
import sys
from src.logger import logging
from src.exception import CustomException
import pandas as pd

from src.components.data_ingetion import DataIngestion
from src.components.data_trans import DataTransformation
from src.components.model_train import ModelTrainer



if __name__=="__main__":
    obj = DataIngestion()
    train_path,test_path = obj.initiate_data_ingestion()
    data_trans_obj = DataTransformation()
    train_arr,test_arr,_ = data_trans_obj.initaite_data_transformation(train_path,test_path)
    model_trainer=ModelTrainer()
    model_trainer.initate_model_training(train_arr,test_arr)