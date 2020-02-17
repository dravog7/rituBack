from storages.backends.azure_storage import AzureStorage
from os import environ
account_key = environ.get('ACCOUNT_KEY','testhttp1234')
account_name = environ.get('ACCOUNT_NAME','wkySBGV/zD9LZ15JYf5vxFUvQK4DCe7FkYDgnP9MRaeNne4lgmZF3yMnxH5+ky9UsJKPbohpsiyn5B8Gmz8NDA==')
class AzureMediaStorage(AzureStorage):
    account_name = account_name
    account_key = account_key
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = account_name
    account_key = account_key
    azure_container = 'static'
    expiration_secs = None