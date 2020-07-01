from rest_framework import filters

class SongsSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        if request.query_params.get('artistName'):
        #perform a related lookup on a ForeignKey or ManyToManyField with the lookup API double-underscore notation:
            return ['artist__name']
        return super(SongsSearchFilter, self).get_search_fields(view, request)

