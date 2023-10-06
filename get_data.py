def get_data(storage_account_name,storage_account_key,container_name,connection_string):
    import pandas as pd
    from azure.storage.blob import BlobServiceClient, generate_blob_sas, BlobSasPermissions
    from datetime import datetime, timedelta


    #create a client to interact with blob storage
    connect_str = connection_string
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)

    #use the client to connect to the container
    container_client = blob_service_client.get_container_client(container_name)

    #get a list of all blob files in the container
    blob_list = []
    for blob_i in container_client.list_blobs():
        blob_list.append(blob_i.name)

    print(blob_list)

    df_list = []
    #generate a shared access signiture for files and load them into Python
    for blob_i in blob_list:
        #generate a shared access signature for each blob file
        sas_i = generate_blob_sas(account_name = storage_account_name,
                                    container_name = container_name,
                                    blob_name = blob_i,
                                    account_key=storage_account_key,
                                    permission=BlobSasPermissions(read=True),
                                    expiry=datetime.utcnow() + timedelta(hours=1))
        
        sas_url = 'https://' + storage_account_name+'.blob.core.windows.net/' + container_name + '/' + blob_i + '?' + sas_i
        
        df = pd.read_csv(sas_url)
        df = df.reset_index(drop=True)
        df_list.append(df)
        
    

    df_combined = pd.concat(df_list, ignore_index=True)
    return(df_combined)