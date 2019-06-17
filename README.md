# No-select and select dropdown_menu_test
Test URL: http://www.imooc.com/ 
          http://www.baidu.com/
          http://demo.magentocommerce.com.com/
Select a drop-down menu for non-select method testing

<Elementpositioning_homepagetest.py>
 采用测试网址：http://demo.magentocommerce.com.com/
 定位搜索文本框，采用is_enabled()测试是否其是否可用
 定位到点击按钮，采用is_displayed() and is_enabled()测试其是否可见且可用
 定位accont和Finance功能，采用is_displayed() and is_enabled(0测试其是否可见 可用
 
 <test_function_options.py>--非select方法
 采用测试网址：http://www.imooc.com/
 启动Chrome()浏览器后
 打开测试网址
 一级定位：父元素
 二级定位：所有子元素
 采用assertEqual()断言判断获取的所有子元素个数
 将期望的子元素和获得所有的子元素使用assertEqual()对比
 
 <test_functions_options_of_select.py>--select方法
 采用测试网址：http://www.baidu.com/
 启动Chrome()浏览器且打开测试网址
 首先定位“设置” --> “搜索设置”-->click点击进去
 然后采用
 
    
