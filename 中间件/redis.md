# redis stream 手动ack的目的

在业务的实现过程中，就算没有大量的流量，解耦和异步化几乎也是处处可用，此时MQ就显得尤为重要。但与此同时MQ也是一个蛮重的组件，例如我们如果用RabbitMQ就必须为它搭建一个服务器，同时如果要考虑可用性，就要为服务端建立一个集群，而且在生产如果有问题也需要查找功能。在中小型业务的开发过程中，可能业务的其他整个实现都没这个重。过重的组件服务会成倍增加工作量。
所幸的是，**Redis提供的list数据结构非常适合做消息队列。**
