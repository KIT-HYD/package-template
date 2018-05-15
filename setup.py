from setuptools import setup, find_packages


with open('requirements.txt') as f:
    REQUIREMENTS = f.read().strip().split('\n')

with open('VERSION') as f:
    VERSION = f.read().strip()

with open('README.md') as f:
    README = f.read()

setup(
    name='package_template',
    version=VERSION,
    license='MIT',
    description='Python package template to publish your own code',
    long_description=README,
    author='Mirko Mälicke',
    author_email='mirko.maelicke@kit.edu',
    install_requires=REQUIREMENTS,
    test_require=['nose'],
    test_suite='nose.collector',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)
