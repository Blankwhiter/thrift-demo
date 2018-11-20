# -*- coding: UTF-8 -*-
from ProductService import ProductService

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer
# 接口实现
class ProductServiceHandler:
    def printProductName(self):
        print("你调用到了打印产品名称的方法")

    def getProductDesc(self, name):
        s = "你获得产品名称为"+name+"的描述"
        print(s)
        return s

    def isHaveStock(self):
        print("顾客是上帝，你想要，我们绝对不会缺货")
        return True

#对接thrift
if __name__ == '__main__':
    handler = ProductServiceHandler()
    processor = ProductService.Processor(handler)  # 根据handler创建一个processor
    transport = TSocket.TServerSocket("127.0.0.1", "9090")  # 指定端口启动transport
    tfactory = TTransport.TBufferedTransportFactory()     #按buffer传输
    # tfactory = TTransport.TFramedTransportFactory()     #按帧传输
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()  #按二进制传输协议
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print("------ running -----")
    server.serve()
    print("------ over -----")


