from setuptools import setup, find_packages

setup(
    name = 'database-browser',
    description = 'a simple command line tool to explore db tables',
    packages = find_packages(),
    author='Yun-Chung Liu',
    install_requires = ['click==8.1.3', 'sqlite3==3.38.5'],
    extras_require = {"dev":"pytest >=7.0"},
    python_requires=">=3.9",
    version = '0.0.1',
    url = 'https://github.com/nogibjj/CLItool_YCLiu'
    )