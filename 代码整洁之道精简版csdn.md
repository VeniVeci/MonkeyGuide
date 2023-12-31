﻿《代码整洁之道：程序员的职业素养》摘抄

# 1 专业主义（开发人员应该怎么保证代码质量）

专业人士，就是能对自己犯下的错误负责的人，哪怕那些错误实际上在所难免。所以，雄心勃勃的专业人士们，你们要练习的第一件事就是“道歉”。道歉是必要的，但还不够。你不能一而再、再而三地犯相同的错误。职业经验多了之后，你的失误率应该快速减少，甚至渐近于零。**失误率永远不可能等于零，但你有责任让它无限接近零。**

发布软件时，你应该确保QA（QA：Quality Assurance (质量保证)）找不出任何问题。故意发送明知有缺陷的代码，这种做法是极其不专业的。什么样的代码是有缺陷的呢？那些你没把握的代码都是！有些家伙会把QA当作啄木鸟看待。他们把自己没有全盘检查过的代码发送过去，想等QA找出bug再反馈回来。

QA：Quality Assurance (质量保证)

QC：Quality Control (质量控制)

QM：Quality Manage (质量管理)

我是开源项目FitNesse的主要贡献者和代码提交者。在写作本书的时候，FitNesse的代码有6万多行。**在这6万行代码中有2000多个单元测试，超过2.6万行。43%的代码都是测试代码**。Emma的报告显示，这2000多个测试对代码的覆盖率约为90%。为什么只有90%呢？因为Emma会忽略一些执行的代码。我确信实际的覆盖率会比90%高许多。能达到100%吗？不，达不到，100%只是个理想值。但是有些代码不是很难测试吗？是的，但之所以很难测试，是因为设计时就没考虑如何测试。唯一的解决办法就是要设计易于测试的代码，**最好是先写测试，再写要测的代码**。

但是有些代码不是很难测试吗？是的，但之所以很难测试，是因为设计时就没考虑如何测试。唯一的解决办法就是要设计易于测试的代码，最好是先写测试，再写要测的代码。这一方法叫做测试驱动开发（TDD）

# 2 如何让代码质量逐步提高

每次通读代码的时候，也可以不时调整一下结构。**这一策略有时也叫“无情重构”，我把它叫作“童子军训练守则”：**对每个模块，每检入一次代码，就要让它比上次检出时变得更为简洁。每次读代码，都别忘了进行点滴的改善。这完全与大多数人对软件的理解相反。他们认为对上线运行的软件不断地做修改是危险的。**错！让软件保持固定不变才是危险的！如果一直不重构代码，等到最后不得不重构时，你就会发现代码已经“僵化了”。**

为什么大多数开发人员不敢不断修改他的代码呢？因为他们害怕会改坏代码！

为什么会有这样的担心呢？

**因为他们没做过测试。话题又回到测试上来了**。如果你有一套覆盖了全部代码的自动化测试，如果那套测试可以随时快速执行，那么你根本不会害怕修改代码。

# 3 保持手感，练习kata

卡塔的形式往往是一个有待解决的简单编程问题，比如编写计算拆分某个整数的素数因子等。练卡塔的目的不是找出解决方法（你已经知道方法了），**而是训练你的手指和大脑**。每天我都会练一两个卡塔，时间往往安排在正式投入工作之前。我可能会选用Java、Ruby、Clojure或其他我希望保持纯熟的语言来练习。我会用卡塔来培养某种专门的技能，**比如让我的手指习惯点击快捷键或习惯使用某些重构技法等**。不妨早晚都来个10分钟的卡塔吧，把它当作热身练习或者静心过程。

# 4 提升开发效率和代码质量的技巧：测试先行（测试驱动开发）

**“测试驱动开发”（TDD）自在行业中首次亮相**，至今已经有十余年了。它最早是极限编程（XP）运动的一部分，但此后已经被Scrum和几乎所有其他敏捷方法所采纳。即使是非敏捷的团队也在实践TDD。

Kent和我坐在他的办公室里，使用Java语言解决一些小问题。我一上来就只想马上写能够解决这个小问题的代码。但是Kent不让我这么做，而是带着我一步步体验了TDD的整个过程。首先，他写了一个单元测试的一小部分，没几行代码。然后，他写了刚好能使那个测试编译通过的代码。接着，他又写了些测试，然后再写一些代码。从编码到运行的周期如此之短完全超出了我的想象。我以前都是先花上大半个小时写代码，然后才去编译或运行。而Kent居然每30秒左右就会运行一次程序。这让我目瞪口呆！

