from consistentHash import ConsistentHash
from worker import Worker
from function import Function


def main():
    # list of workers

    worker = ["1", 100, "2", 50, "3", 150]
    global_workers = []
    for x in worker:
        global_workers.append(Worker(x))

    print(global_workers)

    # list of fn

    fn = [{
        "function_id": "foo",
        "function_imports": ["p0", "p1"],
        "exec_time": 10
    }, {
        "function_id": "foo",
        "function_imports": ["p0", "p2"],
        "exec_time": 5
    }]

    global_fn = []
    for x in fn:
        global_fn.append(Function(x.function_id, x.function_imports, ))
    # list of packages

    # fn execution instruction


if __name__ == "__main__":
    main()
