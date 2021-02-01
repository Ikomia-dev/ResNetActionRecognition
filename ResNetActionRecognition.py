from ikomia import dataprocess
import ResNetActionRecognition_process as processMod
import ResNetActionRecognition_widget as widgetMod


# --------------------
# - Interface class to integrate the process with Ikomia application
# - Inherits dataprocess.CPluginProcessInterface from Ikomia API
# --------------------
class ResNetActionRecognition(dataprocess.CPluginProcessInterface):

    def __init__(self):
        dataprocess.CPluginProcessInterface.__init__(self)

    def getProcessFactory(self):
        # Instantiate process object
        return processMod.ResNetActionRecognitionProcessFactory()

    def getWidgetFactory(self):
        # Instantiate associated widget object
        return widgetMod.ResNetActionRecognitionWidgetFactory()
