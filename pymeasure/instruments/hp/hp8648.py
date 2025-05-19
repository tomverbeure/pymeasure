#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2025 PyMeasure Developers
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from pymeasure.instruments import Instrument, SCPIMixin
from pymeasure.instruments.validators import strict_discrete_set

import logging
log = logging.getLogger(__name__)
log.addHandler(logging.NullHandler())


class HP8648(SCPIMixin, Instrument):
    """ Represents the Hewlett Packard 8648 RF Signal Generator and 
    provides a high-level interface for interacting with the instrument.

    .. code-block:: python

        generator = HP8648("GPIB::12")

        generator.reset() 
        generator.power = 0                 # Sets the output power to 0 dBm
        generator.frequency = 100e6         # Sets the output frequency to 100 MHz
        generator.enable()                  # Enables the output
    """

    power = Instrument.control(
        ":POW?;", ":POW %g dBm;",
        """ A floating point property that represents the output power
        in dBm. This property can be set.
        """
    )
    frequency = Instrument.control(
        ":FREQ?;", ":FREQ %e Hz;",
        """ A floating point property that represents the output frequency
        in Hz. This property can be set.
        """
    )

    def __init__(self, adapter, name="Agilent 8648 RF Signal Generator", **kwargs):
        super().__init__(
            adapter, name, **kwargs
        )


    def enable(self):
        """ Enables the output of the signal. """
        self.write(":OUTPUT ON;")

    def disable(self):
        """ Disables the output of the signal. """
        self.write(":OUTPUT OFF;")





