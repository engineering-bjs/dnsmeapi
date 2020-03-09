import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dnsmeapi",
    version="0.0.1",
    author="BJS Engineering Team",
    author_email="anish@bjshomedelivery.com",
    description="make simple dnsmadeeasy api calls",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/engineering-bjs/dnsmeapi",
    packages=setuptools.find_packages(),
    install_requires=["requests>=2.23.0"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
