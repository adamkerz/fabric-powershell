from setuptools import setup,find_packages


with open('fabric_powershell/version.py') as fin: exec(fin)

setup(
    name='fabric-powershell',
    version=__version__,

    packages=find_packages(exclude=['tests*']),
    
    # dependencies
    install_requires=['fabric'],
    
    # PyPI MetaData
    author='Adam Kerz',
    author_email='github@kerz.id.au',
    description='Fabric functions to run Powershell scripts and manipulate remote Windows servers.',
    license='BSD 3-Clause',
    keywords='fabric powershell',
    url='http://github.com/adamkerz/fabric-powershell',
    classifiers=(
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ),

    zip_safe=False
)
