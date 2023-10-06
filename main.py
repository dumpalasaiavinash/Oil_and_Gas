from get_data import get_data
from train import train
from upload_model import upload_model
import os

storage_account_key = "Zjsxqm/JPOIwuDm/4t/LX3HCw6861fidnNibM59GJXx0Tvwm+b3XcDvYVewk0luSc+m6DwVKOMmx+AStyKTuDw=="
storage_account_name = "storageavinash"
data_container_name = 'containeravinash'
models_container_name = "models"
connection_string = "DefaultEndpointsProtocol=https;AccountName=storageavinash;AccountKey=Zjsxqm/JPOIwuDm/4t/LX3HCw6861fidnNibM59GJXx0Tvwm+b3XcDvYVewk0luSc+m6DwVKOMmx+AStyKTuDw==;EndpointSuffix=core.windows.net"

# get the data to train from azure storage
data = get_data(storage_account_name,storage_account_key,data_container_name,connection_string)
# Send data to train function
model_path = train(data)
# uploading the model to azure storage
upload_model(model_path,storage_account_name,storage_account_key,models_container_name,connection_string)

# deleting the uploded model file
if os.path.exists(model_path):
  os.remove(model_path)
else:
  print("model file does not exist")

