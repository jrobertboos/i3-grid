from setuptools import setup

def readme():
    with open('README.org') as f:
        return f.read()

setup(name='i3grid',
      version='0.1',
      description='i3 grid manager',
      long_description=readme(),
      long_description_content_type='text/markdown',
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Programming Language :: Python :: 3.8',
          'Topic :: Desktop Environment :: Window Managers',
      ],
      keywords='i3grid i3 i3wm extensions add-ons',
      url='https://github.com/jrobertboos/i3-grid',
      author='JR Boos',
      author_email='j.robert.boos@gmail.com',
      license='MIT',
      packages=['i3grid'],
      install_requires=[
          'i3ipc',
      ],
      entry_points ={
          'console_scripts': ['i3-grid=i3grid.i3_grid:main'],
      },
      zip_safe=False)
