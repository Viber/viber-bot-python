from setuptools import setup

setup(
	name='viberbot',
	version='1.0.0',
	packages=['viberbot', 'viberbot.api', 'viberbot.api.viber_requests',
			  'viberbot.api.messages', 'viberbot.api.messages.data_types'],
	install_requires=['future', 'requests'],
	url='https://github.com/Viber/viber-bot-python',
)