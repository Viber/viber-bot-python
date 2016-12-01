class BotConfiguration(object):
	def __init__(self, auth_token, name, avatar):
		self._auth_token = auth_token
		self._name = name
		self._avatar = avatar

	def get_name(self):
		return self._name

	def get_avatar(self):
		return self._avatar

	def get_auth_token(self):
		return self._auth_token
