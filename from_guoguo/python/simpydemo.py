# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import simpy

def car(env: simpy.Environment)->None:
    """
    demo car
    """
    while 1:
        print("start parking at %d" % env.now)
        parking_duration = 5
        yield  env.timeout(parking_duration)

        print("start driving at %d" % env.now)
        trip_duration = 2
        yield env.timeout(trip_duration)

if __name__ == '__main__':
    env = simpy.Environment()
    env.process(car(env))
    env.run(until=15)
