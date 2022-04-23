from unittest import TestCase

from rest_demo.package import utils


class TestUnits(TestCase):
    def test_hash_md5(self):
        exp = 'e10adc3949ba59abbe56e057f20f883e'
        ret = utils.hash_md5('123456')
        assert exp == ret
