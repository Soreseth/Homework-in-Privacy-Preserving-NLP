from setuptools import setup

setup(
    name='pii_bert',
    version='0.1.0',    
    description='DistilBERT model for NER of PII labels',
    author='Abinash Selvarajah, Joel Baltes',
    author_email='abinash.selvarajah@ruhr-uni-bochum.de, joel.baltes@ruhr-uni-bochum.de',
    license='MIT',
    packages=['pii_bert'],
    include_package_data=True,
    install_requires=['transformers', 'torch'],
        entry_points={
        'console_scripts': [
            'pii-bert=pii_bert.model:main',
        ],
    },
)