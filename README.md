# No-select and select dropdown_menu_test
Test URL: http://www.imooc.com/ 
          http://www.baidu.com/
          http://demo.magentocommerce.com.com/
Select a drop-down menu for non-select method testing

<Elementpositioning_homepagetest.py>--页面按钮、功能以及文本框永健和可用测试
 采用测试网址：http://demo.magentocommerce.com.com/
 定位搜索文本框，采用is_enabled()测试是否其是否可用
 定位到点击按钮，采用is_displayed() and is_enabled()测试其是否可见且可用
 定位accont和Finance功能，采用is_displayed() and is_enabled(0测试其是否可见且可用。
 
 <test_function_options.py>--非select方法下拉菜单测试
 采用测试网址：http://www.imooc.com/
 启动Chrome()浏览器后
 打开测试网址
 一级定位：父元素
 二级定位：所有子元素
 采用assertEqual()断言判断获取的所有子元素个数
 将期望的子元素和获得所有的子元素使用assertEqual()对比。
 
 <test_functions_options_of_select.py>--select方法下拉菜单测试
 采用测试网址：http://www.baidu.com/
 启动Chrome()浏览器且打开测试网址
 首先定位“设置” --> “搜索设置”-->click点击进去
 然后采用slect方法选择“每页显示条数”的下拉框，测试是否有三个子选项，且通过索引的方式选择第二个选项。
 
 <test_function_options_gethtml.py>--下拉菜单测试
 通过BeautifulSoup方法获取目的地址的页面内容
 然后使用正则匹配通过div和s标签以及class name='tag-box l'获取对应的页面元素，进行定位，使用一个简单的循环将获取的元素打印出来，将实际的测试的结果和期望的结果对比。
   
<Login_test.py>--登录测试
测试网址：https://www.imooc.com/
启动浏览器进入测试网址后，定位到“登录”按钮并点击进入，然后分别定位文账号、密码文本框，然后通过send_keys()输入用来测试的账号和密码，完成测试。

<searchproducts.py>--关键词搜索以及全部搜索信息的获取
测试网址：http://demo.magentocommerce.com.com/
该测试用例用于测试在搜索框内输入一个关键词，然后获取搜索的全部关联信息的数目，与期望数目值进行比对，完成测试。
