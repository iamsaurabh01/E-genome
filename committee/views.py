from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from.models import Committee
from django.http import JsonResponse

@csrf_exempt
def committeeLogin(request):
    response_json = {}
    email = request.POST.get("emlc")
    print(email)
    try:
    	if request.method=="POST":
	    	if Committee.objects.filter(email=email).exists():
	    		committee_instance = Committee.objects.get(email=email)
	    		print(committee_instance)
	    		password = request.POST.get("pwd2")
	    		if str(password)== committee_instance.password:
	    			response_json["success"] = True
	    			response_json["message"] = "Successfully Loggedin."
	    		else:
	    			response_json["success"] = False
	    			response_json["message"] = "Something wrong in the password."
	    	else:
	    		response_json["success"] = False
	    		response_json["message"] = "email doesnt exiast. Kindly register first before logging in."
    	else: 
    		response_json["success"] = False
    		response_json["message"] = "not post method"
    except Exception as e:
    	print(e)
    	message = "exception - " + str(e)
    	response_json["success"] = False
    	response_json["message"] = message

    return JsonResponse(response_json)

@csrf_exempt
def committeeRegistration(request):
	response_json = {}
	
	try:
		if request.method == "POST":
			email = request.POST.get("eml1")
			if Committee.objects.filter(email=email).exists():
				response_json["success"] = False
				response_json["message"] = "Please try to log in as you have already register"
			else:
				committee_instance = Committee.objects.create(email=email)
				committee_instance.password = request.POST.get("pwd3")
				committee_instance.institute_name = request.POST.get("inst")
				committee_instance.state = request.POST.get("state")
				committee_instance.city = request.POST.get("city")
				committee_instance.commmittee_name = request.POST.get("c_name")
				committee_instance.description = request.POST.get("desc")
				committee_instance.committee_type = request.POST.get("type")
				committee_instance.last2activities1 = request.FILES.get("file_1")
				committee_instance.last2activities2 = request.FILES.get("file_2")
				committee_instance.self_certification = request.FILES.get("file_3")
				committee_instance.save()

				response_json["success"] = True
				response_json["message"] = "Successfully Registered"

		else:
			response_json["success"] = False
			response_json["message"] = "Not Post method"

	except Exception as e:
		print(e)
		message = "Exception - " + str(e)
		response_json["success"] = False
		response_json["message"] = message 

	return JsonResponse(response_json)



@csrf_exempt
def committeeList(request):
	response_json = {}
	try:
		if request.method=="GET":
			committee_instance = Committee.objects.all()
			committee_list = []
			for c in committee_instance:
				x = {
					"committee_name" : c.commmittee_name,
					"institute_name" : c.institute_name,
					"email" : c.email,
				}

				committee_list.append(x)

			response_json["committee_list"] = committee_list
			response_json["success"] = True
			response_json["message"] = "list fecthed"
		else:
			response_json["success"] = False
			response_json["message"] = "not get method"

	except Exception as e:
		message = "exception - " + str(e)
		response_json["success"] = False
		response_json["message"] = message

	return JsonResponse(response_json)	
	