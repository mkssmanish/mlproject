from setuptools import find_packages, setup


pa






setup(
    name='mlproject',
    version='0.0.1',
    author='Manish Kumar Singh',
    author_email='mkssmanish@gmail.com',
    packages=find_packages(),
    # install_require = ['pandas','numpy','seaborn']
    install_requires=get_requirements('requirements.txt')
)