from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_size= 5   # each page have 5 records
    page_query_param= 'lovepage' # this is used to change the url variable. Default variable is `page`.
    max_page_size = 7 # this indicates the maximum page size 
    last_page_strings = 'end' # last page strings is used to watch the last page and default string is `last`, but i have change it to `end`