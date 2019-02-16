# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json
from .models import *
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def mentorLogin(request):
    response_json = {}
    email = request.POST.get("emlm")
    print(email)
    try:
    	if request.method=="POST":
	    	if Mentor.objects.filter(email=email).exists():
	    		mentor_instance = Mentor.objects.get(email=email)
	    		print(mentor_instance)
	    		password = request.POST.get("pwdm")
	    		if str(password)== mentor_instance.password:
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
def mentorRegistration(request):
    response_json = {}
    
    try:
        if request.method == "POST":
            email = request.POST.get("eml1")
            if Mentor.objects.filter(email=email).exists():
                response_json["success"] = False
                response_json["message"] = "Please try to log in as you have already register"
            else:
                mentor_instance = Mentor.objects.create(email=email)
                mentor_instance.password = request.POST.get("pwd3")
                mentor_instance.name = request.POST.get("comp")
                mentor_instance.country = request.POST.get("country")
                mentor_instance.address = request.POST.get("add")
                mentor_instance.description = request.POST.get("desc")
                mentor_instance.spicialization_field = request.POST.get("spcl")
                mentor_instance.document = request.FILES.get("file_4")	
                mentor_instance.save()

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
def mentorList(request):
    response_json = {}
    try:
        if request.method=="GET":
            mentor_instance = Mentor.objects.all()
            mentor_list = []
            for c in mentor_instance:
                x = {
                    "email" : c.email,
                    "spicialization_field" : c.spicialization_field,
                    "description" : c.description,
                    "name" : c.name,
                }

                investor_list.append(x)

            response_json["mentor_list"] = mentor_list
            response_json["success"] = True
            response_json["message"] = "list fecthed"
        else:
            response_json["success"] =  False
            response_json["message"] = "not get method"

    except Exception as e:
        message = "exception - " + str(e)
        response_json["success"] = False
        response_json["message"] = message

    return JsonResponse(response_json)