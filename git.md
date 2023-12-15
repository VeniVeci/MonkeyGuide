![image.png](./assets/1702622408638-image.png)




![image.png](./assets/1702622870336-image.png)



git pull origin dev

![image.png](./assets/1702623048950-image.png)



1.git branch 既可以使用--set-upstream又可以使用--set-upstream-to，但是前者已经被弃用

用法：git branch --set-upstream-to=origin/mybranch1 mybranch1

作用：追踪远程分支origin/mybranch1到本地分支mybranch1，如果远程没有mybranch1会报错，需要先创建远程分支

2.git push只可以使用--set-upstream，等价与使用 -u

用法：git push -u origin mybranch1

作用：

1.推送本地分支mybranch1到远程主机origin的mybranch1分支

2.追踪远程分支，远程没有mybranch1就自动创建一个

3.设置origin为默认主机



```
git push -f origin master
```


`git push -f origin master` 和 `git push -u origin master` 是两个不同的 Git 命令，它们的作用和影响也有所不同。

1. **`git push -f origin master`：**
   * `-f` 选项代表 force（强制），它会强制推送你的本地分支到远程仓库，即便它已经有了更新。
   * 这个命令会覆盖远程分支上的任何更改，所以要小心使用。一般而言，避免在与其他人协作的项目中使用 `-f`，因为它可能导致数据丢失或冲突。
2. **`git push -u origin master`：**
   * `-u` 选项通常与第一次推送到远程仓库的分支一起使用。它会将本地分支与远程分支关联起来，建立跟踪关系。
   * 当你使用 `-u` 选项时，Git 会记住推送的远程仓库和分支，并在以后的推送中默认使用这个远程仓库和分支。这有助于简化后续的推送命令。

综合起来，这两个命令的区别在于 `-f` 的使用和是否建立跟踪关系。如果你想强制推送并且不关心是否建立跟踪关系，可以使用 `git push -f origin master`。如果是第一次推送并且希望建立跟踪关系，可以使用 `git push -u origin master`。在大多数情况下，慎用 `-f` 以避免不必要的问题。
