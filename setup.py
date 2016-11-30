from setuptools import setup

setup(
	name='viber',
	packages=['viber'],
	version='0.1.3',
	packages=['viber', 'viber.api', 'viber.api.viber_requests',
			  'viber.api.messages', 'viber.api.messages.data_types'],
	install_requires=['future', 'requests'],
	url='https://github.com/Viber/viber-bot-python',
	download_url='https://github.com/Viber/viber-bot-python/tarball/0.1.3'
)