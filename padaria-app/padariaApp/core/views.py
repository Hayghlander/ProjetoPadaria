from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import TemplateView
from .models import Produto, Categoria
from django.views.decorators.cache import cache_page

class HomeView(TemplateView):
    template_name = 'paginas/home.html' 


class ProductListView(generic.ListView):

    template_name = 'paginas/product_list.html'
    context_object_name = 'products'
    paginate_by = 3

    def get_queryset(self):
        queryset = Produto.objects.all()
        q = self.request.GET.get('q', '')
        if q:
            queryset = Produto.objects.filter(queryset, q)
        return queryset


product_list = ProductListView.as_view()

class CategoryListView(generic.ListView):

    template_name = 'paginas/category.html'
    context_object_name = 'product_list'
    paginate_by = 3

    def get_queryset(self):
        return Produto.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['current_category'] = get_object_or_404(Categoria, slug=self.kwargs['slug'])
        return context


category = CategoryListView.as_view()


@cache_page(60 * 10)
def product(request, slug):
    product = Produto.objects.get(slug=slug)
    context = {
        'product': product
    }
    return render(request, 'paginas/product.html', context)