from google.cloud import secretmanager
import os

project_id = os.environ.get('PROJECT', 'gts-atr3-sbox')


def secret_manager(secret_id):
    '''
        THIS FUNCTION IS USED FOR LOCAL TESTING, WE ACCES THE SECRETS 
        USING THE SAME SERVICE ACCOUNT OF THE CLOUD RUN
    '''
    # pass
    name = "projects/{}/secrets/{}/versions/latest".format(project_id, secret_id)
    client = secretmanager.SecretManagerServiceClient()
    # Access the secret version.
    response = client.access_secret_version(name=name)

    # Print the secret payload.
    #
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    payload = response.payload.data.decode("UTF-8")
    return payload