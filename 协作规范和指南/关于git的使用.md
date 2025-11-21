# git & vscode的git插件使用 & 个人代码进度同步中央仓库

## 环境安装 
我们在此统一使用vscode作为我们的开发环境，并且使用vscode的图形化界面来使用git进行个人代码进度同步

1. 打开vscode, 在左侧侧边栏找到extension, 搜索Github Action, Github Pull Requests这两个插件安装。安装左侧侧边栏会多出两个图标，一个像串珠的，一个是github那只猫的，分别是github action 和 github pullrequest

插件图片及名字：![image](../photobed/extensions.png)


2. vscode里面左侧侧边栏最下面倒数第二个人像的图标，点开他，在里面登陆你的github账户。
登陆成功后点击github pull request, 如果能看到:

\/ pull requests
    > Created by ME
    > All Open

差不多长这样的界面，说明环境建立已成功。


## 概念介绍 & 术语介绍

对应关系为： 


| 本文称呼 | Git 概念 | 说明 |
|-----------|-----------|------|
| **中央仓库** | Remote Repository | 我们团队在 GitHub 上的主仓库，所有人最后的代码都要提交到这里。<br> 地址：[中央仓库（点击打开）](https://github.com/KongFu-RoboMaster-Team-GT/RoboMaster-Loam/tree/main) |
| **git clone** | Clone 仓库 | 把中央仓库完整复制一份到你的电脑上，建立你的“本地仓库”。 |
| **本地仓库** | Local Repository | 你电脑上这份仓库的副本，所有修改都先在这里进行。 |
| **分支（branch）** | Branch | 你的私人开发空间，不会影响主分支（main）。例如 `dev-lisi`。 |
| **提交（commit）** | Commit | 把你对文件的修改保存到本地仓库。 |
| **推送（push）** | Push | 把本地仓库的修改上传到 GitHub。 |
| **拉取请求（PR）** | Pull Request | 请求把你开发的分支合并到主仓库。需要审核后才会合并。 |




## 开发流程

1. 创建新分支进行开发， 详情见此视频：https://www.bilibili.com/video/BV1JHkQBEELu
2. 分支通过后如何同步本地与云端进度，以及继续在个人分支上进行开发：https://www.bilibili.com/video/BV1VXkDBMESG/

## 注意事项

- 没有必要每个commit都创建pr。
每次commit相当于保存进度，把commit想象成你按下ctrl+S保存，创建pr给想象成你对着百度网盘上传你保存过的文件。我们提倡在本地修改，创建多条commit然后再创建一条pr.
- 你可以创建多条pr, 但是我们推荐如果你的一条pr还没有被合并前，最好不要创建第二条pr.等到第一条pr被合并后，再创建第二条pr.
- 在创建一条开发分支之后，我们建议以后你都使用这条分支进行开发。也就是说，你创建分支这个事情只需要做一次。进行开发前，请千万确保你处于你自己的分支上（可在vscode左下角查看你当前所在分支, 图片中main就是意味着你在main分支，其他名字则意味着你在对应名字的分支）。
![image](../photobed/branch.png)