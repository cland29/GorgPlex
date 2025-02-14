from setuptools import find_packages, setup

with open("app/README.md", "r") as f:
    long_description = f.read()

setup(
    name="gorgplex",
    version="0.0.10",
    description="The gorgplex at your fingertips",
    package_dir={"":"app"},
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cland29/GorgPlex",
    author="Carl Lee Landskron",
    author_email="Carl.lee.landskron@gmail.com",
    install_requires=["matplotlib >= 3.10.0",
                      "numpy >=  1.26.4"],
    python_requires=">=3.12",
)