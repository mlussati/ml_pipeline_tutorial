from setuptools import setup

setup(
    name="ml-pipeline",
    version="1.0.0",
    author="Manilson Lussati",
    author_email="mlussati@hotmail.com",
    description="A machine learning pipeline.",
    packages=[
        "ml_pipeline",
        "ml_pipeline.datasets",
        "ml_pipeline.models",
        "ml_pipeline.mixins",
    ],
    install_requires=[
        "joblib==1.2.0",
        "matplotlib==3.6.3",
        "numpy==1.24.1",
        "omegaconf==2.3.0",
        "pandas==1.5.3",
        "scikit-learn==1.2.1",
        "seaborn==0.12.2",
    ],
)