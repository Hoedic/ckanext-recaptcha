from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
	name='ckanext-recaptcha',
	version=version,
	description="Re-enable Recaptcha widget on registration page (broken since CKAN 2.0)",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='',
	author_email='',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.recaptcha'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points=\
	"""
        [ckan.plugins]
	# Add plugins here, eg
	recaptcha=ckanext.recaptcha.plugin:RecaptchaPlugin
	""",
)
