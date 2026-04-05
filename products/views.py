from django.shortcuts import render

from .models import Product, Category, Tag


def product_list(request):

    #grab all products from the database
    products = Product.objects.all()

    #GET request to  grab search value or empty (repeat for catergory/tags)
    search_query = request.GET.get('search', '')
    category_id =  request.GET.get('category', '')
    tag_ids = request.GET.getlist('tags') # made getlist to grab all tags with multiple vals

    if search_query:
        #run if isn't empty, narrow the list ot find matching items case insenstitive
        products = products.filter(description__icontains=search_query)
    if category_id:
        #on products where id matches
        products = products.filter(category_id=category_id)
    if tag_ids:
        #remove dupes finds tag in particular list of ids
        products = products.filter(tags__in=tag_ids).distinct()

    #filter dropdowns
    categories = Category.objects.all()
    tags = Tag.objects.all()

    #filter dropdowns
    context = {
        'products': products,
        'categories': categories,
        'tags': tags,
        'search_query': search_query,
        'selected_category': category_id,
        'selected_tags': tag_ids,
    }

    # fill the template with context data, have path to our template
    return render(request, 'products/product_list.html', context)


