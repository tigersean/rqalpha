# -*- coding: utf-8 -*-
#
# Copyright 2017 Ricequant, Inc
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from rqalpha.interface import AbstractMod
from rqalpha.utils.logger import system_log

from .data_source import DataSource
from .event_source import RealtimeEventSource


class RealtimeTradeMod(AbstractMod):

    def start_up(self, env, mod_config):
        self._env = env
        self._mod_config = mod_config

        env.set_data_source(DataSource(env.config.base.data_bundle_path))
        env.set_event_source(RealtimeEventSource())

        # ExecutionContext.data_proxy.all_instruments("CS")

    def tear_down(self, code, exception=None):
        pass
