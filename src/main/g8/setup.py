from setuptools import find_packages, setup

setup(
    name='$packge_name;format="lower,snake"$',
    version='$version$',
    author='$author$',
    author_email='$author_email$',
    packages=find_packages(),
    description='$description$',
    test_suite='$name$.tests.get_suite',
    include_package_data=True,
    zip_safe=False,
    entry_points = {
        'console_scripts': [
            'pamhdb = $name$.__main__:main'
        ]
    },
    install_requires=[]
)
