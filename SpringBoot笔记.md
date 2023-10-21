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
