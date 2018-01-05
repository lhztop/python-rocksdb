from setuptools import setup
from setuptools import find_packages
from distutils.extension import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    def cythonize(extensions): return extensions
    sources = ['rocksdb/_rocksdb.cpp']
else:
    sources = ['rocksdb/_rocksdb.pyx']

mod1 = Extension(
    'rocksdb._rocksdb',
    sources,
    include_dirs = ['D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/include', 'D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/options'],
    library_dirs = ['D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/msvc14/Release', 'D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/third-party/Snappy.Library/bin/retail/amd64', 
    'D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/third-party/LZ4.Library/bin/retail/amd64', 'D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/third-party/ZLIB.Library/bin/retail/amd64',
    'D:/lhz/proj/xd/dev/cpp/rocksdb-5.4.6/third-party/Gflags.Library/bin/retail/amd64'],
    extra_compile_args=[
        '-std=c++11',
        '-O3',
        '-Wall',
        # '-Wextra',
        # '-Wconversion',
        '-fno-strict-aliasing'
    ],
    language='c++',
    libraries=[
        'rocksdblib',
        'snappy',
        'lz4',
        'zlib',
        'gflags',
        'Rpcrt4'
    ]
)

setup(
    name="python-rocksdb",
    version='0.6.6',
    description="Python bindings for RocksDB",
    keywords='rocksdb',
    author='Ming Hsuan Tu',
    author_email="Use the github issues",
    url="https://github.com/twmht/python-rocksdb",
    license='BSD License',
    install_requires=['setuptools'],
    package_dir={'rocksdb': 'rocksdb'},
    packages=find_packages('.'),
    ext_modules=cythonize([mod1]),
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    include_package_data=True
)
