import omni.ext
import importlib
import os
from .ogn import *

# Any class derived from `omni.ext.IExt` in top level module (defined in `python.modules` of `extension.toml`) will be
# instantiated when extension gets enabled and `on_startup(ext_id)` will be called. Later when extension gets disabled
# on_shutdown() is called.
class SimpleNodeExtension(omni.ext.IExt):
    # ext_id is current extension id. It can be used with extension manager to query additional information, like where
    # this extension is located on filesystem.
    def on_startup(self, ext_id):
        print("[ft_lab.OmniGraph.GetDateTime] startup")

    def on_shutdown(self):
        print("[ft_lab.OmniGraph.GetDateTime] shutdown")
