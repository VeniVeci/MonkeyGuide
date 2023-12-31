# 使用步骤

## 直接使用

### Elasticsearch的安装和使用

1. 下载Elasticsearch6.2.2的zip包，并解压到指定目录，下载地址：[https://www.elastic.co/cn/downloads/past-releases/elasticsearch-6-2-2](https://www.elastic.co/cn/downloads/past-releases/elasticsearch-6-2-2)
2. 运行bin目录下的elasticsearch.bat启动Elasticsearch
3. 安装图形化插件head，用来可视化存储在es中的数据；[ElasticSearch入门篇（保姆级教程） - coderxz - 博客园 (cnblogs.com)](https://www.cnblogs.com/coderxz/p/13268417.html#24-%E5%AE%89%E8%A3%85%E5%9B%BE%E5%BD%A2%E5%8C%96%E6%8F%92%E4%BB%B6)
4. 按照博客教程启动 head，通过浏览器访问es；
5. ![image.png](./assets/1699779731646-image.png)

![image.png](./assets/1699779768503-image.png)

![image.png](./assets/1699779851768-image.png)

## java项目中使用

引入依赖

```java
        <!--Elasticsearch相关依赖-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-elasticsearch</artifactId>
        </dependency>
```

yml配置

```java
spring:
  data:
    elasticsearch:
      repositories:
        enabled: true
      cluster-nodes: 127.0.0.1:9300 # es的连接地址及端口号
      cluster-name: elasticsearch # es集群的名称

```

编写接口类使用

# 相关博客

[ElasticSearch入门篇（保姆级教程） - coderxz - 博客园 (cnblogs.com)](https://www.cnblogs.com/coderxz/p/13268417.html#8%E6%9F%A5%E8%AF%A2%E6%96%87%E6%A1%A3document-----get)

[Elasticsearch 入门 - 《elasticsearch 中文文档帮助手册教程 V7.11》 - 极客文档 (geekdaxue.co)](https://geekdaxue.co/read/elasticsearch-doc-zh-v7.11/docs-getting_started-getting_started.md)

[ElasticSearch原理 - 神一样的存在 - 博客园 (cnblogs.com)](https://www.cnblogs.com/dreamroute/p/8484457.html)

Elasticsearch 是一个分布式可扩展的实时搜索和分析引擎,一个建立在全文搜索引擎 Apache Lucene(TM) 基础上的搜索引擎.当然 Elasticsearch 并不仅仅是 Lucene 那么简单，它不仅包括了全文搜索功能，还可以进行以下工作:

* 分布式实时文件存储，并将每一个字段都编入索引，使其可以被搜索。
* 实时分析的分布式搜索引擎。
* 可以扩展到上百台服务器，处理PB级别的结构化或非结构化数据。

# 原理

## 索引

Elasticsearch最关键的就是提供强大的索引能力了，其实InfoQ的这篇[时间序列数据库的秘密(2)——索引](http://www.infoq.com/cn/articles/database-timestamp-02?utm_source=infoq&utm_medium=related_content_link&utm_campaign=relatedContent_articles_clk)写的非常好，我这里也是围绕这篇结合自己的理解进一步梳理下，也希望可以帮助大家更好的理解这篇文章。

Elasticsearch索引的精髓：

> 一切设计都是为了提高搜索的性能

另一层意思：为了提高搜索的性能，难免会牺牲某些其他方面，比如插入/更新，否则其他数据库不用混了。前面看到往Elasticsearch里插入一条记录，其实就是直接PUT一个json的对象，这个对象有多个fields，比如上面例子中的 *name, sex, age, about, interests* ，那么在插入这些数据到Elasticsearch的同时，Elasticsearch还默默的为这些字段建立索引--倒排索引，因为Elasticsearch最核心功能是搜索。

### Elasticsearch是如何做到快速索引的

InfoQ那篇文章里说Elasticsearch使用的倒排索引比关系型数据库的B-Tree索引快

# 应用场景

Elasticsearch 为各种数据类型提供接近实时的搜索和分析。不论你有结构化或非结构化的文本、数字数据，还是地理空间数据，Elasticsearch 能以支持快速搜索的方式高效地存储和索引它。你可以远超简单数据检索和聚合信息的方式去发现你数据中的趋势和模式。而且，随着你数据和查询量的增长，Elasticsearch 分布式的特性允许你的部署能随着它无缝地增长匹配。

虽然不是每个问题都是搜索问题，但 Elasticsearch 在大量实例中提供了处理数据的速度和灵活性：

* 为应用或者网站添加搜索框
* 存储和分析日志、度量和安全事件数据
* 使用机器学习，实时自动建模你的数据行为
* 使用 Elasticsearch 作为存储引擎来自动化业务工作流
* 使用 Elasticsearch 作为地理信息系统（GIS）管理、集成和分析空间信息，以及使用 Elasticsearch 作为生物学信息研究工具处理基因数据
* 2013年初，GitHub抛弃了Solr，采取ElasticSearch 来做PB级的搜索。 “GitHub使用ElasticSearch搜索20TB
  的数据，包括13亿文件和1300亿行代码”
* 维基百科：启动以elasticsearch为基础的核心搜索架构
* SoundCloud：“SoundCloud使用ElasticSearch为1.8亿用户提供即时而精准的音乐搜索服务”
* 百度：百度目前广泛使用ElasticSearch作为文本数据分析，采集百度所有服务器上的各类指标数据及用户自定义数据，通过对各种数据进行多维分析展示，辅助定位分析实例异常或业务层面异常。目前覆盖百度内部20多个业务线（包括casio、云分析、网盟、预测、文库、直达号、钱包、风控等），单集群最大100台机器，200个ES节点，每天导入30TB+数据
* 新浪使用ES 分析处理32亿条实时日志
* 阿里使用ES 构建挖财自己的日志采集和分析体系

注意：**es使用java开发，使用lucene作为核心，需要配置好java环境！（jdk1.8以上）**

**9300是tcp通信端口，es集群之间使用tcp进行通信，9200是http协议端口。**

# 概念

![image.png](./assets/image.png)

## 1）index索引

> 一个索引就是一个拥有几分相似特征的文档的集合。比如说，你可以有一个客户数据的索引，另一个产品目录的索引，还有一个订单数据的索引。一个索引由一个名字来标识（必须全部是小写字母的），并且当我们要对对应于这个索引中的文档进行索引、搜索、更新和删除的时候，都要使用到这个名字。在一个集群中，可以定义任意多的索引。**可类比mysql中的数据库**  目前的索引是 pms  商场算是数据库

## 2）type类型

> 在一个索引中，你可以定义一种或多种类型。一个类型是你的索引的一个逻辑上的分类/分区，其语义完全由你来定。通常，会为具有一组共同字段的文档定义一个类型。比如说，我们假设你运营一个博客平台并且将你所有的数据存储到一个索引中。在这个索引中，你可以为用户数据定义一个类型，为博客数据定义另一个类型，当然，也可以为评论数据定义另一个类型。 **可类比mysql中的表**   索引中有几种不同类型的 数据 ，比如品牌，文章，会员

## 3)  Filed字段

> 相当于是数据表的字段，对文档数据根据不同属性进行的分类标识 。

## 4）映射mapping

> mapping是处理数据的方式和规则方面做一些限制，如某个字段的数据类型、默认值、分析器、是否被索引等等，这些都是映射里面可以设置的，其它就是处理es里面数据的一些使用规则设置也叫做映射，按着最优规则处理数据对性能提高很大，因此才需要建立映射，并且需要思考如何建立映射才能对性能更好。**相当于mysql中的创建表的过程，设置主键外键等等**

## 5）document文档

> 一个文档是一个可被索引的基础信息单元。比如，你可以拥有某一个客户的文档，某一个产品的一个文档，当然，也可以拥有某个订单的一个文档。文档以JSON（Javascript Object Notation）格式来表示，而JSON是一个到处存在的互联网数据交互格式。在一个index/type里面，你可以存储任意多的文档。注意，尽管一个文档，物理上存在于一个索引之中，文档必须被索引/赋予一个索引的type。 **插入索引库以文档为单位，类比与数据库中的一行数据**

## 6）集群cluster

> 一个集群就是由一个或多个节点组织在一起，它们共同持有整个的数据，并一起提供索引和搜索功能。一个集群由 一个唯一的名字标识，这个名字默认就是“elasticsearch”。这个名字是重要的，因为一个节点只能通过指定某个集 群的名字，来加入这个集群。

## 7）节点node

> 一个节点是集群中的一个服务器，作为集群的一部分，它存储数据，参与集群的索引和搜索功能。和集群类似，一 个节点也是由一个名字来标识的，默认情况下，这个名字是一个随机的漫威漫画角色的名字，这个名字会在启动的 时候赋予节点。这个名字对于管理工作来说挺重要的，因为在这个管理过程中，你会去确定网络中的哪些服务器对 应于Elasticsearch集群中的哪些节点。

> 一个节点可以通过配置集群名称的方式来加入一个指定的集群。默认情况下，每个节点都会被安排加入到一个叫 做“elasticsearch”的集群中，这意味着，如果你在你的网络中启动了若干个节点，并假定它们能够相互发现彼此， 它们将会自动地形成并加入到一个叫做“elasticsearch”的集群中。

> 在一个集群里，只要你想，可以拥有任意多个节点。而且，如果当前你的网络中没有运行任何Elasticsearch节点， 这时启动一个节点，会默认创建并加入一个叫做“elasticsearch”的集群。

## 8）分片和复制 shards&replicas

> 一个索引可以存储超出单个结点硬件限制的大量数据。比如，一个具有10亿文档的索引占据1TB的磁盘空间，而任一节点都没有这样大的磁盘空间；或者单个节点处理搜索请求，响应太慢。为了解决这个问题，Elasticsearch提供了将索引划分成多份的能力，这些份就叫做分片。当你创建一个索引的时候，你可以指定你想要的分片的数量。每个分片本身也是一个功能完善并且独立的“索引”，这个“索引”可以被放置到集群中的任何节点上。分片很重要，主要有两方面的原因： 1）允许你水平分割/扩展你的内容容量。 2）允许你在分片（潜在地，位于多个节点上）之上进行分布式的、并行的操作，进而提高性能/吞吐量。

> 至于一个分片怎样分布，它的文档怎样聚合回搜索请求，是完全由Elasticsearch管理的，对于作为用户的你来说，这些都是透明的。

> 在一个网络/云的环境里，失败随时都可能发生，在某个分片/节点不知怎么的就处于离线状态，或者由于任何原因消失了，这种情况下，有一个故障转移机制是非常有用并且是强烈推荐的。为此目的，Elasticsearch允许你创建分片的一份或多份拷贝，这些拷贝叫做复制分片，或者直接叫复制。

> 复制之所以重要，有两个主要原因： 在分片/节点失败的情况下，提供了高可用性。因为这个原因，注意到复制分片从不与原/主要（original/primary）分片置于同一节点上是非常重要的。扩展你的搜索量/吞吐量，因为搜索可以在所有的复制上并行运行。总之，每个索引可以被分成多个分片。一个索引也可以被复制0次（意思是没有复制）或多次。一旦复制了，每个索引就有了主分片（作为复制源的原来的分片）和复制分片（主分片的拷贝）之别。分片和复制的数量可以在索引创建的时候指定。在索引创建之后，你可以在任何时候动态地改变复制的数量，但是你事后不能改变分片的数量。

> 默认情况下，Elasticsearch中的每个索引被分片5个主分片和1个复制，这意味着，如果你的集群中至少有两个节点，你的索引将会有5个主分片和另外5个复制分片（1个完全拷贝），这样的话每个索引总共就有10个分片。

## 实例：

mall：商城项目

在索引库里新建一个 mall 索引，用来检索 mall项目中的全部数据。

mall索引中添加品牌类型，用户类型，商品类型，订单类型这几种 type 的数据来区分不同的数据，也就是品牌信息表，用户信息表，商品信息表，订单信息表

对于每一种类型，有一些field，比如品牌的id，名称，描述等等，这样类型的结构就定义好了

接下来就是插入文档document，也就是插入数据。

# 遇到的问题

## elasticsearch中head连不上es，集群健康值: 未连接

解决：

需要在elasticsearch的配置文件中添加以下配置：

启用跨源资源共享 (CORS)

```java
http.cors.enabled: true
http.cors.allow-origin: "*"
network.host: 127.0.0.1
```

network.host: 127.0.0.1

指定服务监听的网络接口。在这里，服务将仅监听本地回环地址（127.0.0.1），这意味着它只能从本地访问，而不对外部网络可见。如果要允许外部访问，你可能需要将其设置为服务器的公共 IP 地址或使用 0.0.0.0 表示监听所有可用的网络接口。
