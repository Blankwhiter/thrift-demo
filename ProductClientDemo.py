# -*- coding: UTF-8 -*-
from ProductService import ProductService
from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

if __name__ == '__main__':
    try:
        # 连接Socket
        transport = TSocket.TSocket('localhost', 9090)
        # 获取Transport
        transport = TTransport.TBufferedTransport(transport)
        # TTransport.TFramedTransportFactory()
        # 获取TBinaryProtocol
        protocol = TBinaryProtocol.TBinaryProtocol(transport)
        # 创建一个Client
        client = ProductService.Client(protocol)
        # 连接通道transport
        transport.open()
        # 调用某个没有返回值的函数
        client.printProductName()
        # 调用某个有返回值string的函数
        print(client.getProductDesc("apple"))
        # 调用某个有返回值bool的函数
        print(client.isHaveStock())
        # 关闭通道transport
        transport.close()
    except Thrift.TException as tx:
     print('error  ------>  %s' % (tx.message))