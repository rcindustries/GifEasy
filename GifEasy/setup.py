from setuptools import setup, find_packages

setup(
    name="GifEasy",
    version="0.1.0",
    author="Ton Nom",
    description="Un module facile pour afficher et manipuler des GIFs avec Tkinter",
    packages=find_packages(),
    install_requires=["Pillow"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)