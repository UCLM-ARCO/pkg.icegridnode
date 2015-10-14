#!/usr/bin/python
# -*- mode:python; coding:utf-8; tab-width:4 -*-

import sys
import Ice


class App(Ice.Application):
    def run(self, args):
        proxy = self.communicator().propertyToProxy('Ice.Default.Locator')
        endpoint = proxy.ice_getEndpoints()[0]
        info = endpoint.getInfo()
        print info.host


App().main(sys.argv)
