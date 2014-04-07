from setuptools import setup, find_packages

version = '0.0.1'

setup(name="django-tools",
      version=version,
      description='Various tools for dealing with SQL in django apps',
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Framework :: Django',
                   'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='django sql orm',
      author='Shaun Duncan',
      author_email='shaun.duncan@gmail.com',
      url='https://github.com/shaunduncan/django-sqltools',
      license='MIT',
      packages=find_packages(),
)
