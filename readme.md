# 日志分析说明
## 安装 \& 卸载
### 安装
直接使用pip安装即可，安装完后会在系统内注册命令 log_analyzer 。
```
pip install dist/log_analyzer-1.2.1.tar.gz
```
### 卸载

```
pip uninstall log_analyzer
```
## 使用前

请在运行命令行程序前在当前目录下配置 config.ini ，这样对于不同的日志格式可以分目录分配置解析，
配置完后即可输入 log_analyzer 启动。

## 使用

以下命令都有自动补全和语法高亮。

* search 

    
    用来搜索任意关键字都行，直接搜索全文异步加载。

    ```
    >>> search CREATE,ISDIR
    ```
* help
	
	获取全部的操作说明或者单个函数的操作说明

	```
    >>> help function -> how to use function
	>>> help -> all the instruction desplayed
	```
* exit \\ quit \\ 直接回车
	
	退出命令行操作
	
* clear
	
	清空屏幕
	
* set \& get 操作
    
    如下文所示

## 配置
### regex \& labels
1. 由于需要灵活应对日志格式，所以需要事先配置日志格式所对应的正则表达式和标签。
2. 程序在命令行运行时可以通过 setregex 以及 setlabels 命令来修改当前环境的 regex 和 labels。
3. 程序在命令行运行时可以通过 getregex 以及 getlabels 命令来获取当前环境的 regex 和 labels。

### path
需要在 config.ini 中制定将要分析的 log 的路径，或者在命令行中直接输入 log 路径即可切换路径。
log 在输入时有自动补全功能，方便用户选择。
    
```
>>> ../../test.log
>>> set log path: ../../test.log
```
