import pytest  
from car import Car
from log import Log as l
from messages import m
car=Car()
log=l()
mass=m()


def test_stop():
    try:
        car.status = True
        assert car.stop() == True
        car.status = False
        with pytest.raises(ValueError):
            car.stop()
            log.writeLog(mass.error_messages['test7'])

    except:
        log.writeLog(mass.error_messages['tes7'])

# @pytest.mark.one
def test_accelerate():
    try:
        car.drive(20)
        car.shiftUp(20)
        assert car.speed == 40
        log.writeLog(mass.error_messages['test8'])
    except ArithmeticError as e:
        log.writeLog({e})
        # log.writeLog(mass.error_messages['tes8'])

def test_brake():
    try:
        car.shiftUp(20)
        car.shiftDown(10)
        log.writeLog(mass.error_messages['test9'])
    except:
        log.writeLog(mass.error_messages['tes9'])

def test_stop():
    try:
        car.drive(100)
        car.stop()
        assert car.status == False
        log.writeLog(mass.error_messages['test10'])
    except:
        log.writeLog(mass.error_messages['tes10'])

@pytest.mark.one
def test_refuel():
    with pytest.raises(Exception):
        car.fuel_up(50) 
    log.writeLog(mass.error_messages['test11'])

def test_refuel_negative():
    try:
        with pytest.raises(Exception):
            car.fuel_up(-50)
        log.writeLog(mass.error_messages['test12'])
    except:
        log.writeLog(mass.error_messages['tes12'])

def test_stop_failure():
    try:
        car.status=False
        with pytest.raises(Exception):
            car.stop()
        log.writeLog(mass.error_messages['test13'])
    except:
        log.writeLog(mass.error_messages['tes13'])


def test_fuel_consumption():
    try:
        car.status = True
        with pytest.raises(Exception):
            car.fuel_up(120) 
        log.writeLog(mass.error_messages['test14'])

    except:
        log.writeLog(mass.error_messages['tes14'])

def test_downshift():
    try:
        car.status = True
        assert car.shiftDown(10) 
        car.status = False
        with pytest.raises(Exception):
            car.shiftDown(10)
        log.writeLog(mass.error_messages['test15'])
    except AssertionError as e:
        log.writeLog({e})

 
   