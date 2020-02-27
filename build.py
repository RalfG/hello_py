from setuptools import Extension
from Cython.Build import cythonize


def build(setup_kwargs):
    setup_kwargs.update({
        'ext_modules': cythonize([
            Extension(
                name='hello_c',
                sources=['hello_py/hello_c.pyx'])
        ], language_level=3),
        'zip_safe': False
    })
