from setuptools import setup, find_packages

setup(
    name="monitoring",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = monitoring.snapshot:main",
        ],
    },
    install_requires=[
        'psutil'
    ],
    version="0.1",
    author="Dzmitry Mezhva",
    author_email="Dzmitry_Mezhva@epam.com",
    description="Monitor system/server",
    license="MIT",
)
