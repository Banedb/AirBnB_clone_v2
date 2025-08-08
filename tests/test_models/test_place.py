#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ """
        new = self.value()
        self.assertTrue(new.city_id is None
                        or isinstance(new.city_id, str))

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(new.user_id is None
                        or isinstance(new.user_id, str))

    def test_name(self):
        """ """
        new = self.value()
        self.assertTrue(new.name is None
                        or isinstance(new.name, str))

    def test_description(self):
        """ """
        new = self.value()
        self.assertTrue(new.description is None
                        or isinstance(new.description, str))

    def test_number_rooms(self):
        """ """
        new = self.value()
        self.assertTrue(new.number_rooms is None
                        or isinstance(new.number_rooms, int))

    def test_number_bathrooms(self):
        """ """
        new = self.value()
        self.assertTrue(new.number_bathrooms is None or
                        isinstance(new.number_bathrooms, int))

    def test_max_guest(self):
        """ """
        new = self.value()
        self.assertTrue(new.max_guest is None
                        or isinstance(new.max_guest, int))

    def test_price_by_night(self):
        """ """
        new = self.value()
        self.assertTrue(new.price_by_night is None
                        or isinstance(new.price_by_night, int))

    def test_latitude(self):
        """ """
        new = self.value()
        self.assertTrue(new.latitude is None
                        or isinstance(new.latitude, float))

    def test_longitude(self):
        """ """
        new = self.value()
        self.assertTrue(new.longitude is None
                        or isinstance(new.longitude, float))

    def test_amenity_ids(self):
        """ """
        new = self.value()
        self.assertTrue(new.amenity_ids is None
                        or isinstance(new.amenity_ids, list))
