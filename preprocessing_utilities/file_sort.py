"""
@author: pritesh-mehta
"""

import os
import shutil

def file_sort(file_dir, sort_str, extension='.nii.gz'):
    '''move files containing sort_str to a folder named sort_str
    '''
    sub_dir = os.path.join(file_dir, sort_str)
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)
    file_list = [_ for _ in os.listdir(file_dir) if _.endswith(extension)]
    for file in file_list:
        print("Sorting:", file)
        if sort_str in file:
            old_path = os.path.join(file_dir, file)
            new_path = os.path.join(sub_dir, file.replace("_" + sort_str, ""))
            shutil.move(old_path, new_path)
    return None
            
            
