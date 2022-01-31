"""
@author: pritesh-mehta
"""

import argparse
from pathlib import Path
import numpy as np
import math
import scipy.ndimage as sy

import preprocessing_utilities.nifti_utilities as nutil

def in_plane_mask_crop(image_data, mask_nii, mask_data, crop_size):
    """in-plane crop using mask to image_data
    """    
    shape = np.shape(image_data)
    
    # get mask voxel spacing information
    hdr = mask_nii.header
    x_spacing, y_spacing, z_spacing = hdr.get_zooms()

    # find mask extremes
    slice_x, slice_y, slice_z = sy.find_objects(mask_data.astype(int))[0]
    x1 = (slice_x.start)
    x2 = (slice_x.stop)
    y1 = (slice_y.start)
    y2 = (slice_y.stop)
                
    # find mask centre in x and y
    x_center = math.floor((x1 + x2) / 2)
    y_center = math.floor((y1 + y2) / 2)
                
    x_rad = math.floor(crop_size / 2)
    y_rad = math.floor(crop_size / 2)
    
    x1 = max(x_center - x_rad, 0)
    x2 = min(x_center + x_rad, shape[0])
    y1 = max(y_center - y_rad,0)
    y2 = min(y_center + y_rad, shape[1])
    
    # apply crop
    image_data = image_data[x1:x2, y1:y2, :]
    
    # crop info
    left = x1 - 1
    right = shape[0] - x2
    top = y1 - 1
    bottom = shape[1] - y2
         
    return image_data, left, right, top, bottom

def in_plane_mask_crop_dir(image_dir, mask_dir, crop_size, output_dir, extension='.nii.gz'):
    """in-plane crop using mask_dir to image_dir
    """   
    filepaths = nutil.path_generator(image_dir, extension)
    for path in filepaths:
        # load data
        name, nii, data = nutil.load(path)
        # load mask
        mask_path = Path(mask_dir) / name
        mask_name, mask_nii, mask_data = nutil.load(mask_path)
        # crop
        print("Processing:", name)
        data, _, _, _, _ = in_plane_mask_crop(data, mask_nii, mask_data, crop_size)
        # save
        output_path = Path(output_dir) / name
        nutil.save(output_path, nii, data)
    return None
    
def process():
    parser = argparse.ArgumentParser()
    parser.add_argument('--image_dir', required=True, type=str)
    parser.add_argument('--mask_dir', required=True, type=str)
    parser.add_argument('--crop_size', required=True, type=int)
    parser.add_argument('--output_dir', required=True, type=str)
    parser.add_argument('--extension', required=False, type=str, default='nii.gz')

    args = parser.parse_args()
    
    in_plane_mask_crop_dir(args.image_dir, args.mask_dir, args.crop_size, args.output_dir, 
                  extension=args.extension)
    
if __name__ == "__main__":
    process()






    
