from setuptools import setup

setup(
    name='guzzle_lite',
    version='0.1',
    description='Inspired by guzzle_sphinx_theme.',
#   long_description=open('README.rst').read(),
    author='YC',
#   author_email='mtdowling@gmail.com',
    url='https://github.com/yinch3ng/guzzle_lite',
    packages=['guzzle_lite'],
    include_package_data=True,
    install_requires=['Sphinx>1.3'],
    classifiers=(
        'Development Status :: 1 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
    ),
)
