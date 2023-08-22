from setuptools import setup, find_packages

setup(
    name="mypackage",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "requests",  # Example dependency
    ],
    entry_points={
        'console_scripts': [
            'mycli=mypackage.cli:main',  # CLI entry point
        ],
    },
    # ... other metadata (author, license, classifiers, etc.)
)
