from setuptools import setup

setup(name='noaa-weather',
      version='0.1',
      description='Fetch weather data from the NOAA API',
      url='http://github.com/viking/noaa-weather',
      author='Jeremy Stephens',
      author_email='jeremy.f.stephens@vumc.org',
      license='MIT',
      scripts=['bin/noaa-weather'],
      install_requires=['requests', 'geojson'],
      zip_safe=False)
