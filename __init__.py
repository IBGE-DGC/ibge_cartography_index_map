# -*- coding: utf-8 -*-
"""
/***************************************************************************
 IBGECartographyIndexMap
                                 A QGIS plugin
 This plugin displays in QGIS the index layers from IBGE Cartography Department.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2021-05-17
        copyright            : (C) 2021 by Marcel Rotunno (IBGE)
        email                : marcelgaucho@yahoo.com.br
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load IBGECartographyIndexMap class from file IBGECartographyIndexMap.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .ibge_cartography_index_map import IBGECartographyIndexMap
    return IBGECartographyIndexMap(iface)
