from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
                       url(r'', include('bookstore.books.urls')),
                       )


from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns += staticfiles_urlpatterns()
