#!/usr/bin/env python

"""Tests for `threaded_mvc` package."""

#import pytest


#from threaded_mvc import Model, View, Controller
import threaded_mvc.model, threaded_mvc.view, threaded_mvc.controller

mvcmodel = threaded_mvc.model.Model()
mvcview = threaded_mvc.view.View()
mvccontroller = threaded_mvc.controller.Controller()

#@pytest.fixture
#def response():
#    """Sample pytest fixture.
#
#    See more at: http://doc.pytest.org/en/latest/fixture.html
#    """
#    # import requests
#    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


#def test_content(response):
#    """Sample pytest test function with the pytest fixture as an argument."""
#    # from bs4 import BeautifulSoup
#    # assert 'GitHub' in BeautifulSoup(response.content).title.string
