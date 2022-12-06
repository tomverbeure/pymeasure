#
# This file is part of the PyMeasure package.
#
# Copyright (c) 2013-2022 PyMeasure Developers
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

from pymeasure.instruments import Instrument, Channel
from pymeasure.instruments.validators import strict_discrete_set

class OutputChannel(Channel):
    """Implementation of a base Agilent E36xxA power supply channel."""

    def __init__(self, instrument, id):
        super().__init__(instrument, id)

    enabled = Instrument.control(
        "INST:SEL {ch};:OUTPUT:STATE?",
        "INST:SEL {ch};:OUTPUT:STATE %s", 
        """A boolean property that enables an output channel.""",
        validator=strict_discrete_set,
        values={True: "ON", False: "OFF"},
        map_values=True,
        get_process=lambda v: "ON" if v == 1 else ("OFF" if v == 0 else v),
        dynamic=True
    )

    voltage = Instrument.control(
        "INST:SEL {ch};:SOURCE:VOLTAGE:LEVEL:IMMEDIATE:AMPLITUDE?", 
        "INST:SEL {ch};:SOURCE:VOLTAGE:LEVEL:IMMEDIATE:AMPLITUDE %g", 
        """A floating point property that represents the output voltage
        setting of the power supply in Volts. This property can be set. """
    )

    max_voltage = Instrument.measurement(
        "INST:SEL {ch};:SOURCE:VOLTAGE:LEVEL:IMMEDIATE:AMPLITUDE? MAX",
        """A floating point property that represents the maximum possible output voltage in Volts"""
    )

    min_voltage = Instrument.measurement(
        "INST:SEL {ch};:SOURCE:VOLTAGE:LEVEL:IMMEDIATE:AMPLITUDE? MIN",
        """A floating point property that represents the minimum possible output voltage in Volts"""
    )

    measured_voltage = Instrument.measurement(
        "MEASURE:VOLTAGE:DC? {ch}",
        """A floating point property that represents measured voltage in Volts"""
    )

    current = Instrument.control(
        "INST:SEL {ch};:SOURCE:CURRENT:LEVEL:IMMEDIATE:AMPLITUDE?", 
        "INST:SEL {ch};:SOURCE:CURRENT:LEVEL:IMMEDIATE:AMPLITUDE %g", 
        """A floating point property that represents the output current
        setting of the power supply in Ampere. This property can be set. """
    )

    max_current = Instrument.measurement(
        "INST:SEL {ch};:SOURCE:CURRENT:LEVEL:IMMEDIATE:AMPLITUDE? MAX",
        """A floating point property that represents the maximum possible output current in Volts"""
    )

    min_current = Instrument.measurement(
        "INST:SEL {ch};:SOURCE:CURRENT:LEVEL:IMMEDIATE:AMPLITUDE? MIN",
        """A floating point property that represents the minimum possible output current in Volts"""
    )


    measured_current = Instrument.measurement(
        "MEASURE:CURRENT:DC? {ch}",
        """A floating point property that represents measured current in Ampere"""
    )


class AgilentE36xxA(Instrument):
    """
    Represent the HP/Agilent/Keysight E36xxA and related power supplies.

    """

    def __init__(self, adapter, model, **kwargs):
        super().__init__(
            adapter, model, **kwargs
        )

    def beep(self):
        self.write("SYST:BEEP")

class AgilentE3631A(AgilentE36xxA):

    ch_scpi_names = ( 'P6V', 'P25V', 'N25V' ) 
    ch = Instrument.ChannelCreator(OutputChannel, ch_scpi_names)

    def __init__(self, adapter, **kwargs):
        super().__init__(
            adapter, "HP/Agilent/Keysight E3631A Power Supply", **kwargs
        )

