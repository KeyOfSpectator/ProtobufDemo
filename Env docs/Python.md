# Protobuf Python 环境搭建

*参考
https://github.com/google/protobuf/issues/34 
https://github.com/google/protobuf/pull/3
https://developers.google.com/protocol-buffers/docs/

*一 安装Protobuf 编译器 (与Java环境一样)

下载最新版protobuf 
https://developers.google.com/protocol-buffers/docs/downloads 

解压缩后进入文件目录
进入su权限
$ ./configure
$ make
$ make check
$ make install
测试protobuf 版本 
$ protoc --version

*二 Python依赖环境

进入protobuf_home -> python
修改setup.py (解决 test时 ImportError: cannot import name cpp_message 问题)
    在py_modules列表中
    加入 'google.protobuf.pyext'
然后在protobuf_home -> python目录下命令
    $ sudo python setup.py build
    $ sudo python setup.py test (可能会出错 ， 检查报错)
    $ sudo python setup.py install 


三个步骤：
1. 编写 XXX.proto文件
2. 用protoc编译 XXX.proto文件
3. python项目引入编译后的文件，调用API

*例： Person.proto

package com.keyofspectator.protobuf;

option java_package = "com.keyofspectator.protobuf";

option java_outer_classname = "PersonProtos";

message Person {

     optional int64 id=1;

    optional string name=2;

    optional string sex=3;

    optional string tel=4;

}


*编译命令： $protoc --python_out=./workspace/ Person.proto

然后项目引入生成的Person_pb2.py
项目中 import Person_pb2
 

