"""
demo code for plane in and out
there is three pushing rules:
1. only 10 airplane on road
2. wait queue should less than ten
3. pushing airplane should separated by two airplane
"""
from simpy import Resource , Environment, Store
import numpy as np


def aircraftpushing(env,airplane,roads,nodes,wait_queue):
    """
    determine if airplane can push or not
    """
    # road = roads.request()
    yield road.put(airplane)
    node = nodes.request()
    yield node
    yield wait_queue.request()
    print('airplane {name} fulfill rule at {time}'.format(name=airplane,time=env.now))
    yield env.timeout(2*60)
    nodes.release(node)

def paircrafparking(env,airplane,roads,nodes):
    yield roads.put(airplane)

def road_gen(env,road):
    yield env.timeout(np.random.randint(20,100))
    r = road.get()
    yield r


if __name__ == '__main__':
    pushing_list = [i for i in range(20)]

    env = Environment()
    # rule 1
    road = Store(env,capacity=3)
    # rule 2
    wait_queue = Resource(env,capacity=20)
    # rule 3
    nodes = Resource(env,capacity=4)

    # env.process(test(env,road))

    for airplane in pushing_list:
        env.process(aircraftpushing(env,airplane,road,nodes,wait_queue))
    for i in range(100):
        env.process(road_gen(env,road))
    env.run()
