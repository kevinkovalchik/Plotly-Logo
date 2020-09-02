from setuptools import setup, find_packages

setup(
    name='plotly-logo',
    version='0.0.2',
    packages=find_packages(),
    url='https://github.com/kevinkovalchik/Plotly-Logo',
    license='MIT License',
    author='Kevin Kovalchik',
    author_email='',
    description='A Python library for making amino acid sequence logos using the Plotly framework.',
    python_requires='>=3.7',
    install_requires=['numpy', 'plotly>=1.12.0', 'pandas'],
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
