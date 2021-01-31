class BotConfiguration(object):
	def __init__(self, auth_token, name, avatar, min_api_version=1):
		self._auth_token = auth_token
		self._name = name
		self._avatar = avatar
		self._min_api_version=min_api_version

	@property
	def name(self):
		return self._name

	@property
	def avatar(self):
		return self._avatar

	@property
	def auth_token(self):
		return self._auth_token

	@property
	def min_api_version(self):
		return self._min_api_version
