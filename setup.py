from setuptools import setup
from xmgrace_parser import __version__

setup(
    name='xmgrace_parser',
    version=__version__,
    py_modules=['xmgrace_parser'],
    description='Modifying xmgrace agr files interactively in ipython',
    author='Michael Goerz',
    author_email='mail@michaelgoerz.net',
    url='https://github.com/goerz/xmgrace_parser',
    license='GPL',
    entry_points={
    'console_scripts': ['xmgrace_parser = xmgrace_parser:main', ],},
)
