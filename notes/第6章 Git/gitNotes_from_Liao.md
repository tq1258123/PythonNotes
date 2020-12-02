#  Git笔记 

>这篇笔记内容主要来自网上廖雪峰的笔记，中间会根据`git`书籍和教学视频进行修改。

---

## Git介绍
- Git是分布式版本控制系统，在版本控制时分为三个区域，即工作区，暂存区和版本库。工作区是修改项目文件；修改后把文件提交到暂存区；最后再提交到版本库里。暂存区主要是对版本变动的哈希值进行记录。

- 区域说明 -- 工作区：在电脑里能看到的目录；版本库：在工作区有一个隐藏目录`.git`，是`Git`的版本库。`Git`的版本库中存了很多东西，其中最重要的就是称为`stage`（或者称为`index`）的暂存区，还有`Git`自动创建的`master`，以及指向`master`的指针`HEAD`。

  进一步解释一些命令：

  - `git add`实际上是把文件添加到暂存区
  - `git commit`实际上是把暂存区的所有内容提交到当前分支

- 集中式`VS`分布式，`SVN VS Git`
  1. `SVN`和`Git`主要的区别在于历史版本维护的位置
  2. `Git`本地仓库包含代码库还有历史库，在本地的环境开发就可以记录历史，而`SVN`的历史库存在于中央仓库，每次对比与提交代码都必须连接到中央仓库才能进行。
  3. 这样的好处在于：
     - 自己可以在脱机环境查看开发的版本历史。
     - 多人开发时如果充当中央仓库的`Git`仓库挂了，可以随时创建一个新的中央仓库然后同步就立刻恢复了中央库。
## Git安装

`git --version`当安装后输入这个命令显示`git`版本后，说明已经安装好了。

## Git配置

```bash
# 配置姓名，邮箱
$ git config --global user.name "Your Name"
$ git config --global user.email "email@example.com"
$ git config --list
# 配置代码别名
$ git config --global alias.新名称 "log -- oneline --decorate --graph --all"
```
`git config`命令的`--global`参数，表明这台机器上的所有`Git`仓库都会使用这个配置，也可以对某个仓库指定不同的用户名和邮箱地址。`--list`参数可以用来查看配置信息，用来检查之前配置的信息是否真的配置好了。

## Git具体命令应用
### 初始化一个Git仓库
```bash
$ git init
```
初始化后会得到一个`.git`的文件夹，文件具体内容说明：

`hooks`：（钩子）存放一些`shell`脚本；`info`目录下有个文件`exclude`，它存放一些仓库的信息`logs`：保存所有更新的引用记录；`objects`：存放所有的`git`对象；`refs`：目录下有`heads`和`tags`两个目录，`heads`存放最新一次提交的哈希值；`COMMIT_EDITMSG`：最新提交的一次提交注释（`git commit -m “……”`。即`commit`提交时引号里的注释），`git`系统不会用到，给用户一个参考
`description`：仓库的描述信息，主要给`gitweb`等`git`托管系统使用；`config`：`git`仓库的配置文件；`index`：暂存区（`stage`），一个二进制文件；`ORIG_HEAD`：`HEAD`指针的上次所在的位置的记录，也记录的一个哈希值；`HEAD`：记录了一个路径，映射到`ref`引用，能够找到下一次`commit`的前一次哈希值。`commit_id`是版本号，是一个用`SHA1`计算出的序列。

### Git仓库的增删改查

#### Git仓库添加文件

```bash
# 提交到暂存区
$ git add <file>
$ git add ./ | git add # 添加所有修改过的文件
	# 底层命令
	git hash-object -w 文件名
	git update-index    
# 提交到版本库
$ git commit -m "description"
	git write-tree
	git commit-tree
# 跳过添加到暂存过程，已跟踪的文件才能使用
$ git commit -a -m "description"
```
`git add`可以反复多次使用，添加多个文件，`git commit`可以一次提交很多文件，`-m`后面输入的是本次提交的说明，可以输入任意内容。

#### Git仓库删除文件和撤销修改

```bash
$ git rm <file>
# 相当于执行下面两条命令
$ rm <file>
$ git add <file>
```

**进一步的解释**

Q：比如执行了`rm text.txt` 误删了怎么恢复？
A：执行`git checkout text.txt` 把版本库的东西重新写回工作区就行了
Q：如果执行了`git rm text.txt`我们会发现工作区的`text.txt`也删除了，怎么恢复？
A：先撤销暂存区修改，重新放回工作区，然后再从版本库写回到工作区

```bash
$ git reset
$ git checkout text.txt
```

Q：如果真的想从版本库里面删除文件怎么做？
A：执行`git commit -m "delete text.txt"`，删除文件后再进行`add - commit`提交，将不包含这个文件

#### Git仓库查看
```bash
# 查看工作区状态
$ git status
```
状态分为已跟踪和未跟踪。已跟踪又分为已修改，已暂存和已提交三种。

