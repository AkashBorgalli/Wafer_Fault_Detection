from azureml.core import Experiment, ScriptRunConfig, Environment
from azureml.core import Workspace
from azureml.widgets import RunDetails
from azureml.core.runconfig import DockerConfiguration
from trainingModel import trainModel
# Create a script config
myenv = Environment.from_conda_specification(name = "wafer-env",
                                             file_path = "environment.yml")

script_config = ScriptRunConfig(source_directory='./scripts',
                                script='main.py',
                                environment=myenv 
                                                             
                                )

if __name__ == "__main__":
    experiment = Experiment(workspace=Workspace.from_config(), name='Wafer-fault-detection')
    run = experiment.submit(config=script_config)
    ##RunDetails(run).show()
    ##run.wait_for_completion()
