from setuptools import setup

setup(name='gunc',
      description='gunc',
      url='http://github.com/williamsmj/gunc',
      author='Mike Williams',
      author_email='mike@pentangle.net',
      entry_points={
          'console_scripts': [
              'gunc = gunc:main'
          ]}
      )
