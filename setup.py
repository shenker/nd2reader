from distutils.core import setup

VERSION = "1.0.1"

setup(
    name="nd2reader",
    packages=['nd2reader', 'nd2reader.model'],
    version=VERSION,
    description='A tool for reading ND2 files produced by NIS Elements',
    author='Jim Rybarski',
    author_email='jim@rybarski.com',
    url='https://github.com/jimrybarski/nd2reader',
    download_url='https://github.com/jimrybarski/nd2reader/tarball/%s' % VERSION,
    keywords=['nd2', 'nikon', 'microscopy', 'NIS Elements'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: Science/Research',
                 'License :: Freely Distributable',
                 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python :: 2.7',
                 'Programming Language :: Python :: 3.4',
                 'Topic :: Scientific/Engineering',
                 ]
)