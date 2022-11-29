from typing import TypedDict
import random as rnd


class User:
    _id: int
    _last_name: str
    _first_name: str
    _phone: str
    _about: str

    def __init__(self, last_name, first_name, phone, about):
        self._id = id.__class__
        self._last_name = last_name
        self._first_name = first_name
        self._phone = phone
        self._about = about

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        self._last_name = value

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        self._first_name = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def about(self):
        return self._about

    @about.setter
    def about(self, value):
        self._about = value



