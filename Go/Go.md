# 简单介绍

* 性能

GoLang是一种[编译语言](https://www.zhihu.com/search?q=%E7%BC%96%E8%AF%91%E8%AF%AD%E8%A8%80&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "编译语言")，可以编译为机器代码，编译后的[二进制文件](https://www.zhihu.com/search?q=%E4%BA%8C%E8%BF%9B%E5%88%B6%E6%96%87%E4%BB%B6&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "二进制文件")可以直接部署到目标机器而无需额外的依赖。性能优于那些解释语言，比如Python。

go语言目前可以达到c/c++80%的性能，远快于c/c++的编译速度，目前很火的[开源软件](https://www.zhihu.com/search?q=%E5%BC%80%E6%BA%90%E8%BD%AF%E4%BB%B6&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "开源软件")docker、[kubernetes](https://www.zhihu.com/search?q=kubernetes&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "kubernetes")、lxd等软件都是使用go语言编写的。

* 并发 & 通道

这可能是GoLang最受好评的特色。它支持并发，因为它诞生了。它可以充分利用多核功能。GoLang使用goroutine来实现[并发性](https://www.zhihu.com/search?q=%E5%B9%B6%E5%8F%91%E6%80%A7&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "并发性")，它提供了一个非常优雅的goroutine[调度程序](https://www.zhihu.com/search?q=%E8%B0%83%E5%BA%A6%E7%A8%8B%E5%BA%8F&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "调度程序")系统，可以很容易地生成数百万个[goroutine](https://www.zhihu.com/search?q=goroutine&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "goroutine")。堆栈使用也可以动态扩展/收缩，这使内存使用更加智能。这与Java线程不同，后者通常只允许创建数千个线程。

通道是 goroutines 之间通信的优先方式。

* 快速的编译时间

当前我们使用 Go 编写的最大[微服务](https://www.zhihu.com/search?q=%E5%BE%AE%E6%9C%8D%E5%8A%A1&search_source=Entity&hybrid_search_source=Entity&hybrid_search_extra=%7B%22sourceType%22%3A%22answer%22%2C%22sourceId%22%3A2337507216%7D "微服务")的编译时间只需 6 秒。相较于 Java 和 C++呆滞的编译速度，Go 的快速编译时间是一个主要的效率优势。

作者：Go语言入门到精通

链接：https://www.zhihu.com/question/504559302/answer/2337507216

来源：知乎

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

**1.可扩展性** ：Golang在创建时就考虑了可扩展性。它具有内置的并发性，可以同时处理多个任务。Python同样可以使用并发，但不是内置的。它通过线程实现并行性。这意味着，如果你要处理大型数据集，那么Golang似乎是一个更合适的选择。

**2. 性能** ：众所周知，Python不是内存或CPU友好型的编程语言，但由于它拥有大量的库，Python可以有效执行基本的开发任务。Golang具有内置功能，它更适合于微服务软件体系结构。

**3. 应用程序** ：**Python非常适合编写用于人工智能、数据分析、深度学习和Web开发的代码。Golang已普遍用于系统编程，并且受到云计算和集群计算应用程序的开发人员的喜爱。**

**4. 社区和库** ：如前所述，Python的时代赋予了它一定的优势。其中之一是它拥有的库数量以及支持它的大型社区。另一方面，Golang虽然没有Python提供的大量库和社区支持，但仍是一种增长中的语言。我们不应该将Golang踢出局。它的增长和采用率令人难以置信，并且每天都在增长。

作者：黑马程序员Python

链接：https://www.zhihu.com/question/504559302/answer/2502732499

来源：知乎

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

## python转Go

[Go Code Converter (thepythoncode.com)](https://thepythoncode.com/assistant/code-converter/go/)
