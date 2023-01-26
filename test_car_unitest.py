# unitest
from car import Car
import unittest
from log import Log as l
from messages import m
class TestCar(unittest.TestCase):
    log=l()
    mass=m()
    def setUp(self):
          self.car = Car()
    def test_add_fuel(self):
        '''
        name:chani
        date:22/01
        The function test_add_fuel
        :return:
        '''
        try:
            self.car.fuel_up(10)
            self.assertEqual(self.car.liter, 60)
            self.log.writeLog(self.mass.error_messages['test'])
        except AssertionError as e:
            self.log.writeLog({e})

    def test_fuel_consumption(self):
        try:
            self.car.status = True
            self.car.km = 200
            self.car.liter -= self.car.liter_per_km * self.car.km / 100
            self.assertEqual(self.car.liter, 10)
            self.log.writeLog(self.mass.error_messages['test1'])
        except:
             self.log.writeLog(self.mass.error_messages['tes1'])

    def test_km_update(self):
        try:
            self.car.km += 200
            self.assertEqual(self.car.km, 400)
            self.log.writeLog(self.mass.error_messages['test2'])
        except:
             self.log.writeLog(self.mass.error_messages['tes2'])

    def test_fill_up_fuel_failure(self):
        try:
            self.car.money = 100
            with self.assertRaises(ValueError) as exacinfo :
                self.car.fuel_up(70)
            # self.log.writeLog(self.mass.error_messages['test3'])
            self.log.writeLog({exacinfo.exception})
        except AssertionError as e:
            self.log.writeLog({e})

    def test_fill_up_fuel_success(self):
        try:
            self.car.money = 500
            self.assertTrue(self.car.fuel_up(49))
            self.log.writeLog(self.mass.error_messages['test4'])
        except:
             self.log.writeLog(self.mass.error_messages['tes4'])

    def test_stop_success(self):
        try:
            self.car.status = True  
            self.assertTrue(self.car.stop())
            self.log.writeLog(self.mass.error_messages['test5'])
        except:
            self.log.writeLog(self.mass.error_messages['tes5'])

    def test_log_stop_success(self):
        try:
            self.car.status = True
            self.car.stop()
            self.log.writeLog(self.mass.error_messages['test6'])
        except:
            self.log.writeLog(self.mass.error_messages['tes6'])

if __name__ == '__main__':
    unittest.main
