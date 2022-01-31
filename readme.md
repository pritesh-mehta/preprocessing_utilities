# Preprocessing-Utilities

Repository containing miscellaneous preprocessing functions.

## Installation instructions 

1) Clone/download repository.

2) Change directory into repository.

3) Install:
	```
	pip install .
    ```
	
## How to use it 

- Function imports. 

- Command line:

	- mask_clean:
		```
		mask_clean --mask_dir .\sample_data\mask_clean\0_sample_highres3dnet_t2w_mask --ref_dir .\sample_data\mask_clean\0_sample_t2w --output_dir .\sample_data\mask_clean\1_highres3dnet_t2w_mask_clean
		```

	- in_plane_mask_crop:
		```
		in_plane_mask_crop --image_dir .\sample_data\in_plane_mask_crop\0_sample_t2w --mask_dir .\sample_data\in_plane_mask_crop\0_sample_mask --crop_size 256 --output_dir .\sample_data\in_plane_mask_crop\1_mask_crop_t2w
		```

	- scale:
		```
		scale --image_dir .\sample_data\scale\0_sample_adc --divisor 1000 --output_dir .\sample_data\scale\1_scaled_adc 
		```
	
	- whiten:
		```
		whiten --image_dir .\sample_data\whiten\0_sample_t2w --output_dir .\sample_data\whiten\1_whitened_t2w --mask_dir .\sample_data\mask_clean\1_highres3dnet_t2w_mask_clean
		```
