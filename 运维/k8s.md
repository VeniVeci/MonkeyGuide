k8s的全生命周期管理
在k8s进行管理应用的时候，基本步骤是：创建集群，部署应用，发布应用，扩展应用，更新应用。

虽然 [Docker](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI0MDQ4MTM5NQ%3D%3D%26mid%3D2247509907%26idx%3D1%26sn%3Dc78499a0684f7d7ef82bfdcedd4b4150%26chksm%3De918c28fde6f4b993d5a3ea0600b3a06b6cca768037425dae7142833c8f4cadfbae5dd9d0fc3%26scene%3D21%23wechat_redirect) 已经很强大了，但是在实际使用上还是有诸多不便，比如集群管理、资源调度、文件管理等等。那么在这样一个百花齐放的容器时代涌现出了很多解决方案，比如 Mesos、Swarm、Kubernetes 等等，其中谷歌开源的 [Kubernetes](https://link.zhihu.com/?target=http%3A//mp.weixin.qq.com/s%3F__biz%3DMzI0MDQ4MTM5NQ%3D%3D%26mid%3D2247507390%26idx%3D2%26sn%3D5887ec3021ce80e44a4c62e2253560a8%26chksm%3De918b8a2de6f31b45a71be736919c2a99f4ed2f77b48c10c7482bada97198f9a35682962e683%26scene%3D21%23wechat_redirect) 是作为老大哥的存在。

1、创建集群：为什么要使用集群？

有一句古话叫做三个臭皮匠，赛过诸葛亮，这就是创建集群的原因。。。

使用集群，create cluster是为了掩盖底层的无能，在各种环境中，底层的硬件各不相同，有的是各种低廉的服务器，有的各种云环境，有的是各种vm，有的各种host machine，要想屏蔽底层的细节，增强可靠性和稳定性，从而需要创建集群。

创建集群的好处就是，统一对外提供接口，无须进行各种复杂的调用；提供更好的可靠性，服务器宕机那么频繁，物理磁盘那么容易损坏，无须担心，集群统一进行调配；提供更好的性能，组合集群中各个机器的计算存储网络资源，提供更好的TPS和PS；提供横向扩容的能力，在进行横向扩容的时候，性能基本上能呈线性增长。
————————————————
版权声明：本文为CSDN博主「运维Linux和python」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/TM6zNf87MDG7Bo/article/details/79621510

![image.png](./assets/image.png)

就在Docker容器技术被炒得热火朝天之时，大家发现，如果想要将Docker应用于具体的业务实现，是存在困难的——编排、管理和调度等各个方面，都不容易。于是，人们迫切需要一套管理系统，对Docker及容器进行更高级更灵活的管理。

就在这个时候，K8S出现了。

**K8S，就是基于容器的集群管理平台，它的全称，是kubernetes。**

Kubernetes 这个单词来自于希腊语，含义是**舵手**或 **领航员** 。K8S是它的缩写，用“8”字替代了“ubernete”这8个字符。

和Docker不同，K8S的创造者，是众人皆知的行业巨头—— **Google** 。

然而，K8S并不是一件全新的发明。它的前身，是Google自己捣鼓了十多年的 **Borg系统** 。

K8S是2014年6月由Google公司正式公布出来并宣布开源的。

同年7月，微软、Red Hat、IBM、Docker、CoreOS、 Mesosphere和Saltstack 等公司，相继加入K8S。

之后的一年内，VMware、HP、Intel等公司，也陆续加入。

2015年7月，Google正式加入OpenStack基金会。与此同时，Kuberentes v1.0正式发布。

目前，kubernetes的版本已经发展到V1.13。

# 问题

什么是k8s

有什么用

最常见的场景

一个demo

公司一般怎么用

和我的业务的关联

内部的原理是什么
