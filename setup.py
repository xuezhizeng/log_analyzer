from setuptools import setup, find_packages, Extension

setup(name='log_analyzer',
      version='1.2.1',
      description="waibao",
      long_description="""waibao""",
      keywords='python log commandline',
      author='cm',
      author_email='jason0916phoenix@gmail.com',
      url='https://github.com/JASON0916/',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'prompt-toolkit',
          'Pygments',
          'six',
          'wheel',
          'wcwidth',
          ],
      classifiers=[
          'Programming Language :: Python :: 2.7',
      ],
      entry_points={
          'console_scripts': [
              'log_analyzer = analyzer.client:main',
          ]
      },
)