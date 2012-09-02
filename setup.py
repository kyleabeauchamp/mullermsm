from glob import glob
from setuptools import setup

setup(name='mullermsm',
      version='0.1',
      license='GPLv3',
      include_package_data=True,
      package_data = {'': ['conf.pdb']},
      packages=['mullermsm'],
      #install_requires=['theano', 'numpy', 'matplotlib', 'ipython'],
      package_dir={'mullermsm':'lib'},
      scripts=glob('scripts/*.py'))