与Kent交流后我领悟到：TDD绝不仅仅是一种用于缩短编码周期的简单技巧。我会在下文中详述TDD的诸多优势。

## TDD的三项法则

（1）在编好单元测试之前，不要编写任何产品代码。

（2）只要有一个单元测试失败了，就不要再写测试代码；无法通过编译也是一种失败情况。

（3）产品代码恰好能够让当前失败的单元测试成功通过即可，不要多写。

遵循这三项法则的话，大概30秒钟就要运行一次代码。先写好一个单元测试的一小部分代码，很快，你会发现还缺少一些类或函数，所以单元测试无法编译。因此必须编写产品代码，让这些测试能够编译成功。产品代码够用即可，然后再回头接着写单元测试代码。

**这个循环不断反复。写一些测试代码，然后再写一些产品代码。这两套代码同步增长，互为补充。测试代码之匹配于产品代码，就如抗体之匹配于抗原一样**。

## 好的设计

当你遵循三项法则并且做到了测试先行时，还会感到进退维谷。通常情况下，你对于想要写的代码十分清楚，但是三项法则却要求你先写出目前无法通过的单元测试，因为要测试的代码尚未诞生！这意味着必须测试将要编写的代码。测试代码的一个问题是必须隔离出待测试的代码。如果一个函数调用了其他函数，单独测试它通常会比较困难。为了编写测试，你必须找出将这个函数和其他函数解耦的办法。

换言之，**测试先行的需要，会迫使你去考虑什么是好的设计**。如果不先写测试，就有可能出现各个函数耦合在一起最终变成无法测试的一大团的问题。如果后面再写测试，你也许能够测试整个大块的输入和输出，但是很难测试单个函数。

“但是我可以稍后再写测试啊。”你也许会这样说。不，不可能。实际上也不是绝对不可以，没错，你是能够稍后写些测试。如果很仔细地来看，也许后写测试还可以达到较高的覆盖率。**但是事后写的测试只是一种防守。而先行编写的测试则是进攻，事后编写测试的作者已经受制于已有代码，他已经知道问题是如何解决的。**

**与采用测试先行的方式编写的测试代码比起来，后写的测试在深度和捕获错误的灵敏度方面要逊色很多。**

# 5 为什么产品经理的想法总是在变化

**原因是观察者效应**

做业务的人和写程序的人都容易陷入一个陷阱，即过早进行精细化。业务方还没有启动项目，就要精确知道最后能得到什么；开发方还没有评估整个项目，就希望精确知道要交付什么。双方都贪求不现实的精确性，而且经常愿意花大价钱来追求这种精确。

不确定原则问题在于，东西画在纸上与真正做出来，是不一样的。

业务方看到真正的运行情况时就会意识到，自己想要的根本不是这样的。一看到已经满足的需求，关于到底要什么，他们就会冒出更好的想法——通常并不是他们当时看到的样子。

在工作中，**有一种现象叫观察者效应，或者不确定原则。每次你向业务方展示一项功能，他们就获得了比之前更多的信息，这些新信息反过来又会影响他们对整个系统的看法**。最终结果就是，需求完成得越精细，就越容易被忽视，系统因此也谈不上完工。

# 6 验收测试和单元测试的区别

**验收测试不是单元测试**。

单元测试是程序员写给程序员的，它是正式的设计文档，描述了底层结构及代码的行为。关心单元测试结果的是程序员而不是业务人员。

验收测试是业务方写给业务方的（虽然可能最后是身为开发者的你来写）。它们是正式的需求文档，描述了业务方认为系统应该如何运行。关心验收测试结果的是业务方和程序员。有人认为区分两种测试是多此一举，所以要消灭“重复劳动”。

尽管单元测试和验收测试的对象通常是相同的，但绝对谈不上“重复”。首先，尽管两者测试的可能是同一个对象，其机制和路径却是不同的。
**单元测试是深入系统内部进行，调用特定类的方法；验收测试则是在系统外部，通常是在API或者是UI级别进行。所以两者的执行路径是截然不同的**。不过，这两种测试并不重复的根本理由在于，它们的主要功能其实不是测试，测试只是它们的附属职能。单元测试和验收测试首先是文档，然后才是测试。它们的主要目的是如实描述系统的设计、结构、行为。它们当然可以验证设计、结构、行为是否达到了具体指标，**但是，它们的真正价值不在测试上，而在具体指标上**。
