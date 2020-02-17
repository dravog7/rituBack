from storages.backends.azure_storage import AzureStorage
from os import environ
class AzureMediaStorage(AzureStorage):
    account_name = 'testhttp1234' # Must be replaced by your <storage_account_name>
    account_key = 'wkySBGV/zD9LZ15JYf5vxFUvQK4DCe7FkYDgnP9MRaeNne4lgmZF3yMnxH5+ky9UsJKPbohpsiyn5B8Gmz8NDA==' # Must be replaced by your <storage_account_key>
    azure_container = 'media'
    expiration_secs = None

class AzureStaticStorage(AzureStorage):
    account_name = 'testhttp1234' # Must be replaced by your storage_account_name
    account_key = 'wkySBGV/zD9LZ15JYf5vxFUvQK4DCe7FkYDgnP9MRaeNne4lgmZF3yMnxH5+ky9UsJKPbohpsiyn5B8Gmz8NDA==' # Must be replaced by your <storage_account_key>
    azure_container = 'static'
    expiration_secs = None