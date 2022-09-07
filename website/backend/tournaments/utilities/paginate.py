def paginate(queryset, paginate_by):
    total = len(queryset)
    pages = []
    i = 0
    j = 0
    data = []
    page = {}
    number = 1
    for item in queryset:
        data.append(item)
        i += 1
        j += 1
        if i == paginate_by:
            i = 0
            page['data'] = data
            page['number'] = number
            number += 1
            pages.append(page)
            page = {}
            data = []
        elif j == total:
            page['data'] = data
            page['number'] = number
            pages.append(page)
    return pages
