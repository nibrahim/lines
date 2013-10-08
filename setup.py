from setuptools import setup

setup(
    name="lines",
    version="0.1.0-a",
    description='Treat lines of a file as elements of a set',
    license='GPL',
    author='Noufal Ibrahim',
    author_email='noufal@nibrahim.net.in' ,
    url='https://github.com/nibrahim/lines',
    platforms=['linux', 'osx', 'win32'],
    install_requires = ['pytest', 'pylev'],
    py_modules=['lines'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: MacOS :: MacOS X',
        'Topic :: Utilities',
        'Programming Language :: Python',
    ],
    entry_points = {
        'console_scripts' : [ 'lines = lines:entry' ]
        }
)
