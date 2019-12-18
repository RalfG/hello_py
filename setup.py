from setuptools import setup
from Cython.Build import cythonize

setup(
	name='hello_py',
	version='0.1.0',
	license='apache-2.0',
	author='Ralf Gabriels',
	author_email='ralfg@hotmail.be',
	packages=['hello_py'],
	include_package_data=False,
	entry_points={'console_scripts': ['hello_py=hello_py.__main__:main']},
	install_requires=[],
	python_requires='>=3.6,<4',
	ext_modules = cythonize("hello_py/hello_c.pyx")
)
