from future.utils import python_2_unicode_compatible


class UserProfile(object):
	def __init__(self, name, avatar, user_id, country=None, language=None):
		self._name = name
		self._avatar = avatar
		self._id = user_id
		self._country = country
		self._language = language

	def get_name(self):
		return self._name

	def get_avatar(self):
		return self._avatar

	def get_id(self):
		return self._id

	def get_country(self):
		return self._country

	def get_language(self):
		return self._language

	@python_2_unicode_compatible
	def __str__(self):
		return u"UserProfile[name={0}, avatar={1}, id={2}, country={3}, language={4}"\
			.format(self._name,
					self._avatar,
					self._id,
					self._country,
					self._language)
