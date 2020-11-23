from setuptools import setup, find_packages
find__init__ = find_packages()

options = dict(name="chicovidtracker",
               author="Brandon Hoeft",
               packages=find__init__)

if __name__ == '__main__':
    setup(**options)