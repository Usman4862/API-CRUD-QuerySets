from rest_framework.pagination import CursorPagination

"""
CursorPagination:
    It is used for `Previous` & `Next` pagination. 
"""


class MyPagination(CursorPagination):
    page_size = 5
    ordering = 'id'
    cursor_query_param = 'usman' # default cursor query param is `cursor`, i have used it as usman

