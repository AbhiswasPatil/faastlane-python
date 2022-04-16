# DO: import threshold, cachedCleanTime from globalVariables files

# Assumptions : workers and worker is just worker_id or worker_name not worker object

class Worker:
    def __init__(self, worker_id, threshold):
        self.worker_id = worker_id
        self.threshold = threshold
        self.currentLoad = 0
        self.cachedPackages = []
        # Dict which shows last executed time for a package on this worker node
        self.lastExcecutedTime = {}
        # DO :self.threshold = threshold
        # DO : self.cacheCleanTime = cacheCleanTime
