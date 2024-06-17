#  Used for packaging Python projects
import setuptools
# opens the README.md file, reads its contents and stores it in the variable long_description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# Defining the Package Version
__version__ = "0.0.0"

# Defining Package Metadata
REPO_NAME = "Chicken-Disease-Classification--Project"
AUTHOR_USER_NAME = "moatazsaad"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "moataz.osama@hotmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)