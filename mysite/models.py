#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 14:22:11 2024

@author: rudra
"""

from django.db import models

class TestModels(models.Model):
    
    name = models.charField(max_length=20)