```bash
# 查看修改内容
$ git diff
$ git diff --cached
$ git diff --staged
$ git diff HEAD -- <file>
```
- `git diff` 可以查看工作区(`work dict`)和暂存区(`stage`)的区别
- `git diff --cached` 可以查看暂存区(`stage`)和分支(`master`)/版本库的区别
- `git diff HEAD -- <file>` 可以查看工作区和版本库里面最新版本的区别
```bash
# 查看提交日志
$ git log
# 简化日志输出信息
$ git log --pretty=oneline
# 查看命令历史
$ git reflog
```

### 分支

切换分之前，需要对分支里的内容`commit`，不然可能会污染到其他分支。

```bash
# 创建分支
$ git branch <branchname>
# 查看分支
$ git branch
# 切换分支
$ git checkout <branchname>
# 创建+切换分支
$ git checkout -b <branchname>
# 合并某分支到当前分支，要在主分支上操作
$ git merge <branchname>
# 删除分支
$ git branch -d <branchname> # 合并分支后可以使用这个命令删除不需要的分支
$ git branch -D <branchname> # 强制删除
# 查看分支合并图
$ git log --graph
# 普通模式合并分支
$ git merge --no-ff -m "description" <branchname>
```

`git branch`命令会列出所有分支，当前分支前面会标一个`*`号。

当`Git`无法自动合并分支时，就必须首先解决冲突。解决冲突后，再提交，合并完成。用`git log --graph`命令可以看到分支合并图。

因为本次合并要创建一个新的commit，所以加上`-m`参数，把commit描述写进去。合并分支时，加上`--no-ff`参数就可以用普通模式合并，能看出来曾经做过合并，包含作者和时间戳等信息，而fast forward合并就看不出来曾经做过合并。

合并分支产生冲突后，在冲突的文件上修改再提交。

### Git存储

有时，当你在姓名的一部分上已经工作一段时间后，所有东西都已进入混乱状态，而这时你要切换到另一个分支做一点别的事情，问题是你不想仅仅因为过会回到这一点而而为你做了一半的工作进行提交，这时可以用`stash`命令保存工作现场。这个保存不会出现在`log`日志里。

```bash
# 保存工作现场
$ git stash
# 查看工作现场
$ git stash list
# 恢复工作现场
$ git stash pop
```

撤销和重置



### 版本回退

```bash
# 回退到上一版本
$ git reset --hard HEAD^
# 回退指定版本号
$ git reset --hard commit_id
```
以上命令是返回上一个版本，在`Git`中，用`HEAD`表示当前版本，上一个版本就是`HEAD^`，上上一个版本是`HEAD^^`，往上100个版本写成`HEAD~100`。
### 远程仓库
#### 创建SSH Key
```bash
$ ssh-keygen -t rsa -C "youremail@example.com"
```
#### 关联远程仓库
```bash
$ git remote add origin https://github.com/username/repositoryname.git
```
#### 推送到远程仓库
```bash
$ git push -u origin master
```
`-u` 表示第一次推送master分支的所有内容，此后，每次本地提交后，只要有必要，就可以使用命令`git push origin master`推送最新修改。

#### 从远程克隆
```bash
$ git clone https://github.com/usern/repositoryname.git
```

#### 查看远程库信息
```bash
$ git remote -v
```

#### 在本地创建和远程分支对应的分支
```bash
$ git checkout -b branch-name origin/branch-name，
```
本地和远程分支的名称最好一致；

#### 建立本地分支和远程分支的关联
```bash
$ git branch --set-upstream branch-name origin/branch-name；
```
#### 从本地推送分支
```bash
$ git push origin branch-name
```
如果推送失败，先用git pull抓取远程的新提交；
#### 从远程抓取分支
```bash
$ git pull
```
如果有冲突，要先处理冲突。

### 标签
tag就是一个让人容易记住的有意义的名字，它跟某个commit绑在一起。
#### 新建一个标签
```bash
$ git tag <tagname>
```
命令`git tag <tagname>`用于新建一个标签，默认为HEAD，也可以指定一个commit id。
#### 指定标签信息
```bash
$ git tag -a <tagname> -m <description> <branchname> or commit_id
```
`git tag -a <tagname> -m "blablabla..."`可以指定标签信息。
#### PGP签名标签
```bash
$ git tag -s <tagname> -m <description> <branchname> or commit_id
```
`git tag -s <tagname> -m "blablabla..."`可以用PGP签名标签。
#### 查看所有标签
```bash
$ git tag
```
#### 推送一个本地标签
```bash
$ git push origin <tagname>
```
#### 推送全部未推送过的本地标签
```bash
$ git push origin --tags
```
#### 删除一个本地标签
```bash
$ git tag -d <tagname>
```
#### 删除一个远程标签
```bash
$ git push origin :refs/tags/<tagname>
```

