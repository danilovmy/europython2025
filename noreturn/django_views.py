from django.views.generic import DetailView
from django.utils.timezone import now

class Article:
    pass

class ArticleDetailResponse(DetailView.response_class):

    def __init__(self, *args, context=None, **kwargs):
        context["now"] = now()
        return super().init(*args, context=context, **kwargs)

class ArticleDetailView(DetailView):
    model = Article
    response_class = ArticleDetailResponse
