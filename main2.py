import os
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()

def add_data():
    try:
        data_files = [('share/applications', ['extra/cheesemaker.desktop']),
                ('share/pixmaps', ['extra/cheesemaker.png'])]
        return data_files
    except:
        return

if os.name == 'posix':
    data_files = add_data()
else:
    data_files = None

setup(
    name = 'cheesemaker',
    version = '0.3.9',
    author='David Whitlock',
    author_email='alovedalongthe@gmail.com',
    url = 'https://github.com/riverrun/cheesemaker',
    description = 'A minimalistic image viewer using Python3 and PyQt5',
    long_description=long_description,
    license='GPLv3',
    packages = ['cheesemaker'],
    include_package_data=True,
    data_files=data_files,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Viewers',
    ],
    entry_points={
        'gui_scripts': [
            'cheesemaker = cheesemaker.gui:main',
            ]
        },
)