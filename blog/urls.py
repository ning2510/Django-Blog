from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    # django 会从用户访问的 URL 中自动提取 URL 路径参数转换器 <type:name> 规则捕获的值，然后传递给其对应的视图函数。
    path('', views.IndexView.as_view(), name='index'),
    # 文章页面
    path('posts/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    # 归档页面
    path('archives/<int:year>/<int:month>/', views.ArchiveView.as_view(), name='archive'),
    # 分类页面
    path('categories/<int:pk>/', views.CategoryView.as_view(), name='category'),
    # 标签页面
    path('tags/<int:pk>/', views.TagView.as_view(), name='tag'),
]