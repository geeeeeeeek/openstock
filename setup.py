from setuptools import setup, find_packages

setup(
    name="openstock",
    version="0.0.7",
    author="Tim",
    author_email="kefu308@gmail.com",
    description="一个股票行情工具包，可以用来获取股票历史k线数据",
    long_description=open('README.md', "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/geeeeeeeek/openstock",
    packages=find_packages(),
    install_requires=[
        "akshare>=1.17.36"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)