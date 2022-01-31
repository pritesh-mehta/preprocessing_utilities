"""
@author: pritesh-mehta
"""
from pathlib import Path
import numpy as np
import scipy.ndimage as sy
import math

import preprocessing_utilities.nifti_utilities as nutil

def pcf_mask_crop_dir(image_dir, mask_dir, output_dir, border=(5, 5, 0), extension='nii.gz'):
    """
    square crop x and y, crop z + border
    """
    
    mask_paths = nutil.path_generator(mask_dir, extension)
    for mask_path in mask_paths:
        mask_name, mask_nii, mask_data = nutil.load(mask_path)
        print("Processing:", mask_name)
        mask_data = mask_data.astype(int)
        
        # get mask voxel spacing information
        hdr = mask_nii.header
        x_spacing, y_spacing, z_spacing = hdr.get_zooms()

        # find mask extremes
        slice_x, slice_y, slice_z = sy.find_objects(mask_data)[0]
        x1=(slice_x.start)
        x2=(slice_x.stop) - 1
        y1=(slice_y.start)
        y2=(slice_y.stop) - 1
        z1=(slice_z.start)
        z2=(slice_z.stop) - 1
                
        mask_width = (x2 - x1 + 1)
        mask_height = (y2 - y1 + 1)
        mask_depth = (z2 - z1 + 1)
        
        crop_width = mask_width + 2 * border[0]
        crop_height = mask_height + 2 * border[1]
        crop_depth = mask_depth + 2 * border[2]
    
        #find mask centre
        x_center = math.floor((x1 + x2) / 2)
        y_center = math.floor((y1 + y2) / 2)
        z_center = math.floor((z1 + z2) / 2)
                    
        max_dim = max(crop_width * x_spacing, crop_height * y_spacing)
        x_rad = math.floor(max_dim / (2 * x_spacing))
        y_rad = math.floor(max_dim / (2 * y_spacing))
        z_rad = math.floor(crop_depth / 2)
        
        x1=max(x_center - x_rad, 0)
        x2=min(x_center + x_rad + 1, np.shape(mask_data)[0])
        y1=max(y_center - y_rad, 0)
        y2=min(y_center + y_rad + 1, np.shape(mask_data)[1])
        z1=max(z_center - z_rad, 0)
        z2=min(z_center + z_rad + 1, np.shape(mask_data)[2])
            
        # load image
        image_path = Path(image_dir) / mask_name
        image_name, image_nii, image_data = nutil.load(image_path)
    
        # apply crop
        image_data = image_data[x1:x2, y1:y2, z1:z2]
                    
        # save image
        output_path = Path(output_dir) / image_name
        nutil.save(output_path, image_nii, image_data)    
        
    return None






