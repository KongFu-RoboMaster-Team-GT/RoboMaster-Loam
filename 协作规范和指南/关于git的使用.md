# git & vscode的git插件使用 & 个人代码进度同步中央仓库

## 环境安装 
我们在此统一使用vscode作为我们的开发环境，并且使用vscode的图形化界面来使用git进行个人代码进度同步

1. 打开vscode, 在左侧侧边栏找到extension, 搜索Github Action, Github Pull Requests这两个插件安装。安装左侧侧边栏会多出两个图标，一个像串珠的，一个是github那只猫的，分别是github action 和 github pullrequest

在此说明本文涉及的术语 
图标对应关系：
左侧侧边栏长得像串珠的---github action
左侧侧边栏长得像github那只猫的---github pull request


2. vscode里面左侧侧边栏最下面倒数第二个人像的图标，点开他，在里面登陆你的github账户。
登陆成功后点击github pull request, 如果能看到:

\/ pull requests
    > Created by ME
    > All Open

差不多长这样的界面，说明环境建立已成功。


## 概念介绍 & 术语介绍

对应关系为： 
- 本文俗称 ： 概念及解释 
- 中央仓库：  在github上我们功夫组织名下的仓库, 所有的个人代码都提交到这里，这里存储着全部比赛用的代码
(https://github.com/KongFu-RoboMaster-Team-GT/RoboMaster-Loam/tree/main)

- `git clone` ： 把`中央仓库`的代码复制一份到你的电脑上，
- `本地仓库` : 执行`git clone` 后， 你把中央仓库代码下载到你电脑上的某个位置。我们称这个位置为你的`本地仓库`
- 



## 开发流程

1. 去中央仓库点击code copy url to clipboard ![如图所示](../photobed/gitcenterrepo.png)
点绿色的code然后点copy url to clipboard下面的那个按钮，把仓库地址复制到你的剪切板

2. 
