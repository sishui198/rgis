# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_rivergis.ui'
#
# Created: Sun May 17 23:23:34 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from qgis.gui import QgsProjectionSelectionWidget

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RiverGIS(object):
    def setupUi(self, RiverGIS):
        RiverGIS.setObjectName(_fromUtf8("RiverGIS"))
        RiverGIS.setEnabled(True)
        RiverGIS.resize(600, 400)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/rivergis.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        RiverGIS.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(RiverGIS)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lineEdCurDatabase = QtGui.QLineEdit(self.centralwidget)
        self.lineEdCurDatabase.setReadOnly(True)
        self.lineEdCurDatabase.setObjectName(_fromUtf8("lineEdCurDatabase"))
        self.gridLayout.addWidget(self.lineEdCurDatabase, 0, 1, 1, 1)
        self.labelCurSchema = QtGui.QLabel(self.centralwidget)
        self.labelCurSchema.setObjectName(_fromUtf8("labelCurSchema"))
        self.gridLayout.addWidget(self.labelCurSchema, 0, 2, 1, 1)
        self.lineEdCurSchema = QtGui.QLineEdit(self.centralwidget)
        self.lineEdCurSchema.setReadOnly(True)
        self.lineEdCurSchema.setObjectName(_fromUtf8("lineEdCurSchema"))
        self.gridLayout.addWidget(self.lineEdCurSchema, 0, 3, 1, 1)
        self.labelCurDatabase = QtGui.QLabel(self.centralwidget)
        self.labelCurDatabase.setObjectName(_fromUtf8("labelCurDatabase"))
        self.gridLayout.addWidget(self.labelCurDatabase, 0, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.gridLayout_2.addWidget(self.textEdit, 1, 0, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.crsWidget = QgsProjectionSelectionWidget(self.centralwidget)
        self.crsWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.crsWidget.setMaximumSize(QtCore.QSize(400, 16777215))
        self.crsWidget.setObjectName(_fromUtf8("crsWidget"))
        self.horizontalLayout.addWidget(self.crsWidget)
        self.gridLayout_2.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        RiverGIS.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RiverGIS)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menu_Results = QtGui.QMenu(self.menubar)
        self.menu_Results.setObjectName(_fromUtf8("menu_Results"))
        self.menu_Geometry = QtGui.QMenu(self.menubar)
        self.menu_Geometry.setObjectName(_fromUtf8("menu_Geometry"))
        self.menuDB = QtGui.QMenu(self.menubar)
        self.menuDB.setObjectName(_fromUtf8("menuDB"))
        RiverGIS.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RiverGIS)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RiverGIS.setStatusBar(self.statusbar)
        self.dock = QtGui.QDockWidget(RiverGIS)
        self.dock.setAllowedAreas(QtCore.Qt.LeftDockWidgetArea|QtCore.Qt.RightDockWidgetArea)
        self.dock.setObjectName(_fromUtf8("dock"))
        self.dockWidgetContents = QtGui.QWidget()
        self.dockWidgetContents.setObjectName(_fromUtf8("dockWidgetContents"))
        self.dock.setWidget(self.dockWidgetContents)
        RiverGIS.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dock)
        self.actionCreate2dAreaPerimeter = QtGui.QAction(RiverGIS)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/2darea_perimeter.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate2dAreaPerimeter.setIcon(icon1)
        self.actionCreate2dAreaPerimeter.setObjectName(_fromUtf8("actionCreate2dAreaPerimeter"))
        self.actionCorrect_Lateral_Weirs = QtGui.QAction(RiverGIS)
        self.actionCorrect_Lateral_Weirs.setEnabled(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/correctLateralWeir.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCorrect_Lateral_Weirs.setIcon(icon2)
        self.actionCorrect_Lateral_Weirs.setObjectName(_fromUtf8("actionCorrect_Lateral_Weirs"))
        self.actionCreate2dArea = QtGui.QAction(RiverGIS)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/2darea.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate2dArea.setIcon(icon3)
        self.actionCreate2dArea.setObjectName(_fromUtf8("actionCreate2dArea"))
        self.actionAbout = QtGui.QAction(RiverGIS)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionHelpContents = QtGui.QAction(RiverGIS)
        self.actionHelpContents.setObjectName(_fromUtf8("actionHelpContents"))
        self.actionLoad_2D_WSEL_from_HDF = QtGui.QAction(RiverGIS)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/loadWselHdf.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoad_2D_WSEL_from_HDF.setIcon(icon4)
        self.actionLoad_2D_WSEL_from_HDF.setObjectName(_fromUtf8("actionLoad_2D_WSEL_from_HDF"))
        self.actionCreate_Water_Surface_Raster = QtGui.QAction(RiverGIS)
        self.actionCreate_Water_Surface_Raster.setEnabled(True)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/createWselRaster.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Water_Surface_Raster.setIcon(icon5)
        self.actionCreate_Water_Surface_Raster.setObjectName(_fromUtf8("actionCreate_Water_Surface_Raster"))
        self.actionImportRiverFromIsokp = QtGui.QAction(RiverGIS)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/importFromIsok.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionImportRiverFromIsokp.setIcon(icon6)
        self.actionImportRiverFromIsokp.setObjectName(_fromUtf8("actionImportRiverFromIsokp"))
        self.actionRefresh = QtGui.QAction(RiverGIS)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/action_refresh.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon7)
        self.actionRefresh.setObjectName(_fromUtf8("actionRefresh"))
        self.actionCreate_Depths_and_Flood_Range = QtGui.QAction(RiverGIS)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/createDepthsAndRange.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCreate_Depths_and_Flood_Range.setIcon(icon8)
        self.actionCreate_Depths_and_Flood_Range.setObjectName(_fromUtf8("actionCreate_Depths_and_Flood_Range"))
        self.actionLoad_1D_WSEL_from_HDF = QtGui.QAction(RiverGIS)
        self.actionLoad_1D_WSEL_from_HDF.setObjectName(_fromUtf8("actionLoad_1D_WSEL_from_HDF"))
        self.actionLoad_WSEL_from_HEC_RAS = QtGui.QAction(RiverGIS)
        self.actionLoad_WSEL_from_HEC_RAS.setIcon(icon4)
        self.actionLoad_WSEL_from_HEC_RAS.setObjectName(_fromUtf8("actionLoad_WSEL_from_HEC_RAS"))
        self.actionCreate_1d_PostGIS_Tables = QtGui.QAction(RiverGIS)
        self.actionCreate_1d_PostGIS_Tables.setObjectName(_fromUtf8("actionCreate_1d_PostGIS_Tables"))
        self.actionSave_mesh_points_to_HEC_RAS_geometry_file = QtGui.QAction(RiverGIS)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/rivergis/icons/save2dmeshPtsToGeo.svg")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_mesh_points_to_HEC_RAS_geometry_file.setIcon(icon9)
        self.actionSave_mesh_points_to_HEC_RAS_geometry_file.setObjectName(_fromUtf8("actionSave_mesh_points_to_HEC_RAS_geometry_file"))
        self.actionPreview_2D_Mesh = QtGui.QAction(RiverGIS)
        self.actionPreview_2D_Mesh.setObjectName(_fromUtf8("actionPreview_2D_Mesh"))
        self.menuHelp.addAction(self.actionHelpContents)
        self.menu_Results.addAction(self.actionLoad_WSEL_from_HEC_RAS)
        self.menu_Results.addSeparator()
        self.menu_Results.addAction(self.actionCreate_Water_Surface_Raster)
        self.menu_Results.addAction(self.actionCreate_Depths_and_Flood_Range)
        self.menu_Geometry.addAction(self.actionCreate2dArea)
        self.menu_Geometry.addAction(self.actionPreview_2D_Mesh)
        self.menu_Geometry.addAction(self.actionSave_mesh_points_to_HEC_RAS_geometry_file)
        self.menu_Geometry.addAction(self.actionCorrect_Lateral_Weirs)
        self.menu_Geometry.addSeparator()
        self.menu_Geometry.addAction(self.actionCreate_1d_PostGIS_Tables)
        self.menuDB.addAction(self.actionRefresh)
        self.menuDB.addAction(self.actionImportRiverFromIsokp)
        self.menubar.addAction(self.menuDB.menuAction())
        self.menubar.addAction(self.menu_Geometry.menuAction())
        self.menubar.addAction(self.menu_Results.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(RiverGIS)
        QtCore.QMetaObject.connectSlotsByName(RiverGIS)
        RiverGIS.setTabOrder(self.textEdit, self.lineEdCurSchema)
        RiverGIS.setTabOrder(self.lineEdCurSchema, self.lineEdCurDatabase)

    def retranslateUi(self, RiverGIS):
        RiverGIS.setWindowTitle(_translate("RiverGIS", "RiverGIS", None))
        self.lineEdCurDatabase.setPlaceholderText(_translate("RiverGIS", "-----", None))
        self.labelCurSchema.setText(_translate("RiverGIS", "Current Schema:", None))
        self.lineEdCurSchema.setPlaceholderText(_translate("RiverGIS", "------", None))
        self.labelCurDatabase.setText(_translate("RiverGIS", "Current Connection:", None))
        self.label.setText(_translate("RiverGIS", "Projection", None))
        self.menuHelp.setTitle(_translate("RiverGIS", "Help", None))
        self.menu_Results.setTitle(_translate("RiverGIS", "Results", None))
        self.menu_Geometry.setTitle(_translate("RiverGIS", "Geometry", None))
        self.menuDB.setTitle(_translate("RiverGIS", "Database", None))
        self.dock.setAccessibleName(_translate("RiverGIS", "QRAS_DBView", None))
        self.dock.setWindowTitle(_translate("RiverGIS", "Connections", None))
        self.actionCreate2dAreaPerimeter.setText(_translate("RiverGIS", "2D Area (Perimeter)", None))
        self.actionCorrect_Lateral_Weirs.setText(_translate("RiverGIS", "Correct Lateral Weirs", None))
        self.actionCreate2dArea.setText(_translate("RiverGIS", "Create 2D Flow Areas", None))
        self.actionAbout.setText(_translate("RiverGIS", "About", None))
        self.actionHelpContents.setText(_translate("RiverGIS", "Contents", None))
        self.actionLoad_2D_WSEL_from_HDF.setText(_translate("RiverGIS", "Load 2D WSEL from HDF", None))
        self.actionCreate_Water_Surface_Raster.setText(_translate("RiverGIS", "Create Water Surface Raster", None))
        self.actionImportRiverFromIsokp.setText(_translate("RiverGIS", "Import River Data From ISOKP Database", None))
        self.actionRefresh.setText(_translate("RiverGIS", "Refresh", None))
        self.actionCreate_Depths_and_Flood_Range.setText(_translate("RiverGIS", "Create Depths and Flood Range", None))
        self.actionLoad_1D_WSEL_from_HDF.setText(_translate("RiverGIS", "Load 1D WSEL from HDF", None))
        self.actionLoad_WSEL_from_HEC_RAS.setText(_translate("RiverGIS", "Load max WSEL from HEC-RAS", None))
        self.actionCreate_1d_PostGIS_Tables.setText(_translate("RiverGIS", "Create 1D PostGIS Tables", None))
        self.actionSave_mesh_points_to_HEC_RAS_geometry_file.setText(_translate("RiverGIS", "Save mesh points to HEC-RAS geometry file", None))
        self.actionPreview_2D_Mesh.setText(_translate("RiverGIS", "Preview 2D Mesh", None))

import resources_rc
