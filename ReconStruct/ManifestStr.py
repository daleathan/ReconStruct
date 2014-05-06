"""
ReconStruct

Reconstruct is a application which helps easily reverse engineer binary file
formats.  It is tested to run on Python 2.7, 3.3, 3.4 and pypy.

Copyright (c) 2014 Sandy Carter
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

try:
    from ReconStruct.ManifestBase import ManifestBase
except ImportError:
    from ManifestBase import ManifestBase


class ManifestStr(ManifestBase):
    """Descriptor manifest which parses strings"""
    def __init__(self, label, size, parent=None):
        super(ManifestStr, self).__init__(label, size, parent)

    def __call__(self, data, start=0):
        return data[start:start + self.size].decode("utf-8"), self.size

    @classmethod
    def type(cls):
        return 'str'
