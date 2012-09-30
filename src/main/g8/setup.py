# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    name='$package_name;format="lower,snake"$',
    version='$version$',
    author='$author$',
    author_email='$author_email$',
    packages=find_packages(),
    url='',
    license='LICENSE.txt',
    description='$description$',
    test_suite='$package_name$.tests.get_suite',
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            '$package_name;format="lower,snake"$ = $package_name;format="lower,snake"$.__main__:main'
        ]
    },
    install_requires=[]
)
