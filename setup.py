import os

from setuptools import find_packages, setup

HERE = os.path.dirname(os.path.abspath(__file__))


def _get_version():
    """ Get version by parsing _version programmatically """
    version_ns = {}
    with open(
        os.path.join(HERE, "dash_holoniq_components", "_version.py")
    ) as f:
        exec(f.read(), {}, version_ns)
    version = version_ns["__version__"]
    return version

def _get_long_description():
    with open(os.path.join(HERE, "landing-page.md")) as f:
        return f.read()

setup(
    name="dash-holoniq-components",
    version=_get_version(),
    description="Custom components for use in Plotly Dash",
    long_description=_get_long_description(),
    long_description_content_type="text/markdown",
    url='https://github.com/stevej2608/dash-holoniq-components',
    author='Steve Jones',
    author_email='jonesst2608@gmail.com',
    license="Apache Software License",
    packages=find_packages(),
    install_requires=["dash>=0.41.0", "dash-bootstrap-components>=0.7.1"],
    include_package_data=True,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Financial and Insurance Industry",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Manufacturing",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Database :: Front-Ends",
        "Topic :: Office/Business :: Financial :: Spreadsheet",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Widget Sets",
    ]
)
