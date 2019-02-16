# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def startupLogin(request):
    response_json = {}
    print(request.body)
    # email = json.loads(request.POST.get["eml"])
    # email = json.loads(request.body.decode('utf-8'))
    email = request.POST.get('eml')
    print(email)
    try:
    	if request.method=="POST":
	    	if Startup.objects.filter(email=email).exists():
	    		startup_instance = Startup.objects.filter(email=email)
	    		print(startup_instance)
	    		password = request.POST.get("pwd1")
	    		if str(password)== startup_instance.password:
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
    	message = "exception - " + e
    	response_json["success"] = False
    	response_json["message"] = message

    return JsonResponse(response_json)

# @csrf_exempt
# def postChallenge(request):
# 	response_json = {}
# 	data = json.loads(request.body.decode('utf-8'))

@csrf_exempt
def startupList(request):
    response_json = {}
    try:
        if request.method=="GET":
            startup_instance = Startup.objects.all()
            startup_list = []
            for c in startup_instance:
                x = {
                    "name" : c.name,
                    "field" : c.field,
                    "email" : c.email,
                    "description": c.description
                }

                startup_list.append(x)

            response_json["startup_list"] = startup_list
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