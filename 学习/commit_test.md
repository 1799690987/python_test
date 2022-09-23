### 查看log 
git log

### 合并前三次
git rebase -i HEAD~3
![img_9.png](img_9.png)

### 保留3
pick：保留该commit
squash：将该commit和前一个commit合并
故如果我们想要将此3次提价合并成一个提交，需要将commit2和commit3的pick改成squnsh(缩写“s”)也可。如下图：
![img_10.png](img_10.png)

### 编辑提交信息。wq保存退出
![img_11.png](img_11.png)

###  再次查看记录（命令：git log）
![img_12.png](img_12.png)

### 强制推送到远程（命令：git push -f） ；没有与远端建立连接 所以需要执行 git push -f --set-upstream origin gongneng 

