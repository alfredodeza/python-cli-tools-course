from setuptools import setup, find_packages

setup(
    name="demo-jformat",
    version="0.0.1",
    description="Reformats files to stdout",
    install_requires = ["click", "colorama"],
    entry_points="""
    [console_scripts]
    jformat=jformat.main:main
    """,
    author="Alfredo Deza",
    author_email="alfredo@deza.pe",
    packages=find_packages(),
)
