#it will also have consistentHash, and will use it to access worker_id (consitentHash <-> workers)

import math
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
        self.threshold = 1

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
        # print(type(pkg))
        if(err!= "") :
            print("No packages in function to run !!!")
        
        # selectedWorker1,selectedWorker2 -> worker_id
        err1,selectedWorker1 = self.consitentHash.getWorker(pkg)
        err2,selectedWorker2 = self.consitentHash.getWorker(pkg+self.salt)
        print("Selected workers for function,",function_id,"are :",selectedWorker1,selectedWorker2)

        load_1 = self.getLoad(selectedWorker1)
        load_2 = self.getLoad(selectedWorker2)
        # print("load1 :",load_1)
        # print("load2 :",load_2)

        #chooses the least loaded among 2 chosen worker nodes
        chosen_power_of_two_node = selectedWorker1
        if(load_1>load_2):
            chosen_power_of_two_node=selectedWorker2

        chosen_node_to_run = chosen_power_of_two_node
        index_of_chosen_node_to_run = self.getIndexInWorkersArray(chosen_node_to_run) 

        if(self.getLoad(chosen_power_of_two_node) >= self.threshold ):
            chosen_node_to_run = self.getLeastLoadedWorker() # returns worker_id
            index_of_chosen_node_to_run=self.getIndexInWorkersArray(chosen_node_to_run)
        
        # DO: what if least loaded is also crossing threshold ??

        # all clear till here


        # increase its currentLoad, update caached packages, after all that update the workers array in Pasch
        # self.workerId = worker_id , self.threshold = threshold, self.currentLoad = 0
        # self.cachedPackages = [], self.lastExcecutedTime = {}

        # calculate if biggest package was hit or missed

        if(self.workers[index_of_chosen_node_to_run].lastExcecutedTime.get(pkg) == None) :
            # first time caching pkg
            print("First time importing on node :",self.workers[index_of_chosen_node_to_run].worker_id,"package: ",pkg)
        elif(self.workers[index_of_chosen_node_to_run].lastExcecutedTime[pkg] + cacheCleanTime > timestamp) :
            print("CACHE HIT ON NODE :",self.workers[index_of_chosen_node_to_run].worker_id, "for package :", pkg)
        else :
            print("CACHE missed !!!! ON NODE :",self.workers[index_of_chosen_node_to_run].worker_id, "for package :",pkg)

        
        #updating load
        workerNodes[index_of_chosen_node_to_run].currentLoad += 1

        #updating the cache executed time for all imported packages including the biggest package
        # packages_imported contains array of package_id
        packages_imported = self.functions[self.getIndexInFunctionsArray(function_id)].function_imports 
        for i in range(0,len(packages_imported)):
            workerNodes[index_of_chosen_node_to_run].lastExcecutedTime[packages_imported[i]] = timestamp


        #updating the changes in object
        self.workers = workerNodes
        # print({"",workerNodes[index_of_chosen_node_to_run].worker_id})
        return {"",workerNodes[index_of_chosen_node_to_run].worker_id}



    def getLeastLoadedWorker(self):
        #uses all keys in consistent Hash and gets min loaded
        min_worker_id =""
        min_worker_id_load = math.inf
        for i in range(0,len(self.workers)) :
            if(min_worker_id_load >self.workers[i].currentLoad) :
                min_worker_id_load = self.workers[i].currentLoad
                min_worker_id = self.workers[i].worker_id
        
        return min_worker_id


    def getLoad(self,worker_id):
        #returns load of the worker
        return self.workers[self.getIndexInWorkersArray(worker_id)].currentLoad


    def getWorkerDetails(self):
        for i in range(0,len(self.workers)) :
            print("worker_id:",self.workers[i].worker_id)
            print("threshold",self.workers[i].threshold)
            print("currentLoad",self.workers[i].currentLoad)
            # print(self.workers[i].cachedPackages)
            print("lastExcecutedTime",self.workers[i].lastExcecutedTime)
            print("\n:::::::\n")



