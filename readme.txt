这个小项目的环境：
Windows 10: x64
python version: 3.6.4
pycharm version: community 2017.3.3
mysql version: 5.7
-----------------------------------------
在mysql里创建article_web数据库，然后用pycharm打开此项目，接着进入虚拟环境。你需要运行models.py来创建表，如果models.py没有db.create_all()，
那么请加上:
if __name__ == '__main__':
    db.create_all()
  
 然后在虚拟环境中运行，在命令行里为:python models.py
 接着便可运行views.py文件，以便打开web服务器。
 如果你需要将项目移植到其他环境，用其他IDE打开的话，依赖包导出方法为：
 pip freeze > requiredments.txt
 在其他环境安装依赖包：
 pip install -r requiredments.txt
 
 里面的manager.py其实是一个配置文件，之前在views.py里面初始化app和配置app，导致models.py不能导入app，views.py也不能导入db,如果在models.py里面再
 定义一个app,那么两者的配置就会不一致，会出现一些配置的错误，比如程序找不到'SQLALCHEMY_TRACK_MODIFICATIONS'配置。
 所以建议app在一个地方初始化和配置，然后其他文件从这个地方引入app,就不会发生循环导入。
 
 关于验证登录装饰器：
 这里没用flask-login扩展，是因为自己动手写装饰器可以更好地理解装饰器，它的奇妙之处。
 
 关于视图函数请求的处理的建议是，将处理GET请求的代码放在处理POST请求的代码的后面，这样会避免POST表单时，修改后的数据被原来的数据所覆盖，导致修改失败
 （除非明确指明哪些是处理GET和POST请求的代码）
 
 关于前端，富文本编辑器是UEditer,框架是bootstrap。使用UEditer时注意引入js文件的顺序，以及相关的JS代码定义，详情请参考art_add.html。
 boostrap为4.0版本，还有一个holder.js文件，作用是生成图片占位符。
