"""usersProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usersApp import urls as userUrls
from followersApp import urls as followerUrls
from subscriptionsApp import urls as subscriptionUrls
from retweetsApp import urls as retweetUrls
from postsApp import urls as postsUrls
from likesApp import urls as likesUrls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', include(userUrls)),
    path('followers/', include(followerUrls)),
    path('subscriptions', include(subscriptionUrls)),
    path('posts/', include(postsUrls)),
    path('likes', include(likesUrls)),
    path('retweets/', include(retweetUrls)),
]
