"""
@author: pritesh-mehta
"""

import argparse
from pathlib import Path
import numpy as np

import preprocessing_utilities.nifti_utilities as nutil

def whiten(data, mask_data=None):
    """image whitening normalization
    """ 
    if mask_data is None:
        masked_data = data
    else: 
        mask_data = np.squeeze(np.round(mask_data))
        masked_data = np.multiply(data, mask_data)
        masked_data[masked_data == 0] = np.nan

    # mean-variance normalisation
    data = data - np.nanmean(masked_data)
    data = data / np.nanstd(masked_data)       
    return data

def whiten_dir(image_dir, output_dir, mask_dir=None, extension='.nii.gz'):
    """image whitening normalization
    """   
    filepaths = nutil.path_generator(image_dir, extension)
    for path in filepaths:
        # load data
        name, nii, data = nutil.load(path)
        print("Processing:", name)
        if mask_dir:
            mask_path = Path(mask_dir) / name
            ma_name, ma_nii, ma_data = nutil.load(mask_path)
            data = whiten(data, ma_data)
        else:
            data = whiten(data)
        # save
        output_path = Path(output_dir) / name
        nutil.save(output_path, nii, data)
    return None
    
def process():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', required=True, type=str)
    parser.add_argument('--output_dir', required=True, type=str)
    parser.add_argument('--mask_dir', required=False, type=str)
    parser.add_argument('--extension', required=False, type=str, default='.nii.gz')

    args = parser.parse_args()
    
    whiten_dir(args.image_dir, args.output_dir, mask_dir=args.mask_dir, 
               extension=args.extension)
    
if __name__ == "__main__":
    process()





