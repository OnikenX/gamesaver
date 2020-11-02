from setuptools import setup
from Cython.Build import cythonize


setup(
    name='ConfigManagerTest',
    ext_modules=cythonize("ConfigManager.py", language_level=3),
    zip_safe=False,
)