# -*- coding: utf-8 -*-
from flask import jsonify, request
from . import api
@api.route('/catalog/product')
def product():
    """

    {
        category_id : ""
        sortColum : ""
        fileterAttrs:{''}
    }

    """
    category_id = request.json.get("category_id")
    sortcolum = request.json.get("sortcolum")
    fileterAttrs = request.json.get("fileterAttrs")

