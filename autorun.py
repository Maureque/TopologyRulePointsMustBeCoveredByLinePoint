# encoding: utf-8

import gvsig

from gvsig import uselib
uselib.use_plugin("org.gvsig.topology.app.mainplugin")

from pointsMustBeCoveredByLinePointRuleFactory import selfRegister

def main(*args):
    selfRegister()
