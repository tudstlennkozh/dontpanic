import sys
import random
import uno
import unohelper
from org.tudstlennkozh.DontPanic import XDontPanic

import marvin


class DontPanicImpl( unohelper.Base, XDontPanic ):
	def __init__( self, ctx ):
		self.ctx = ctx

	def h2g2(self, a):
		if marvin.check_question(a, 0.95):
			return 42
		else:
			# some kind of Infinite Improbability
			return random.randint(0, 92272036)


def createInstance( ctx ):
	return DontPanicImpl( ctx )


g_ImplementationHelper = unohelper.ImplementationHelper()
g_ImplementationHelper.addImplementation(
	createInstance,"org.tudstlennkozh.DontPanic.python.DontPanicImpl",
		("com.sun.star.sheet.AddIn",),)
