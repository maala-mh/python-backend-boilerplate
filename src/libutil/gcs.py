import os
import logging
from google.cloud import storage


logger = logging.getLogger(__name__)


def list_blobs(bucket_name) -> list[str]:
    """Lists all the blobs in the bucket."""
    logger.info("connecting to project {} bucket_name {}".format(os.environ['GCS_PROJECT'], bucket_name))
    storage_client = storage.Client(project=os.environ['GCS_PROJECT'])

    # Note: Client.list_blobs requires at least package version 1.17.0.
    blobs = storage_client.list_blobs(bucket_name)
    res = [blob.name for blob in blobs]
    return res

