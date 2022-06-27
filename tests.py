from utils import *
import unittest


class TestLoadData(unittest.TestCase):
    def setUp(self):
        self.result = loadfile("files/data.txt")
        self.schedule1 = createSchedule("MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00")
        self.schedule2 = createSchedule("MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")

    def test_type_expected(self):
        self.assertEqual(type(self.result), list)

    def test_len_expected(self):
        self.assertEqual(len(self.result), 2)

    def test_content_list_expected(self):
        e1 = Employee("RENE", self.schedule1)
        e2 = Employee("ASTRID", self.schedule2)
        self.assertEqual(self.result, [e1, e2])


class TestCreateRelations(unittest.TestCase):

    def setUp(self):
        self.data = loadfile("files/data.txt")
        self.result = relations(self.data)
        self.schedule1 = createSchedule("MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00")
        self.schedule2 = createSchedule("MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")

    def test_type_expected(self):
        self.assertEqual(type(self.result), list)

    def test_len_expected(self):
        self.assertEqual(len(self.result), 1)

    def test_type_items_expected(self):
        self.assertEqual(type(self.result[0]), tuple)

    def test_len_items_expected(self):
        self.assertEqual(len(self.result[0]), 2)

    def test_content_list_expected(self):
        e1 = Employee("RENE", self.schedule1)
        e2 = Employee("ASTRID", self.schedule2)
        self.assertEqual(self.result, [(e1, e2)])


class TestIterateList(unittest.TestCase):
    def setUp(self):
        self.result = relations(loadfile("files/schedule.txt"))
        self.lista = []

    def test_type_expected(self):
        result = coincidence(self.result, self.lista, 0)
        self.assertEqual(type(result), list)

    def test_len_expected(self):
        result = coincidence(self.result, self.lista, 0)
        self.assertEqual(len(result), 3)

    def test_first_value_expected(self):
        result = coincidence(self.result, self.lista, 0)
        self.assertEqual(result, ["PEPE-ANDREA:2", "PEPE-ANDRES:2", "ANDREA-ANDRES:3"])


class TestIntersectionSchedules(unittest.TestCase):
    def setUp(self):
        self.result = loadfile("files/data.txt")
        self.schedule1 = createSchedule("MO10:15-12:00,TU10:00-12:00,TH13:00-13:15,SA14:00-18:00,SU20:00-21:00")
        self.schedule2 = createSchedule("MO10:00-12:00,TH12:00-14:00,SU20:00-21:00")

    def test_count_intersection(self):
        counter = intersection(self.schedule1, self.schedule2)
        self.assertEqual(counter, 3)


if __name__ == '__main__':
    unittest.main()
