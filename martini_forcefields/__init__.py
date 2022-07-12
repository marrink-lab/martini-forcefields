# Copyright 2022 University of Groningen
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
import os
import pbr.version
__version__ = pbr.version.VersionInfo('martini_forcefields').release_string()

# Find the data directory once.
try:
    import pkg_resources
except ImportError:
    import os
    base_path = os.path.join(os.path.dirname(__file__), '')
    base_path_polarizable = os.path.join(os.path.dirname(__file__), 'polarizable')
    base_path_titratable = os.path.join(os.path.dirname(__file__), 'titratable')
    del os
else:
    base_path_regular = pkg_resources.resource_filename('polyply', 'regular')
    base_path_polarizable = pkg_resources.resource_filename('polyply', 'polarizable')
    base_path_titratable = pkg_resources.resource_filename('polyply', 'titratable')
    del pkg_resources

del pbr

# import all force-fields as local package variables
# for the regular force-field
for dirname in os.listdir(base_path):
    if dirname.startswith('v'):
        ff_name = "".join(dirname.split("."))
        locals()[ff_name] = os.path.join(base_path, dirname)

# import polarizable files
for dirname in os.listdir(base_path_polarizable):
    if dirname.startswith('v'):
        ff_name = "".join(dirname.split(".")) + "P"
        locals()[ff_name] = os.path.join(base_path, dirname)

# import titratable files
for dirname in os.listdir(base_path_titratable):
    if dirname.startswith('v'):
        ff_name = "".join(dirname.split(".")) + "T"
        locals()[ff_name] = os.path.join(base_path, dirname)
