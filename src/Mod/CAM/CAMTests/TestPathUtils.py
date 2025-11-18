# SPDX-License-Identifier: LGPL-2.1-or-later

# ***************************************************************************
# *   Copyright (c) 2025 FreeCAD contributors                               *
# *                                                                         *
# *   This program is free software; you can redistribute it and/or modify  *
# *   it under the terms of the GNU Lesser General Public License (LGPL)    *
# *   as published by the Free Software Foundation; either version 2 of     *
# *   the License, or (at your option) any later version.                   *
# *   for detail see the LICENCE text file.                                 *
# *                                                                         *
# *   This program is distributed in the hope that it will be useful,       *
# *   but WITHOUT ANY WARRANTY; without even the implied warranty of        *
# *   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         *
# *   GNU Library General Public License for more details.                  *
# *                                                                         *
# *   You should have received a copy of the GNU Library General Public     *
# *   License along with this program; if not, write to the Free Software   *
# *   Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  *
# *   USA                                                                   *
# *                                                                         *
# ***************************************************************************

import PathScripts.PathUtils as PathUtils

from CAMTests.PathTestUtils import PathTestWithAssets

class TestPathUtils(PathTestWithAssets):

    def test01(self):
        """
        Test getToolRadiusAtDepth calculation sanity
        """
        
        toolbit = self.assets.get("toolbit://5mm_Endmill")
        toolbit.set_property("Diameter", 10)

        # regular endmill has static diameter
        assert PathUtils.getToolRadiusAtDepth(toolbit.obj, 2) == 10

        toolbit = self.assets.get("toolbit://30degree_Vbit")
        toolbit.set_property("Diameter", 10)

        assert toolbit.obj.CuttingEdgeAngle == 30

        self.assertRoughly(PathUtils.getToolRadiusAtDepth(toolbit.obj, 2), 0.535898)

        # max radius is constrained by diameter property
        self.assertRoughly(PathUtils.getToolRadiusAtDepth(toolbit.obj, 20), 5)


        # min radius is constrained by tip diameter
        toolbit.set_property("TipDiameter", 1)
        self.assertRoughly(PathUtils.getToolRadiusAtDepth(toolbit.obj, 1), 0.5)



