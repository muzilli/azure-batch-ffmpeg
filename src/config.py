# -------------------------------------------------------------------------
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND,
# EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE IMPLIED WARRANTIES
# OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR PURPOSE.
# ----------------------------------------------------------------------------------
# The example companies, organizations, products, domain names,
# e-mail addresses, logos, people, places, and events depicted
# herein are fictitious. No association with any real company,
# organization, product, domain name, email address, logo, person,
# places, or events is intended or should be inferred.
# --------------------------------------------------------------------------

# Global constant variables (Azure Storage account/Batch details)

# import "config.py" in "batch_python_tutorial_ffmpeg.py"

# Update the Batch and Storage account credential strings below with the values
# unique to your accounts. These are used when constructing connection strings
# for the Batch and Storage client objects.

_BATCH_ACCOUNT_NAME = 'batrseus001'  # Your batch account name
_BATCH_ACCOUNT_KEY = 'KZR44AGFgFDG25GWpyHEZ6LMBfWTht1j9s5NsI1ojlMRk20LFmqFnheBV0LhAS7m+7vFnfDgVoYGL2nr5oWjPg=='  # Your batch account key
_BATCH_ACCOUNT_URL = 'https://batrseus001.eastus.batch.azure.com'  # Your batch account URL
_STORAGE_ACCOUNT_NAME = 'strseus001'  # Your storage account name
_STORAGE_ACCOUNT_KEY = 'D6F1VeB6QHLQMiiZN4X2rGWpbtW+XbFi6SIwCsDtPqCE2uDbn6BbY30Ruf7LWZlz+4kowsjf+BCeuLfk5D2tag=='  # Your storage account key
_STANDARD_OUT_FILE_NAME = 'stdout.txt'  # Standard Output file
_POOL_ID = 'LinuxFfmpegPool'
_DEDICATED_POOL_NODE_COUNT = 0
_LOW_PRIORITY_POOL_NODE_COUNT = 5
_POOL_VM_SIZE = 'STANDARD_A1_v2'
_JOB_ID = 'LinuxFfmpegJob'
