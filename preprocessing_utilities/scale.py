"""
@author: pritesh-mehta
"""

import argparse
from pathlib import Path

import preprocessing_utilities.nifti_utilities as nutil

def scale_dir(image_dir, divisor, output_dir, extension='.nii.gz'):
    """scale voxel values
    """   
    filepaths = nutil.path_generator(image_dir, extension)
    for path in filepaths:
        # load data
        name, nii, data = nutil.load(path)
        print("Processing:", name)
        data = data / divisor
        # save
        output_path = Path(output_dir) / name
        nutil.save(output_path, nii, data)
    return None
    
def process():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', required=True, type=str)
    parser.add_argument('--divisor', required=True, type=int)
    parser.add_argument('--output_dir', required=True, type=str)
    parser.add_argument('--extension', required=False, type=str, default='.nii.gz')

    args = parser.parse_args()
    
    scale_dir(args.image_dir, args.divisor, args.output_dir, 
                extension=args.extension)
    
if __name__ == "__main__":
    process()





