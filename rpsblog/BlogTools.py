from rpsblog.models import *
from knowledge.models import *
class BlogTools(object):
	"""docstring for BlogTools"""
	def __init__(self):
		self.__recommendArticle = True
		self.__clickArticle = True
		self.__links = True
		self.__navgation = True
		self.__recentVisiter = True

	def getRecentVisiter(self): return self.__recentVisiter 
	def setRecentVisiter(self, value):self.__recentVisiter = value
	RecentVisiter = property(getRecentVisiter, setRecentVisiter, "Property RecentVisiter")

	def getRecommendArticle(self): return self.__recommendArticle 
	def setRecommendArticle(self, value):self.__recommendArticle = value
	RecommendArticle = property(getRecommendArticle, setRecommendArticle, "Property RecommendArticle")

	def getClickArticle(self): return self.__clickArticle 
	def setClickArticle(self, value):self.__clickArticle = value
	ClickArticle = property(getClickArticle, setClickArticle, "Property ClickArticle") 

	def getLinks(self): return self.__links 
	def setLinks(self, value):self.__links = value
	Links = property(getLinks, setLinks, "Property Links") 

	def getNavgation(self): return self.__navgation 
	def setNavgation(self, value):self.__navgation = value
	Navgation = property(getNavgation, setNavgation, "Property Navgation") 


	def getActiveTools(self):
		tool_dict = dict()
		knowlist = KnowLib.objects.all().order_by('-time')
		if len(knowlist) > 6:
			knowlist = knowlist[0:6]
		tool_dict['know_list'] = knowlist
		if self.__recommendArticle:
			artlist = Article.objects.all().order_by('-createTime')
			tool_dict['rec_list'] = artlist[0:6]
		if self.__clickArticle:
			click = Article.objects.all().order_by('-readCount')
			tool_dict['click_list'] = click[0:6]
		if self.__links:
			linklist = Link.objects.all()
			tool_dict['links_list'] = linklist.order_by('-time')
		if self.__navgation:
			navlist = Classification.objects.all()
			tool_dict['nav_list'] = navlist
		if self.__recentVisiter:
			vislist = Visiter.objects.all().order_by('-time')
			if len(vislist) > 8:
				vislist = vislist[0:8] 
			tool_dict['visiter_list'] = vislist
		return dict(tool_dict)

		