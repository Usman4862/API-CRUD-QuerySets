from rest_framework.pagination import LimitOffsetPagination

"""
LimitOffsetPagination:
    Limit means the exact limit that we apply how many records will show in each page.
    Offset means from where we need to start record in that pagination for each page.
    `` http://127.0.0.1:8000/api/mobile/list/?limit=5&offset=10 `` this is how we use it in urls
"""


class MyPagination(LimitOffsetPagination):
    default_limit = 6
    limit_query_param = 'mylimit' # default value of limit query param is `limit`, we can change it as we want.. 
    offset_query_param = 'myoffset' # same as above
    max_limit = default_limit # this is the max limit of the records that will show on each page.


