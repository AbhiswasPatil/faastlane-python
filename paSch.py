#it will also have consistentHash, and will use it to access worker_id (consitentHash <-> workers)

import string
from consistentHash import ConsistentHash
from GLOBAL import *
from function import Function
from worker import Worker

class PaSch:
    # workers: Worker[], functions : Function[], packages : Package[]
    def __init__(self,hashworkers, workers, functions, packages):
        
        self.consitentHash = ConsistentHash(hashworkers) #so now updates in hash are part of pasch so no worries
        
        self.salt = salt
        self.threshhold = 20

        self.workers = workers
        self.functions = functions
        self.packages = packages

    def getLoad(self, worker_id):
        
        for x in self.workers :
            if(x.worker_id == worker_id):
                return x.currentLoad

    def getIndexInWorkersArray(self,worker_id):
        for i in range(0,len(self.workers)) :
            # print(self.workers[i])
            if(self.workers[i].worker_id == worker_id):
                return i

    def getIndexInFunctionsArray(self,function_id):
        for i in range(0,len(self.functions)) :
            if(self.functions[i].function_id == function_id):
                return i

    def getIndexInPackagesArray(self,package_id):
        for i in range(0,len(self.packages)) :
            if(self.packages[i].package_id == package_id):
                return i

    def assignWorker(self,function_id,timestamp):
        
        workerNodes = self.workers

        # if(len(workerNodes) == 0):
        #     return {"there are no worker nodes", None}

        function_object = self.functions[self.getIndexInFunctionsArray(function_id)]

        err, pkg = function_object.getLargestPackage()
        if(err!= "") :
            print("No packages in function to run !!!")
        
        # selectedWorker1,selectedWorker2 -> worker_id
        err1,selectedWorker1 = self.consitentHash.getWorker(pkg)
        err2,selectedWorker2 = self.consitentHash.getWorker(pkg+self.salt)
        print(selectedWorker1,selectedWorker2)

        load_1 = self.getLoad(selectedWorker1)
        load_2 = self.getLoad(selectedWorker2)
        print("load1 :",load_1)
        print("load2 :",load_2)

        #chooses the least loaded among 2 chosen worker nodes
        chosen_power_of_two_node = selectedWorker1
        if(load_1>load_2):
            chosen_power_of_two_node=selectedWorker2

        # all clear till here
        chosen_node_to_run = chosen_power_of_two_node
        index_of_chosen_node_to_run = self.getIndexInWorkersArray(chosen_node_to_run) 

        if(self.getLoad(chosen_power_of_two_node) >= self.threshhold ):
            chosen_node_to_run = self.getLeastLoadedWorker() # returns worker_id
            index_of_chosen_node_to_run=self.getIndexInWorkersArray(chosen_node_to_run)
        

        # increase its currentLoad, update caached packages, after all that update the workers array in Pasch
        # self.workerId = worker_id
        # self.threshhold = threshhold
        # self.currentLoad = 0
        # self.cachedPackages = []
        # self.lastExcecutedTime = {}

        #updating load
        workerNodes[index_of_chosen_node_to_run].currentLoad += 1

        #updating the cache executed time
        packages_imported = self.functions[self.getIndexInFunctionsArray(function_id)].function_imports #contains array of package_id
        for i in range(0,len(packages_imported)):
            workerNodes[index_of_chosen_node_to_run].lastExcecutedTime[packages_imported[i]] = timestamp

        # DO: can calculate if biggest package was hit or missed

        #updating the changes in object
        self.workers = workerNodes
        print({"",workerNodes[index_of_chosen_node_to_run].worker_id})
        return {"",workerNodes[index_of_chosen_node_to_run].worker_id}

    def getLeastLoadedWorker():
        #uses all keys in consistent Hash and gets min loaded
        return

    def getLoad(self,worker_id):
        #returns load of the worker
        return self.workers[self.getIndexInWorkersArray(worker_id)].currentLoad

    def getWorkerDetails(self):
        for i in range(0,len(self.workers)) :
            print("worker_id:",self.workers[i].worker_id)
            print("threshhold",self.workers[i].threshhold)
            print("currentLoad",self.workers[i].currentLoad)
            # print(self.workers[i].cachedPackages)
            print("lastExcecutedTime",self.workers[i].lastExcecutedTime)
            print("\n:::::::\n")



