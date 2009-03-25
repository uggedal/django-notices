from setuptools import setup, find_packages
 
setup(
    name='django-notices',
    version='0.1.0',
    description='Efficient and lightweight notices for Django.',
    author='Eivind Uggedal',
    author_email='eu@redflavor.com',
    url='http://redflavor.com/',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
