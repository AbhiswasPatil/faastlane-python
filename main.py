from sqlite3 import Timestamp

from numpy import True_
from worker import Worker
from function import Function
from package import Package
from paSch import PaSch


def main():
    # list of workers

    workers = [{"worker_id": "1", "threshold": 100},
              {"worker_id": "2", "threshold": 50},
              {"worker_id": "3", "threshold": 150}]

    global_workers = []
    global_hashworkers = []
    for x in workers:
        global_workers.append(Worker(x["worker_id"], x["threshold"]))
        global_hashworkers.append(x["worker_id"])

    # bhai implement karna consistent hash idhar
    # print(global_workers)

    # list of fn

    fn = [{
        "function_id": "foo",
        "function_imports": ["p0", "p1"],
        "function_size": 10
    }, {
        "function_id": "bar",
        "function_imports": ["p0", "p2"],
        "function_size": 15
    }, {
        "function_id": "par",
        "function_imports": ["p1", "p2"],
        "function_size": 20
    }]

    global_fn = []
    for x in fn:
        global_fn.append(
            Function(x["function_id"], x["function_imports"], x["function_size"]))

    # list of packages

    pkgs = [{"package_id": "p0", "package_size": 3},
            {"package_id": "p1", "package_size": 4},
            {"package_id": "p2", "package_size": 5}]

    global_pkgs = []
    for x in pkgs:
        global_pkgs.append(
            Package(x["package_id"], x["package_size"])
        )

    # fn execution instruction
    fn_inst = [{"fid:": "foo", "timestamp": 0},
               {"fid:": "bar", "timestamp": 1},
               {"fid:": "foo", "timestamp": 2},
               {"fid:": "foo", "timestamp": 3},
               {"fid:": "bar", "timestamp": 2}]

    # now we have all our inputs ready, create instance of scheduler intitalise the scheduler
    scheduler = PaSch(global_hashworkers, global_workers,
                      global_fn, global_pkgs)

    while True:
        print("\n")
        print("1. Add a new worker.")
        print("2. Update an existing worker's threhold.")
        print("3. Remove a worker.")
        print("4. View all workers.")
        print("5. Execute a function")
        print("0. Exit")
        print("\n")
        option = int(input("Choose an option: "))
        print("\n")
        match option:
            case 1:
                w_id = input("Enter worker id: ")
                thres = int(input("Enter worker's threshold: "))
                workers.append({"worker_id": w_id, "threshold": thres})
                print("Worker {} successfully added!".format(w_id))
            case 2:
                w_id = input("Enter worker id: ")
                thres = int(input("Enter worker's threshold: "))
                for i, worker in enumerate(workers):
                    if w_id  == worker["worker_id"]:
                        worker["threshold"] = thres
                        break
                print("Worker {} successfully updated!".format(w_id))
            case 3:
                w_id = input("Enter worker id: ")
                for i, worker in enumerate(workers):
                    if w_id  == worker["worker_id"]:
                        del workers[i]
                print("Worker {} successfully removed!".format(w_id))
            case 4:
                print("Workers: ")
                print(workers)
            case 5:
                f_id = input("Enter the function id: ")
                t_stamp = int(input("Enter the timestamp: "))
                print(scheduler.assignWorker(f_id, t_stamp))
                print("Function {} successfully executed!".format(f_id))
            case 0: 
                exit()
            case default:
                continue

    # print(scheduler.assignWorker("foo", 1))
    # print(scheduler.assignWorker("foo", 2))
    # print(scheduler.assignWorker("bar", 2))
    # print(scheduler.assignWorker("bar", 3))
    # print(scheduler.assignWorker("foo", 1))
    # print(scheduler.assignWorker("foo", 2))
    # print(scheduler.assignWorker("par", 2))
    # print(scheduler.assignWorker("par", 3))
    # print(scheduler.assignWorker("bar", 1))
    # print(scheduler.assignWorker("foo", 2))
    # print(scheduler.assignWorker("par", 2))
    # print(scheduler.assignWorker("bar", 3))

    # send requests from here
    # DO : for x in fn_inst

    # for getWorker Details create an option in while loop of inctructions to run it at a timestamp 
    scheduler.getWorkerDetails(timestamp=9)


if __name__ == "__main__":
    main()
