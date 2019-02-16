# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def investorLogin(request):
    response_json = {}
    print(request.body)
    # email = json.loads(request.POST.get["eml"])
    # email = json.loads(request.body.decode('utf-8'))
    email = request.POST.get('emli')
    print(email)
    try:
    	if request.method=="POST":
	    	if Investor.objects.filter(email=email).exists():
	    		investor_instance = Investor.objects.filter(email=email)
	    		print(investor_instance)
	    		password = request.POST.get('pwdi')
	    		if str(password)== investor_instance.password:
	    			response_json["success"] = True
	    			response_json["message"] = "Successfully Loggedin."
	    		else:
	    			response_json["success"] = False
	    			response_json["message"] = "Something wrong in the password."
	    	else:
	    		response_json["success"] = False
	    		response_json["message"] = "email doesnt exist. Kindly register first before logging in."

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
def investorRegistration(request):
    response_json = {}
    
    try:
        if request.method == "POST":
            email = request.POST.get("emli")
            if Investor.objects.filter(email=email).exists():
                response_json["success"] = False
                response_json["message"] = "Please try to log in as you have already register"
            else:
                investor_instance = Investor.objects.create(email=email)
                investor_instance.password = request.POST.get("pwd3")
                investor_instance.company_name = request.POST.get("comp")
                investor_instance.country = request.POST.get("country")
                investor_instance.address = request.POST.get("add")
                investor_instance.company_type = request.POST.get("t_name")
                investor_instance.description = request.POST.get("desc")
                investor_instance.committee_type = request.POST.get("type")
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
def investorList(request):
    response_json = {}
    try:
        if request.method=="GET":
            investor_instance = Investor.objects.all()
            investor_list = []
            for c in investor_instance:
                x = {
                    "email" : c.email,
                    "company_name" : c.company_name,
                    "company_type" : c.company_type,
                    "description" : c.description,
                }

                investor_list.append(x)

            response_json["investor_list"] = committee_list
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