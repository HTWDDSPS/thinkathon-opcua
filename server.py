'''
   Show 3 different examples for creating an object:
   1) create a basic object
   2) create a new object type and a instance of the new object type
   3) import a new object from xml address space and create a instance of the new object type
'''
import sys

from numpy import array
sys.path.insert(0, "..")
import asyncio, json

from asyncua import ua, Server, Client

async def add_station(server,id,station_name):
    node = await server.nodes.objects.add_object(
        ua.NodeId.from_string(id),
        station_name,
        ua.NodeId.from_string("ns=3;i=1002")
    )
    return node

async def add_wirkrichtung(parent, parent_name):
    node =  await parent.add_object(
        ua.NodeId.from_string('ns=2;s='+parent_name+'.Wirkrichtung'),
        parent_name,
        ua.NodeId.from_string("ns=3;i=1004")
    ) 
    return node
    
   
    

async def add_messpunkt(parent, messpunkt_name):
    return await parent.add_object(
        ua.NodeId.from_string('ns=2;s='+str(messpunkt_name)),
        messpunkt_name,
        ua.NodeId.from_string("ns=3;i=1003")
    ) 
   


    
     
def create_dict(js: array):
    d = {}
    js = js[15:-2]
    for val in js:
        if val[1] not in d:
            d[val[1]] = True
    return d

def set_values(server, js):
    for value in js:
        if len(js) > 4:
            pass#print(js)
        
def add_werte(server: Server, js):
    pass

async def main():

    # setup our server
    server = Server()
    await server.init()
    js = {}
    with open('./dump.json') as f:
        js = json.load(f)
        
        #print(js)
    set_values(server, js)
    punkt_dict = create_dict(js)
    #print(punkt_dict)
    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")
    station_name = js[0][0]
   
    
    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)
    
    await server.import_xml('./models/spaltmessung.xml')
    nodeIdrollo = 'ns='+str(idx)+';s=' + station_name 
    node = await add_station(server, nodeIdrollo,station_name )
    
    for key in punkt_dict.keys():  
       await add_wirkrichtung(node, key)
        
    werte = js[15:-2]
    
    #ns=2;s=ALSAA0357_O_AA.Wirkrichtung.Flush.A
    #test = 'ns=2;s='+str(js[20][1])+'.Wirkrichtung.'+str(js[20][2])+'.' + str(js[20][0])
    #print(test)
    #node = await server.get_node(ua.NodeId.from_string(test))
    #node.set_value(js[20][-1])
    #add_werte(werte)
    # starting!
    imported = False
    async with server:
        i = 0
        while True:
            await asyncio.sleep(5)           
         




if __name__ == "__main__":
    asyncio.run(main())