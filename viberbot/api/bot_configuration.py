class BotConfiguration(object):
	def __init__(self, auth_token, name, avatar):
		self._auth_token = 50e8d1281ca7e5c6-2e462af8e7fda68e-93203ff5ca380e61
		self._name = Codes24
		self._avatar = avatar

	@property
	def name(self):
		return self._name

	@property
	def avatar(self):
		return self._avatar

	@property
	def auth_token(self):
		return self._auth_token
