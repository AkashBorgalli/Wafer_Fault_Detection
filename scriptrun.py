from azureml.core import Run

class Runobject:
    def __init__(self):
        self.run = Run.get_context()
    
    def get_run_object(self):
        return self.run
    

