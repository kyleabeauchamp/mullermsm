from glob import glob
from setuptools import setup

setup(name='mullermsm',
      version='0.1',
      author='Robert McGibbon',
      author_email='rmcgibbo@gmail.com',
      url='https://github.com/rmcgibbo/mullermsm',
      description='Markov State Models on the Muller potential -- a MSMBuilder Tutorial',
      license='GPLv3  <http://www.gnu.org/licenses/gpl.html>',
      classifiers = ['Topic :: Scientific/Engineering :: Information Analysis',
                     'Topic :: Scientific/Engineering :: Chemistry',
                     'Topic :: Scientific/Engineering :: Physics',
                     'Topic :: Scientific/Engineering :: Bio-Informatics',
                     'Development Status :: 3 - Alpha',
                     'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
                     'Operating System :: OS Independent',
                     'Programming Language :: Python :: 2.7',
                     'Intended Audience :: Science/Research',],
      install_requires=['theano==0.5.0'],
      include_package_data=True,
      package_data = {'': ['conf.pdb']},
      packages=['mullermsm'],
      package_dir={'mullermsm':'lib'},
      scripts=glob('scripts/*.py'))
