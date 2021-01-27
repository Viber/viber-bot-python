from setuptools import setup
exec(open('viberbot/version.py').read())
setup(
    name='viberbot',
    version=__version__,
    packages=['viberbot', 'viberbot.api', 'viberbot.api.viber_requests',
              'viberbot.api.messages', 'viberbot.api.messages.data_types'],
    install_requires=['future', 'requests'],
    tests_require=['pytest'],
    url='https://github.com/Viber/viber-bot-python',
)
