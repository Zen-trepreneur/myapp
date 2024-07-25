#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 10:12:01 2024

@author: rudra
"""
from django.http import HttpResponse
from django.shortcuts import render
def index1(request):
    return HttpResponse('Hello World')

def index(request):
    return render(request,'index.html')