#!/usr/bin/python

# Copyright 2015 Huawei Devices USA Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
#
# Authors:
#       Chuk Orakwue <chuk.orakwue@huawei.com>

"""
    GlitchType: Possible glitch types.
"""
from .common import ConstantBase

class GlitchType(ConstantBase):
    UNDERRUN_FULL = () # framesReady() is full frame count, no underrun
    UNDERRUN_PARTIAL = () # framesReady() is non-zero but < full frame count
    UNDERRUN_EMPTY = () # framesReady() is zero, total underrun
    OVERRUN = ()
    UNKNOWN = ()
    
    @classmethod
    def underruns(cls):
        return [cls.UNDERRUN_PARTIAL, cls.UNDERRUN_EMPTY]