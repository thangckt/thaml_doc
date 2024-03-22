from setuptools import setup, find_packages
import re

from thaml._version import __version__


def get_property(prop, folder):
    result = re.search(r'{}\s*=\s*[\'"]([^\'"]*)[\'"]'.format(prop), open(folder + '/__init__.py').read())
    return result.group(1)

# with open("README.md", "r") as f:
#     long_description = f.read()


package_name = 'thaml'

setup(
    name=package_name,         # How you named your package folder (MyLib)
    packages=find_packages(),

    author=get_property('__author__', package_name),
    description=get_property('__description__', package_name),
    long_description=get_property('__long_description__', package_name),
    author_email=get_property('__author_email__', package_name),
    version=__version__,

    ### Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    license_files=('LICENSE.md'),
    # url = 'https://github.com/thangckt/thaml',   # Provide either the link to your github or to your website
    # download_url="https://github.com/thangckt/thaml/tarball/{}".format(__version__),    # I explain this later on
    # keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best

    # package_data={'': ['*/*.mplstyle', 'path/to/resources/*.txt']},
    # include_package_data=True,

    python_requires='>=3.7',

    install_requires=[
        'scipy',
        'numpy',
        'pandas',
        'matplotlib',
        'openai',
        'langchain',
        'chromadb',
        'pypdf',
        'docx2txt',
        'tiktoken',
        'google-generativeai',
        'g4f'
    ],

    classifiers=[
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Development Status :: 3 - Alpha',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3.7',
    ],
)
