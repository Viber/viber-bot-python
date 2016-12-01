from future.utils import python_2_unicode_compatible


class Contact(object):
	def __init__(self, name=None, phone_number=None):
		self._name = name
		self._phone_number = phone_number

	def from_dict(self, contact):
		if 'name' in contact:
			self._name = contact['name']
		if 'phone_number' in contact:
			self._phone_number = contact['phone_number']
		return self

	def to_dict(self):
		return {
			'name': self._name,
			'phone_number': self._phone_number
		}

	def get_name(self):
		return self._name

	def get_phone_number(self):
		return self._phone_number

	def __eq__(self, other):
		return self._name == other.get_name() and self._phone_number == other.get_phone_number()

	@python_2_unicode_compatible
	def __str__(self):
		return u"Contact[name={0}, phone_number={1}]".format(self._name, self._phone_number)
