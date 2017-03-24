# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django import forms
from django.forms.extras.widgets import SelectDateWidget


class RemarkForm(forms.Form):
        start_time = forms.DateTimeField(input_formats="%Y-%m-%d %H:%M:%S",
                                         widget=SelectDateWidget,
                                         label="开始时间")
        end_time = forms.DateTimeField(input_formats="%Y-%m-%d %H:%M:%S",
                                         widget=SelectDateWidget,
                                         label="结束时间")


class TimeForm(forms.Form):
    start_time = forms.DateTimeInput()
    end_time = forms.DateTimeInput()
