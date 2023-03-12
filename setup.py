from setuptools import setup, find_packages


setup(
    name="Courier",
    version="1.0.2-alpha.0",
    license="MIT",
    author="Joshua Rose",
    author_email="courierpackagemanager@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    url="https://github.com/Courier-Package-Manager/Courier",
    keywords="package manager, CLI",
    install_requires=[
        "bs4",
        "requests",
        "colorama",
        "packaging",
        "Sphinx",
        "flake8",
        "black>=23.1.0",
        "coverage",
        "codecov",
        "mypy>=0.991",
        "pytest",
        "pytest-cov",
        "pytest-sugar",
        "types-PyYAML",
        "types-requests",
        "types-beautifulsoup4",
        "types-setuptools",
        "types-colorama",
    ],
)
