'''
   Show 3 different examples for creating an object:
   1) create a basic object
   2) create a new object type and a instance of the new object type
   3) import a new object from xml address space and create a instance of the new object type
'''
import sys
sys.path.insert(0, "..")
import asyncio

import asyncua

from asyncua import ua, Server, Client


async def main():

    # setup our server
    server = Server()
    await server.init()

    server.set_endpoint("opc.tcp://0.0.0.0:4840/freeopcua/server/")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://examples.freeopcua.github.io"
    idx = await server.register_namespace(uri)

    await server.import_xml('./models/spaltmessung.xml')
    # starting!
    imported = False
    async with server:
        i = 0
        while True:
            await asyncio.sleep(5)           
         




if __name__ == "__main__":
    asyncio.run(main())