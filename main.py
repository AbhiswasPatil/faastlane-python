from worker import Worker
from function import Function
from package import Package
from consistentHash import ConsistentHash
from paSch import PaSch


def main():
    # list of workers

    worker = [{"worker_id": "1", "threshhold": 100},
              {"worker_id": "2", "threshhold": 50},
              {"worker_id": "3", "threshhold": 150}]

    global_workers = []
    global_hashworkers = []
    for x in worker:
        global_workers.append(Worker(x["worker_id"], x["threshhold"]))
        global_hashworkers.append(x["worker_id"])

    # bhai implement karna consistent hash idhar
    # print(global_workers)

    # list of fn

    fn = [{
        "function_id": "foo",
        "function_imports": ["p0", "p1"],
        "exec_time": 10
    }, {
        "function_id": "bar",
        "function_imports": ["p0", "p2"],
        "exec_time": 15
    }, {
        "function_id": "par",
        "function_imports": ["p1", "p2"],
        "exec_time": 20
    }]

    global_fn = []
    for x in fn:
        global_fn.append(
            Function(x["function_id"], x["function_imports"], x["exec_time"]))

    # list of packages

    pkgs = [{"package_id": "p0", "exec_time": 3},
            {"package_id": "p1", "exec_time": 4},
            {"package_id": "p2", "exec_time": 5}]

    global_pkgs = []
    for x in pkgs:
        global_pkgs.append(
            Package(x["package_id"], x["exec_time"])
        )

    # fn execution instruction
    fn_inst = [{"fid:": "foo", "timestamp": 0},
               {"fid:": "bar", "timestamp": 1},
               {"fid:": "foo", "timestamp": 2},
               {"fid:": "foo", "timestamp": 3},
               {"fid:": "bar", "timestamp": 2}
               ]

    # now we have all our inputs ready, create instance of scheduler intitalise the scheduler
    scheduler = PaSch(global_hashworkers, global_workers,
                      global_fn, global_pkgs)
    print(scheduler.assignWorker("foo", 1))
    print(scheduler.assignWorker("foo", 2))
    print(scheduler.assignWorker("bar", 2))
    print(scheduler.assignWorker("bar", 3))
    print(scheduler.assignWorker("foo", 1))
    print(scheduler.assignWorker("foo", 2))
    print(scheduler.assignWorker("par", 2))
    print(scheduler.assignWorker("par", 3))
    print(scheduler.assignWorker("bar", 1))
    print(scheduler.assignWorker("foo", 2))
    print(scheduler.assignWorker("par", 2))
    print(scheduler.assignWorker("bar", 3))

    # send requests from here
    # DO : for x in fn_inst

    scheduler.getWorkerDetails()


if __name__ == "__main__":
    main()
