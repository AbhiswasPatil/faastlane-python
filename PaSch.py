#it will have Worker class, and will create list of workers from input via user.
#it will also have consistentHash, and will use it to access worker_id (consitentHash <-> workers)
#Lambda will be intialised in here or main.py 

class PaSch:
    def __init__(self,consitent_hash_from_main,fn_with_timestap):
