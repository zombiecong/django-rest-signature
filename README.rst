**django-rest-signature是一个基于Django REST Framework的多站点签名验证组件。**

简介
---------

安装本组件后，可以在组件的数据库中设置多组客户端的信息，并为每组客户端指定一对site-api-id和site-api-secret。

访问RESTful API时，客户端需要以特定方式在HTTP Request Header中发送一组约定好的site-api-id以及经过site-api-secret加密的签名。

如果以上Header信息无法通过验证，则拒绝访问任何API。

如果以上Header信息可以通过验证，则可以在Django REST Framework的view中访问新增的request.site对象来获取site-api-id所对应的站点信息。

|

Requirements 
----------------
* python(3.4)
* Django(1.8)
* Django REST Framework (3.1.0)
* PyJWT

|

安装
----------------

Install using pip

.. code-block:: bash

 $ pip install django-rest-signature

|

设置
----------

**在Settings.py文件中：**

在INSTALLED_APPS 中增加 **'rest_signature'**.

.. code-block:: python

 INSTALLED_APPS = (
     ....
     'rest_signature',
 )

|

在MIDDLEWARE_CLASSES 中 AuthenticationMiddleware之前增加 **'rest_signature.middleware.SignatureMiddleware'**

.. code-block:: python

 MIDDLEWARE_CLASSES = (
     ...
     'rest_signature.middleware.SignatureMiddleware', 
     'django.contrib.auth.middleware.AuthenticationMiddleware',
     ...
 )
 
|

客户端发送Request方法
---------------------------------

通过已有的sid，时间戳，key和算法进行加密 `--详见jwt <https://github.com/kjur/jsjws>`_，加密结果通过header增加signature参数传递。


|


Django REST Framework 端用法
------------------------------

在Django REST Framework的view中访问新增的request.site对象来获取site-api-id所对应的站点信息。

|

Issue
------

1. 本组件尚处测试期间，请勿用于生产
2. 未处理GET和非GET请求




 