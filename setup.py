from setuptools import setup


setup(
    name='pre_commit_hook_prototype',
    version='0.0.0',
    # This installs the dependencies
    install_requires=['yapf==0.16.1', 'docformatter==0.8'],
    # This places our yapf.conf in the right place
    data_files=[('/etc/prototype', ['example_yapf.conf'])]
)
