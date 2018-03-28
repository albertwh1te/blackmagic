from simpy import Environment, Resource


def request_all(items: list) -> list:
    """
    request all items and return the list
    """
    # return list(map(lambda x: x.request(), items))
    requested_items = []
    for item in items:
        requested = yield item.request()
        requested_items.append(item)
        print(requested)
    return requested_items


def release_all(items: list,requested_list) -> None:
    """
    release all items
    """
    # list(map(lambda x: x.release(), items))
    for i,v in enumerate(items):
        print(i,v)
        print(len(list(requested_list)))
        v.release(list(requested_list)[0])


def test1(env, items):
    requested_list = request_all(items)
    import ipdb; ipdb.set_trace()
    yield env.timeout(11)
    print(env.now)
    release_all(items,requested_list)


def test2(env, items):
    requested_list = request_all(items)
    yield env.timeout(11)
    print(env.now)
    release_all(items,requested_list)


env = Environment()
res_list = [Resource(env, capacity=1) for i in range(10)]
env.process(test1(env, res_list))
env.process(test2(env, res_list))
env.run()
