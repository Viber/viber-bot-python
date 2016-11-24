from setuptools import setup

setup(
	name='viber',
	version='0.1.3',
	packages=['viber', 'viber.api', 'viber.api.viber_requests',
			  'viber.api.messages', 'viber.api.messages.data_types'],
	install_requires=['future', 'requests']
)