from setuptools import setup
setup(
    name='pyramid_analytics_api',
    author='Shawn Sarwar, Lutz Paelike',
    author_email="shawn.sarwar@pyramidanalytics.com",
    description='''Pyramid Analytics REST APIs in Python (2020.26.0)''',
    version='1.1.4',
    packages=['pyramid_api'],
    setup_requires=['pytest','pytest-runner', 'requests', 'pydantic'],
    url='https://github.com/pyramid-alliances/pyramid_analytics_python',
    keywords=['REST', 'pyramidanalytics', 'pyramid', 'analytics'],
    classifiers=[]
)
