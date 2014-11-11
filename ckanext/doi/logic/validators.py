#!/usr/bin/env python
# encoding: utf-8
"""
Created by 'bens3' on 2013-06-21.
Copyright (c) 2013 'bens3'. All rights reserved.
"""

import re

import ckan.plugins as p
from ckan.common import _
import ckan.logic as logic
import ckan.lib.navl.dictization_functions as df
from ckanext.doi.helpers import mandatory_field_is_editable

missing = df.missing
StopOnError = df.StopOnError
Invalid = df.Invalid

get_action = logic.get_action


def editable_mandatory_field(key, data, errors, context):

    pkg_dict = get_action('package_show')(context, {'id': context['package'].id})
    value = data.get(key)
    field = key[0]

    # Raise an error if the field value has been updated and this field is no longer editable
    if value != pkg_dict[field] and not mandatory_field_is_editable(pkg_dict):
        errors[key].append(_('Core DOI metadata fields are no longer editable.'))
        raise StopOnError