from __future__ import unicode_literals
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import News

@csrf_exempt
def news_feed(request):
	response_json = {}
	try:
		
		if request.method=="GET":
			news_query = News.objects.all()
			news_List = []
			for n in news_query:
				print(n.headline)
				news_json = {
					"headline": n.headline,
					"image": request.scheme + "://" + request.get_host() + '/media/' + str(n.news_image),
					"news_para" : n.news_para
				}
				news_List.append(news_json)

			response_json["news_list"]= news_List
			response_json["success"] = True
			response_json["message"] = "news list fetched"
		else:
			response_json["success"] = False
			response_json["message"] = "Some erroe occured while fetching"		

	except Exception as e:
		msg = "exception - " + str(e)
		response_json["success"] =False
		response_json["message"] = msg
	
	print(str(response_json))


	return JsonResponse(response_json)