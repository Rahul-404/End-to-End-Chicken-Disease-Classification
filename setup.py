import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "End-to-End-Chicken-Disease-Classification"
AUTHER_USER_NAME = "Rahul-404"
SRC_REPO = "cnnClassifier"
AUTHER_EMAIL = "rahulshelke981@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    author=AUTHER_USER_NAME,
    author_email=AUTHER_USER_NAME,
    version=__version__,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bugs": f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)