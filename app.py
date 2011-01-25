import vm

class Datacenter():
    def __init__():
        self.vm

class NetFlowCollector(protocol.DatagramProtocol):
    """This class that holds the rules for processing netflow records"""
    
    netFlowHeaderFormat = "!HHIIIIxxH";
    netFlowHeaderSize   = struct.calcsize(netFlowHeaderFormat);
    
    netFlowRecordFormat = "!IIxxxxxxxxIIIIHHxxBxxxxxxxxx";
    netFlowRecordSize   = struct.calcsize(netFlowRecordFormat);
    
    def datagramReceived(self, data, (host, port)):
        # print '> Received ', len(data), ' bytes';
        netFlowHeader = struct.unpack(
            self.netFlowHeaderFormat, data[:self.netFlowHeaderSize]);
        i=0;
        while ((self.netFlowHeaderSize+i*48) < len(data)):
            recordStart = self.netFlowHeaderSize+(i*48);
            recordEnd   = self.netFlowHeaderSize+((i+1)*48);
            netFlowRecordStruct = data[recordStart:recordEnd];
            
            netFlowRecord = struct.unpack(
                self.netFlowRecordFormat, netFlowRecordStruct);
            
            flow(netFlowRecord[0], netFlowRecord[1], netFlowRecord[3]);
            print '> ', self.long2ip(netFlowRecord[0]), ' -> ',; 
            print self.long2ip(netFlowRecord[1]), ' ',;
            print netFlowRecord[3], 'bytes' ;
            i=i+1;
        
    
    def long2ip(self, val):
        slist = []
        for x in range(0,4):
            slist.append(str(int(val >> (24 - (x * 8)) & 0xFF)))
        return ".".join(slist)
    


def main():
    #factory = protocol.ServerFactory();
    #factory.protocol = NetFlowReceiver
    #reactor.listenUDP(6666, factory);
    reactor.listenUDP(6666, NetFlowCollector());
    reactor.run();

if __name__ == '__main__':
    main();
