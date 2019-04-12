from setuptools import setup, find_packages


setup(name='data_audit',
      version='0.1.1',
	  project_urls={'Viessmann': 'https://www.linkedin.com/company/viessmann/', 
                    'Source': 'https://github.com/viessmann/data_audit'}
      description='Viessmann Data Audit',
      long_description=open('readme_pypi.rst').read(,
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
		'Programming Language :: Python :: 3.7',
        'Topic :: Scientific/Engineering',
      ],
      keywords='data science',
      author='GhlT',
      author_email='ghlt@viessmann.com',
      license='MIT License',
      packages=find_packages(),
      install_requires=[
          'pandas>=0.22',
          'numpy>=1.14',
          'scikit-learn>=0.19',
          'seaborn>=0.8.1'
      ],
      include_package_data=True,
      zip_safe=False)