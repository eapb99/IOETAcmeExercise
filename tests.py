from Employee import Employee
from utils import loadfile, create_schedule, relations, coincidence, intersection
import unittest

data = loadfile("files/data.txt")
schedule1 = create_schedule("MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00")
schedule2 = create_schedule("MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")


class TestLoadData(unittest.TestCase):

    def test_type_expected(self):
        self.assertEqual(type(data), list)

    def test_len_expected(self):
        self.assertEqual(len(data), 2)

    def test_content_list_expected(self):
        e1 = Employee("RENE", schedule1)
        e2 = Employee("ASTRID", schedule2)
        self.assertEqual(data, [e1, e2])


class TestCreateRelations(unittest.TestCase):

    def setUp(self):
        self.result = relations(data)

    def test_type_expected(self):
        self.assertEqual(type(self.result), list)

    def test_len_expected(self):
        self.assertEqual(len(self.result), 1)

    def test_type_items_expected(self):
        self.assertEqual(type(self.result[0]), tuple)

    def test_len_items_expected(self):
        self.assertEqual(len(self.result[0]), 2)

    def test_content_list_expected(self):
        e1 = Employee("RENE", schedule1)
        e2 = Employee("ASTRID", schedule2)
        self.assertEqual(self.result, [(e1, e2)])


class TestIterateList(unittest.TestCase):

    def setUp(self):
        self.relations = relations(loadfile("files/schedule.txt"))
        self.lista = []
        self.results = coincidence(self.relations, self.lista, 0)

    def test_type_expected(self):
        self.assertEqual(type(self.results), list)

    def test_len_expected(self):
        self.assertEqual(len(self.results), 3)

    def test_first_value_expected(self):
        self.assertEqual(self.results, ["PEPE-ANDREA:2", "PEPE-ANDRES:2", "ANDREA-ANDRES:3"])


class TestIntersectionSchedules(unittest.TestCase):
    def test_count_intersection(self):
        counter = intersection(schedule1, schedule2)
        self.assertEqual(counter, 3)


if __name__ == '__main__':
    unittest.main()
