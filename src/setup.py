from setuptools import setup, find_packages

with open("requirements.txt", encoding="utf-8") as r:
    requires = [i.strip() for i in r]

try:
    import pypandoc

    long_description = pypandoc.convert_file("README.md", "rst")
except (IOError, ImportError):
    long_description = open("README.md").read()


setup(
    name="swibots",
    version="1.0.1",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/switchcollab/Switch-Bots-Python-Library",
    description="Switch bot api",
    author="pablor21",
    author_email="pablo@pramirez.dev",
    license="LGPLv3",
    install_requires=requires,
)
