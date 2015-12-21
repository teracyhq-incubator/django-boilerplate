# -*- coding:utf-8 -*-

# Copyright (c) Teracy, Inc. and individual contributors.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
#     1. Redistributions of source code must retain the above copyright notice,
#        this list of conditions and the following disclaimer.
#
#     2. Redistributions in binary form must reproduce the above copyright
#        notice, this list of conditions and the following disclaimer in the
#        documentation and/or other materials provided with the distribution.
#
#     3. Neither the name of Teracy, Inc. nor the names of its contributors may be used
#        to endorse or promote products derived from this software without
#        specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

"""
env = Env(BOOLEAN_VAR=bool, LIST_VAR=dict(type=list, subtype=int, cast=cast_func),
         BROKER_URL=dict(name='RABBITMQ_URL', if_only=func))

env.add(override=False)

env.add(BROKER_URL=[dict(name='RABBITMQ_URL', only_if='RABBITMQ_URL'),
                    dict(name='REDISCLOUD_URL', only_if=rediscloud_available_func)]
"""
import os

from envparse import env
from django.conf import settings


# _cached_setting_values = {} # {name: (value, override, ignore_none, prev_value)}

def setting_value(name, value, override=True, ignore_none=False):
    """Set new value settings
    By default, override default value.
    To skip override, pass override=False
    :param name:
    :param value:
    :param override:
    :param ignore_none:
    """
    if ignore_none and value is None:
        return

    # prev_value = getattr(settings, name, None)
    # _cached_setting_values[name] = (value, override, ignore_none, prev_value)
    if override:
        setattr(settings, name, value)
    else:
        value = getattr(settings, name, value)
        setattr(settings, name, value)


def cast_eval(value):
    """
    cast value by eval
    :param value:
    TODO(hoatle): any security concerns?
    """
    return eval(value)

BOOLEAN_TRUE_STRINGS = ('true', 'on', 'ok', 'y', 'yes', '1')


def cast_bool(value):
    """cast string to boolean
    :param value:
    """
    return value.lower() in BOOLEAN_TRUE_STRINGS


class Env(object):
    """
    Env class to process the schema
    :param schema:
    """

    def __init__(self, **schema):
        self._schema = schema
        self._parse()

    def _process_spec(self, var, spec):
        var_name = spec.get('name', var)
        only_if = spec.get('only_if')
        passed = True
        if callable(only_if):
            passed = only_if(self, var, spec)
        elif only_if:  # str
            # if only_if is string => check if that string is available as system env name
            passed = only_if in os.environ

        if not passed:
            return False, None

        kwargs = {}

        if 'cast' in spec:
            kwargs['cast'] = spec['cast']
        if 'default' in spec:
            kwargs['default'] = spec['default']

        return True, env(var_name, **kwargs)

    def _parse(self, schema=None):
        """parse the schema and set django settings"""
        if schema is not None:
            self._schema.update(schema)

        schema = schema or self._schema

        for var, spec in schema.iteritems():
            value = None
            override = None
            ignore_none = None

            if type(spec) is dict:
                passed, value = self._process_spec(var, spec)
                override = spec.get('override')
                ignore_none = spec.get('ignore_none')
            elif type(spec) is list or type(spec) is tuple:
                for spec_item in spec:
                    passed, value = self._process_spec(var, spec_item)
                    if passed:
                        override = spec_item.get('override')
                        ignore_none = spec_item.get('ignore_none')
                        break
            else:  # simple cast
                value = env(var, cast=spec)

            kwargs = {}
            if override is not None:
                kwargs['override'] = override
            if ignore_none is not None:
                kwargs['ignore_none'] = ignore_none

            setting_value(var, value, **kwargs)

    def add(self, **schema):
        """useful to extend the Env object
        :param schema:
        """
        # update schema, and re-parse
        # restore all existing settings from previous schema
        # global _cached_setting_values
        #
        # for name, store in _cached_setting_values.iteritems():
        #     if store[3] is None and store[2] is True:
        #         delattr(settings, name)
        #     else:
        #         setattr(settings, name, store[3])
        # _cached_setting_values = {}

        self._parse(schema)

# for convenience
env_vars = Env()
