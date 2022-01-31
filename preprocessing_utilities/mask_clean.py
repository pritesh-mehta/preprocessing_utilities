"""
@author: pritesh-mehta
"""

import argparse
from pathlib import Path
import numpy as np

import preprocessing_utilities.nifti_utilities as nutil

def mask_clean_dir(mask_dir, ref_dir, output_dir, threshold=0.51, remove_str=None, extension='.nii.gz'):
    """clean masks 
        1. threshold
        2. set values to int
        3. save with ref header
        4. remove string from filename (optional)
    """   
    filepaths = nutil.path_generator(mask_dir, extension)
    for path in filepaths:
        # load mask
        name, nii, data = nutil.load(path)
        if remove_str:
            name = name.replace(remove_str, "")
        # load ref
        ref_path = Path(ref_dir) / name
        ref_name, ref_nii, ref_data = nutil.load(ref_path)
        # binarize
        print("Processing:", name)
        data = (data >= threshold) * 1
        # to int
        data = data.astype(int)
        # squeeze
        data = np.squeeze(data)
        # save
        output_path = Path(output_dir) / name
        nutil.save(output_path, ref_nii, data)
    return None
    
def process():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mask_dir', required=True, type=str)
    parser.add_argument('--ref_dir', required=True, type=str)
    parser.add_argument('--output_dir', required=True, type=str)
    parser.add_argument('--threshold', required=False, type=float, default=0.51)
    parser.add_argument('--remove_str', required=False, type=str, default=None)
    parser.add_argument('--extension', required=False, type=str, default='.nii.gz')

    args = parser.parse_args()
    
    mask_clean_dir(args.mask_dir, args.ref_dir, args.output_dir, threshold=args.threshold, 
                            remove_str=args.remove_str, extension=args.extension)
    
if __name__ == "__main__":
    process()






    
