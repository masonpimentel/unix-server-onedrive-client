import os
from lib.debugging import *
from lib.utils import *


def fs_get_local_filename(dev_upload_pair_index):
    dev_paths = config_get_dev_paths()
    return os.path.basename(dev_paths["upload_pairs"][dev_upload_pair_index])


def fs_get_filename(filename):
    return os.path.basename(filename)


def fs_get_upload_size(dev_upload_pair_index):
    dev_paths = config_get_dev_paths()
    try:
        size = os.stat(dev_paths["upload_pairs"][dev_upload_pair_index]).st_size
        return size
    except FileNotFoundError as e:
        print_message("File path '" + dev_paths["upload_pairs"][dev_upload_pair_index] + "' could not be found!", "UPLOAD", "error")
        raise e

def fs_get_chunk_size(filename):
    return os.stat(filename).st_size


def fs_get_parent_dir():
    return os.path.dirname(os.getcwd())


def fs_get_chunk_full_path(tmpdirname, chunk_name):
    return os.path.join(tmpdirname, chunk_name)
