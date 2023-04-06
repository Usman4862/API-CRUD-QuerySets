from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.filters import SearchFilter

class MovieView(generics.ListAPIView):
    queryset = SampleModel.objects.all()
    serializer_class = SampleModelSerializer
    # filter backends is used for the django filter backend
    filter_backends = [SearchFilter]
    # use your desired fields for filtering 
    search_fields = [
        '^movie', # this `^`, indicated istartwith in the search filter
        '=series',
    ]

    """
    `|`: The `|` symbol is used for ORing multiple search terms.
      For example, if you want to search for books whose title contains either "The" or "Great"

    `~`: The `~` symbol is used for negation, i.e., to exclude results that match a certain search term. 
    For example, if you want to search for all books whose title does not contain the word "Gatsby"

    """