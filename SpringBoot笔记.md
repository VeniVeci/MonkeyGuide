@SpringBootApplication 是什么意思，怎么理解。

是一个注解，如果加上这个注解，会表示这是一个启动类，启动后会

扫描全包

扫描配置

@SpringBootApplication组成部分

```
元注解：
@Target(ElementType.TYPE)
@Retention(RetentionPolicy.RUNTIME)
@Documented
@Inherited

@SpringBootConfiguration
@EnableAutoConfiguration
@ComponentScan

```

整合swagger

引入依赖

添加注解

访问页面测试

类  方法  入参  返回参数

不加配置类的话

Unable to infer base url. This is common when using dynamic servlet registration or when the API is behind an API Gateway. The base url is the root of where all the swagger resources are served. For e.g. if the api is available at http://example.org/api/v2/api-docs then the base url is http://example.org/api/. Please enter the location manually:

需要添加  sw的配置

```java
@Configuration
@EnableSwagger2
public class SwaggerConfig {
    @Bean
    public Docket productApi() {
        return new Docket(DocumentationType.SWAGGER_2)
                .apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.withMethodAnnotation(ApiOperation.class))  //添加ApiOperiation注解的被扫描
                .paths(PathSelectors.any())
                .build();

    }

    private ApiInfo apiInfo() {
        return new ApiInfoBuilder().title(”swagger和springBoot整合“).description(”swagger的API文档")
                .version("1.0").build();
    }

}
```

# 整合redis

添加依赖

添加配置文件 yml

引入工具类

使用redis 实现 增删改查

实现一些 压测

看一下redis 这边的性能如何

侧重点在redis

事务怎么做到

```yml
server:
  port: 8080

spring:
  datasource:
    url: jdbc:mysql://localhost:3306/mall?useUnicode=true&characterEncoding=utf-8&serverTimezone=Asia/Shanghai
    username: root
    password: root
  redis:
    host: localhost
    port: 6279
    password:
    database: 0
    jedis:
      pool:
        max-active: 8
        max-wait: -1ms
        max-idle: 8
        min-idle: 0
    timeout: 3000ms

mybatis:
  mapper-locations:
    - classpath:mapper/*.xml
    - classpath*:com/**/mapper/*.xml

redis:
  key:
    prefix:
      authCode: "portal:authCode:"
#       authCode 类型的数据在Redis中的键会以 "portal:authCode:" 作为前缀。
    expire:
      authCode: 120




```

## 为啥redis的配置一个在根节点  一个在 spring下

将这两部分配置分开是为了更好地组织和管理不同类型的Redis配置。`spring` 节点下的配置通常用于与底层的Redis连接相关，而根节点下的配置则用于定义应用中的具体数据管理策略，例如数据键的前缀和过期时间。这种分离使得配置更具可读性和可维护性。同时，它也更符合配置的逻辑组织，以确保不同部分的配置清晰明了。
