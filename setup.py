"""
@author: pritesh-mehta
"""

from setuptools import setup, find_packages

setup(name='preprocessing_utilities',
      version='1.0',
      description='Preprocessing utilities',
      url='https://github.com/pritesh-mehta/preprocessing_utilities',
      python_requires='>=3.6',
      author='Pritesh Mehta',
      author_email='pritesh.mehta@kcl.ac.uk',
      license='Apache 2.0',
      zip_safe=False,
      install_requires=[
      'numpy',
      'scipy',
      'pathlib',
      'argparse',
      'nibabel',
      ],
      entry_points={
        'console_scripts': [
            'mask_clean=preprocessing_utilities.mask_clean:process',
            'in_plane_mask_crop=preprocessing_utilities.in_plane_mask_crop:process',
            'scale=preprocessing_utilities.scale:process',
            'whiten=preprocessing_utilities.whiten:process',
            ],
      },
      packages=find_packages(include=['preprocessing_utilities']),
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
      ]
      )