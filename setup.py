from setuptools import setup

setup(
    name="gusevtech.cvgpt",
    packages=["gusevtech.cvgpt"],
    version="0.0.1",
    install_requires=[
        "sqlite3",
        "numpy",
        "toml",
    ],
    entry_points={
        "console_scripts": [
            "cvgpt = gusevtech.cvgpt.main:main",
        ]
    },
)
