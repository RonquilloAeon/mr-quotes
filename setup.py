from setuptools import setup, find_packages


setup(
    name="mrquotes",
    version="0.1.0",
    install_requires=[
        "fastapi==0.53.2",
        "migri==0.1.4",
        "pydantic==1.4",
        "uvicorn==0.11.7",
    ],
    packages=find_packages(exclude=['test*']),
    include_package_data=True,
    python_requires='>=3.8',
)
