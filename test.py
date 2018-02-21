from simpy import Environment, Event, Store


class Res:
    def __init__(self, env: Environment, event, capacity):
        self.env = env
        self.capacity = capacity
        self.num = 0
        self.event = event

    def request(self, events, i):
        self.num += 1
        self.trigger()
        print(i, events, env.now, self.num)
        return self

    def release(self):
        self.num -= 1
        self.trigger()

    def trigger(self):
        if self.num < self.capacity:
            self.event.succeed()
            self.event = self.env.event()


def p(env, res, s):
    for i in range(10):
        yield env.timeout(1)
        yield res.event
        res.request('push', i)
        env.process(run(env, 'push end', res, i, s))


def p2(env, res, s):
    for i in range(10):
        res.request('land', i)
        env.process(run(env, 'land end', res, i, s))


def run(env, events, res, i, s):
    yield env.timeout(24)
    res.release()
    print(i, events, env.now, res.num)


env = Environment()
event = Event(env)
s = Store(env)

res = Res(env, event, capacity=10)
env.process(p(env, res, s))
env.process(p2(env, res, s))
env.run()
