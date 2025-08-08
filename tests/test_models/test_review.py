#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ """
        new = self.value()
        self.assertTrue(new.place_id is None
                        or isinstance(new.place_id, str))

    def test_user_id(self):
        """ """
        new = self.value()
        self.assertTrue(new.user_id is None
                        or isinstance(new.user_id, str))

    def test_text(self):
        """ """
        new = self.value()
        self.assertTrue(new.text is None
                        or isinstance(new.text, str))
