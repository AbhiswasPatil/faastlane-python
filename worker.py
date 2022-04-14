# DO: import threshhold, cachedCleanTime from globalVariables files

#Assumptions : workers and worker is just worker_id or worker_name not worker object

class Worker:
    def __init__(self, worker_id, threshold):
        self.workerId = worker_id
        self.threshold = threshold
        self.currentLoad = 0
        self.cachedPackages = []
        self.lastExcecutedTime = {} # Dict which shows last executed time for a package on this worker node
        # DO :self.threshhold = threshhold
        # DO : self.cacheCleanTime = cacheCleanTime

