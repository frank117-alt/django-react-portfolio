from rest_framework.pagination import PageNumberPagination

class SmallSetPagination(PageNumberPagination):
	page_query_param = 'p'
	page_size= 6
	max_size_query_param='page_size'
	max_page_size = 6


class MediumSetPagination(PageNumberPagination):
		page_query_param = 'p'
		page_size= 9
		max_size_query_param='page_size'
		max_page_size = 9


class LargeSetPagination(PageNumberPagination):
		page_query_param = 'p'
		page_size= 18
		max_size_query_param='page_size'
		max_page_size = 18