# 1_littelbook
数据来自http://www.literaturepage.com/
## day1
初始化结构：
- 目录toc
- 阅读器reader

编写爬虫
## day2
主要编写toc的点击响应，点击则在reader中显示相应文段内容

目前问题：
1. 点击标题时，无法正确取出章节标题，导致无法显示内容

## day3 11/20
- 昨天的问题已经全部解决
- 实现了递归的subtoc
- 维护了subtoc的代码，只有最深层的标题能响应点击，在reader中显示出内容

问题：
当阅读完一个大Chapter后，再点击箭头翻页，无法跨越大Chapter寻页
解决思路：每个大Chapter，即chapter: { chp1: [], chp2 : []} 的结构需要有一个唯一标识符，才能识别它的前后sibiling。顶层目录拥有整个结构，可能可以找到，但多层结构可能难以decide到底是在哪一层寻找。。。

添加目标功能：

- 调整视觉
  - 字体大小
  - 背景颜色
  - 方案化切换

- 寻找大chapter未实现_(:зゝ∠)_

## Day4 11/21
progress:
- 成功实现跨越大chapter的切换！！😃
添加简单路由

新目标功能：
- 允许同时阅读多个book，保持多个reader（也许可以设个上限）
- 后端服务器，使得booklist页面能够发出请求取回数据
---

目标功能：
- 切换book
- 调整视觉
  - 调整的元素：
   - 字体大小
   - 背景颜色
   - 方案化切换
  - 调整方法
   - 点击大标题toggle？

  [-] 允许同时阅读多个book，保持多个reader（也许可以设个上限）
  - 后端服务器，使得booklist页面能够发出请求取回数据

Keep Going!
