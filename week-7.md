# 学习笔记
## Linux
查看目录 ls
进入目录 cd
新建目录 mkdir
快捷操作：
输入 `cd ..` 可以回到上一级目录，类似 Windows 的「向上」。

```bash
cd ..
```

`cd -` 表示回到上一次所在的目录，类似 Windows 的「后退」。

```bash
cd -
```

`cd ~` 表示回到当前用户的主目录，类似 Windows 的「回到桌面」。

```bash
cd ~
```
`cd /` 表示进入根目录。

```bash
cd /
```
使用 `touch` 命令新建文件或目录
使用 `cp` 命令（Copy）复制文件到指定目录下
使用 `rm` 命令删除文件
使用 `mv` 命令可以移动文件或目录。
使用 `cat` 命令可以查看文件。
### 编辑
Sublime Text ，vim，gedit……
## Git
### 建立一个仓库
使用您当前目录作为Git仓库，我们只需使它初始化。
`git init`
### 添加新文件
`git add filename`
### 提交版本
现在我们已经添加了这些文件，我们希望它们能够真正被保存在Git仓库。
为此，我们将它们提交到仓库。
`git commit -m "Adding files"`
如果您不使用-m，会出现编辑器来让你写自己的注释信息。
当我们修改了很多文件，而不想每一个都add，想commit自动来提交本地修改，我们可以使用-a标识。
`git commit -a -m "Changed some files"`
git commit 命令的-a选项可将所有被修改或者已删除的且已经被git管理的文档提交到仓库中。
==千万注意，-a不会造成新文件被提交，只能修改。==
### 发布版本
我们先从服务器克隆一个库并上传。
`git clone ssh://example.com/~/www/project.git`
现在我们修改之后可以进行推送到服务器。
`git push ssh://example.com/~/www/project.git`
