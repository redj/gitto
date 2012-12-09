# coding: utf-8
#
# GittoOnSave for Sublime Text 2
#
# Copyright (c) 2012, Réjean Loyer
#
# All rights reserved.
#
#    Redistribution and use in source and binary forms, with or without
#    modification, are permitted provided that the following conditions are met:
# 
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright notice,
#       this list of conditions and the following disclaimer in the documentation
#       and/or other materials provided with the distribution.
#     * Neither the name of Ecere Corporation nor the names of its contributors
#       may be used to endorse or promote products derived from this software 
#       without specific prior written permission.
# 
#    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#    "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#    LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#    A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#    OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#    SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#    LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#    DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#    THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#    (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
#

#
# Explaination
#
# GittoOnSave will look for every Gitto repository potentially tracking
# the file that's just been saved. Those are all the Gitto repositories
# in parent directories of the file that's been saved.
#
# For each Gitto repository it finds, GittoOnSave will call _gitto_ with
# the _flash_ command in that repository's directory.
#
# Please see Gitto documentation for the details on the _flash_ command.
#
#

#
# Change Log
# (Time stamps are given in GMT-5.)
#
# 2012.12.03 20.58  -  Final Version
#                      This program should be considered complete and mature.
#                      I don't expect the source code will change at all in the future.
#                      The documentation part might see some changes.
#
# 2012.12.02 01.09  -  Birth
#
#

#
# Notes on Operation
#
# Gitto and it's dependencies (Git) must be installed of course.
# Make sure the gitto program is in your system path.
#
#

import sublime, sublime_plugin, os, subprocess

class GittoOnSave(sublime_plugin.EventListener):
	def on_post_save(self, view):
		path = os.path.split(view.file_name())[0]
		while os.path.exists(path):
			if not os.path.basename(path):
				break
			if os.path.exists(os.path.join(path, ".gitto")) and os.path.exists(os.path.join(path, ".git")):
				subprocess.call(["cd " + path + " && gitto flash &"],shell=True)
			path = os.path.split(path)[0]
