from setuptools import setup

exec (open('react_live_clock_port/version.py').read())

setup(
    name='react_live_clock_port',
    version=__version__,
    author='drawinism',
    packages=['react_live_clock_port'],
    include_package_data=True,
    license='MIT',
    description='Python-port of the react-live-clock to integrate with plotly dash (forked from https://github.com/pvoznyuk/react-live-clock) ',
    install_requires=[]
)
