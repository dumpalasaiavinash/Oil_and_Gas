def upload_model(model_path,storage_account_name,storage_account_key,container_name,connection_string):
    from azure.storage.blob import BlobServiceClient
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(container=container_name,blob=model_path)
    with open(model_path, "rb") as data:
        blob_client.upload_blob(data, overwrite = True)
        print("uploaded model:",model_path)
