from setuptools import setup


setup(
    name = 'hello_stan',
    version='0.0.2',
    description='Say Hi to Stanley',
    py_modules=["hello_stan", "hello_blanche"],
    package_dir={'': 'src'},
)