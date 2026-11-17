# My-Python-Learning-Journey
My Python learning assignments.

## 项目简介
本项目是我的 Python 语言课程学习仓库，用于记录本学期的编程练习与作业。目前包含两个基础程序，分别解决逻辑运算和循环控制的问题，旨在巩固 Python 基础语法。

## 文件说明
- `bmi.py`：BMI 指数计算器，根据输入的身高和体重计算 BMI，并判断体型分类。
- `snake.py`：简易贪吃蛇逻辑演示，通过循环模拟蛇吃食物变长，输入 q 退出。

## 代码说明
本项目包含两个核心程序。第一个是 BMI 计算器，程序使用 `if-elif-else` 进行区间划分，并使用 `try-except` 处理用户输入异常；第二个是简易贪吃蛇，使用 `while` 循环不断读取用户输入，按回车增加长度，输入 q 退出。核心代码如下：

```python
# bmi.py 核心代码
def get_bmi_category(bmi):
    if bmi < 18.5: return "偏瘦"
    elif bmi < 24: return "正常"
    elif bmi < 28: return "超重"
    else: return "肥胖"

# snake.py 核心代码
while True:
    action = input("按回车前进(输入 q 退出): ")
    if action == 'q': break
    snake_length += 1
```
## 学习心得与规划
浏览 GitHub 优秀项目后，我意识到规范的文档对展示技能至关重要。本次任务让我学会了用 Markdown 排版，懂得了不仅要写好代码，还要用文档“包装”代码。我计划将未来的数据分析代码持续上传到该仓库，通过清晰的提交说明和 README 更新，打造个人的编程成长记录本。
