from setuptools import setup, find_packages

setup(
    name='mertics',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[],
    author='BobryTeam',
    author_email='sinntexxx@gmail.com',
    description='Metrics data structure',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/BobryTeam/metrics',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
