import pandas as pd
from azureml.core import Workspace, Dataset, Run
from base_config import config

class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training from azure.

    Written By: Akash Borgalli
    Version: 1.0
    Revisions: None

    """
    def __init__(self, file_object, logger_object):
        self.fetch_data=config() 
        self.file_object=file_object
        self.logger_object=logger_object

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception

         Written By: Akash Borgalli
        Version: 1.0
        Revisions: None

        """
        self.logger_object.log(self.file_object,'Entered the get_data method of the Data_Getter class')
        try:
            self.workspace = Workspace(self.fetch_data.subscription_id, self.fetch_data.resource_group, self.fetch_data.workspace_name)
            self.dataset = Dataset.get_by_name(self.workspace, name=self.fetch_data.data_set)
            self.data = self.dataset.to_pandas_dataframe()
            self.logger_object.log(self.file_object,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()


