# Protobuf Java 环境搭建

*参考
http://blog.csdn.net/ajun_studio/article/details/7693056 
https://developers.google.com/protocol-buffers/docs/javatutorial 

*一 安装Protobuf 编译器 (与Python环境一样)

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

*二 Java 编解码实例

引入Java依赖：
	方法一：mvn install 编译好jar包引入
	方法二：maven项目中引入protoc
		pom.xml增加：
			<dependency>
   				<groupId>com.google.protobuf</groupId>
   				<artifactId>protobuf-java</artifactId>
   				<version>2.6.1</version>
			</dependency>

三个步骤：
1. 编写 XXX.proto文件
2. 用protoc编译 XXX.proto文件
3. java项目引入编译后的文件，调用API

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


*编译命令： $protoc --java_out=./workspace/ Person.proto

然后编译 protobuf-java-2.6.1.jar
进入解压的protobuf文件目录 －》 java
$ mvn install
然后Java项目引入 protobuf_home/java/target/protobuf-java-2.6.1.jar

然后把编译好的

PersonProtos.java
放在com.keyofspectator.protobuf 的位置

*主文件内容：

import com.google.protobuf.InvalidProtocolBufferException;

import com.keyofspectator.protobuf.PersonProtos.Person;

public class MainClass {


public static void main(String[] args) {

// TODO Auto-generated method stub

System.out.println("This is a test for protobuf");


        //序列化

        Person.Builder b = Person.newBuilder();

        b.setId(1);

        b.setName("fsc");

        b.setSex("男");

        b.setTel("123456");

        Person p = b.build();

        

        byte [] value = p.toByteArray();

        

        System.out.println("byte array : " + value);

        

        //反序列化：

        Person last = null;

        try {

                last = Person.parseFrom(value);

        } catch (InvalidProtocolBufferException e) {

            // TODO Auto-generated catch block

            e.printStackTrace();

        }

        

        System.out.println("person id : " + last.getId());

        System.out.println("person name : " + last.getName());

        System.out.println("person sex : " + last.getSex());

        System.out.println("person Tel : " + last.getTel());
     

    }

}

