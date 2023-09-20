import unittest
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestDBStorage(unittest.TestCase):
    def setUp(self):
        self.storage = storage
        self.storage.reload()

    def tearDown(self):
        self.storage.delete(self.obj)
        self.storage.save()

    def test_all(self):
        self.obj = BaseModel()
        self.storage.new(self.obj)
        self.storage.save()
        objs = self.storage.all()
        self.assertIn(self.obj, objs.values())

    def test_new(self):
        self.obj = User()
        self.storage.new(self.obj)
        self.storage.save()
        objs = self.storage.all(User)
        self.assertIn(self.obj, objs.values())

    def test_save(self):
        self.obj = State()
        self.obj.name = "California"
        self.storage.new(self.obj)
        self.storage.save()
        objs = self.storage.all(State)
        self.assertIn(self.obj, objs.values())

    def test_delete(self):
        self.obj = City()
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.delete(self.obj)
        objs = self.storage.all(City)
        self.assertNotIn(self.obj, objs.values())

    def test_reload(self):
        self.obj = Amenity()
        self.storage.new(self.obj)
        self.storage.save()
        self.storage.reload()
        objs = self.storage.all(Amenity)
        self.assertNotIn(self.obj, objs.values())
