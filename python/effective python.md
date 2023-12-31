# 第1章　培养Pythonic思维


Python开发者不喜欢写复杂的代码，他们喜欢用直观、简洁而且容易看懂的方式来编写（在Python解释器界面输入import this，可以查看The Zen of Python）。


Python Enhancement Proposal #8叫作PEP 8，它是一份针对Python代码格式而编订的风格指南。尽管只要语法正确，代码随便怎么写都行，但采用一致的风格可以使代码更易读、更易懂。如果你的代码风格和其他Python程序员的相同，那么就能够更加顺利地与大家一起做项目。即便你的代码只给自己看，也应该按照这套风格来写，以便以后修改更加容易一些，而且能够避开很多常见的错误。


与命名有关的建议PEP 8建议采用不同的方式来给Python代码中的各个部分命名，这样在阅读代码时，就可以根据这些名称看出它们在Python语言中的角色。遵循以下与命名相关的建议。函数、变量及属性用小写字母来拼写，各单词之间用下划线相连，例如：lowercase_underscore。受保护的实例属性，用一个下划线开头，例如：_leading_underscore。私有的实例属性，用两个下划线开头，例如：__double_leading_underscore。类（包括异常）命名时，每个单词的首字母均大写，例如：CapitalizedWord。模块级别的常量，所有字母都大写，各单词之间用下划线相连，例如：ALL_CAPS。类中的实例方法，应该把第一个参数命名为self，用来表示该对象本身。类方法的第一个参数，应该命名为cls，用来表示这个类本身。


与表达式和语句有关的建议The Zen of Python中提到：“每件事都应该有简单的做法，而且最好只有一种。”PEP 8就试着运用这个理念，来规范表达式和语句的写法。采用行内否定，即把否定词直接写在要否定的内容前面，而不要放在整个表达式的前面，例如应该写if a is not b，而不是if not a is b。不要通过长度判断容器或序列是不是空的，例如不要通过if len(somelist) == 0判断somelist是否为[]或''等空值，而是应该采用if not somelist这样的写法来判断，因为Python会把空值自动评估为False。如果要判断容器或序列里面有没有内容（比如要判断somelist是否为[1]或'hi'这样非空的值），也不应该通过长度来判断，而是应该采用if somelist语句，因为Python会把非空的值自动判定为True。不要把if语句、for循环、while循环及except复合语句挤在一行。应该把这些语句分成多行来写，这样更加清晰。


提示Pylint（https://www.pylint.org/）是一款流行的Python源码静态分析工具。它可以自动检查受测代码是否符合PEP 8风格指南，而且还能找出Python程序里的许多种常见错误。很多IDE（集合成开发环境）与编辑器，都包含这样的linting工具或者支持类似的插件。



# 第53条　可以用线程执行阻塞式I/O，但不要用它做并行计算


Python语言的标准实现叫作CPython，它分两步来运行Python程序。首先解析源代码文本，并将其编译成字节码（bytecode）。字节码是一种底层代码，可以把程序表示成8位的指令（从Python 3.6开始，这种底层代码实际上已经变成16位了，所以应该叫作wordcode才对，但基本原理依然相同）。然后，CPython采用基于栈的解释器来运行字节码。这种字节码解释器在执行Python程序的过程中，必须确保相关的状态不受干扰，所以CPython会用一种叫作全局解释器锁（global interpreter lock，GIL）的机制来保证这一点。

若要CPython把多个核心充分利用起来，还是有一些办法的，但那些办法都不采用标准的Thread类（参见第64条），而且实现起来也需要大量的精力。既然有这么多限制，那Python还支持多线程干什么？这其实有两个原因。
