from setuptools import setup

setup(
	name='viberbot',
	version='0.1.3.3',
	packages=['viberbot', 'viberbot.api', 'viberbot.api.viber_requests',
			  'viberbot.api.messages', 'viberbot.api.messages.data_types'],
	install_requires=['future', 'requests'],
	url='https://github.com/Viber/viber-bot-python',
	download_url='https://github.com/Viber/viber-bot-python/tarball/0.1.3.3'
)