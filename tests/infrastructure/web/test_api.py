from json import loads
from typing import List
from uuid import uuid4
from pytest import fixture, raises
from json import loads, dumps
from flask import Flask, request
from marshmallow import ValidationError
from mediark.application.models import Audio, Image
from mediark.infrastructure.core.configuration import ProductionConfig
from mediark.infrastructure.web.resources import RootResource
from mediark.infrastructure.web.spec import create_spec


# def test_api_images_search(app: Flask) -> None:
#     response = app.get('/images?filter=[["reference", "=", "ABC"]]')
#     data = str(response.data, 'utf-8')
#     data_dict = loads(data)
#     assert data
#     assert len(data_dict) == 1


# def test_api_audios_search(app: Flask) -> None:
#     response = app.get('/audios?filter=[["reference", "=", "XYZ"]]')
#     data = str(response.data, 'utf-8')
#     data_dict = loads(data)
#     assert data
#     assert len(data_dict) == 1
