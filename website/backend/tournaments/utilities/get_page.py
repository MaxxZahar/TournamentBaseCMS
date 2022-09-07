def get_page(pages, request):
    if request.GET.get('page', False):
        try:
            page_number = int(request.GET.get('page'))
            if page_number > len(pages) or page_number < 1:
                raise ValueError
        except ValueError:
            print('Wrong request')
        queryset = pages[page_number - 1]['data']
    else:
        queryset = pages[0]['data']
        page_number = 1
    return {
        'queryset': queryset,
        'page_number': page_number
    }
