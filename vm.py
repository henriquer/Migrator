class PM:
    """
    A PM must keep track of its memory and its processors
    """
    def __init__(self, memSize, nproc, ip):
        self.nproc = nproc
        for i in range(nproc):
            self.proc.append(None)
        self.mem = memSize
        self.ip = ip
        putProc(self)
        return
    
    def grabProc(self, m):
        self.proc[self.getFreeProc()] = m
        self.nproc -= 1;
        return
    def releaseProc(self, m):
        pm.proc.index(vm)
        
        
    def getFreeProc(self):
        for i in range(1,len(self.proc)):
            if self.proc[i]:
                return i
    
class VM:
    """
    The only thing we need to know about VMs is how much memory it
    needs.  The FlowDB will store the VMs traffic patterns.
    """
    def __init__(self, memSize, pm, ip):
        self.mem = memSize
        self.pm = pm
        self.ip = ip

class Placement:
    def __init__(self):
        self.vmList = []
        self.pmList = []
        return
    
    def addPM(self, pm):
        self.pmList.append(pm)
        return
    
    def addVM(self, vm, pmto):
        pmto.mem -= vm.mem
        vm.pmto   = 
        return
    
    def changePlacement(self, vm, pmto):
        vm.pm.mem += vm.mem
        pm.proc[pm.proc.index(vm)] = None;
        vm.pm      = pmto
        pmto.mem  -= vm.mem
        pm.proc[pmto.getFreeProc()] = vm
        # xm migrate cmd
        return
        

