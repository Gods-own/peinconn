from flask import url_for

def get_pagination(endpoint, dbquery, **kwargs):
    try:
        links = {
            'firstPage': url_for(endpoint, **kwargs, page=dbquery.first, per_page=dbquery.per_page),
            'lastPage': url_for(endpoint, **kwargs, page=dbquery.last, per_page=dbquery.per_page),
            'prevPage': url_for(endpoint, **kwargs, page=dbquery.prev_num, per_page=dbquery.per_page),
            'nextPage': url_for(endpoint, **kwargs, page=dbquery.next_num, per_page=dbquery.per_page),
            'meta': {
                'paging': {
                'pageCount': dbquery.per_page,
                'totalPages': dbquery.pages,
                'totalItems': dbquery.total,
                'page': dbquery.page,
                'prev_page_num': dbquery.prev_num,
                'next_page_num': dbquery.next_num,
                'hasPrevPage': dbquery.has_prev,
                'hasNextPage': dbquery.has_next,
                }
            }
        }

        return links
    except Exception as e:
        return None    