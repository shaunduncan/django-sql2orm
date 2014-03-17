from setuptools import setup, find_packages

version = '0.0.1'

setup(name="django-sql2orm",
      version=version,
      description=('Reverse engineer SQL queries to ORM calls'),
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
      url='https://github.com/shaunduncan/django-sql2orm',
      license='MIT',
      packages=find_packages(),
)
