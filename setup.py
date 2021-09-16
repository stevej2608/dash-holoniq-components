import json
import os
from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))

with open('package.json') as f:
    package = json.load(f)

package_name = package["name"].replace(" ", "_").replace("-", "_")

def _get_long_description():
    with open(os.path.join(HERE, "landing-page.md")) as f:
        return f.read()

setup(
    name=package_name,
    version=package["version"],
    author=package['author'],
    packages=find_packages(),
    install_requires=["dash>=2.0.0", "dash-bootstrap-components>=0.13.0"],
    include_package_data=True,
    license=package['license'],
    description=package.get('description', package_name),
    long_description=_get_long_description(),
    long_description_content_type="text/markdown",
    classifiers = [
        'Framework :: Dash',
    ],    
)
