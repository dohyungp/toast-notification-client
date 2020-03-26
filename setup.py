import setuptools

install_requires = [
    'requests == 2.22.0',
    'jsonschema == 3.1.1'
]


with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='Toast-Notification-Client',  # Replace with your own username
    version='0.0.1',
    author='Dohyung Park',
    author_email='dohyung.prk@gmail.com',
    description='Toast cloud Notification RESTful API Client for Python User.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/dohyungp/toast-notification-client',
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
