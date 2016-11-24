from setuptools import setup

setup(name='satapi',
      version='0.2',
      description='Version 0.2',
      url='http://github.com/soukron/satapi2',
      author='Sergio G.',
      author_email='soukron@gmbros.net',
      license='MIT',
      packages=['satapi'],
      install_requires=[
          'restkit',
          'config'
      ],
      zip_safe=False)
