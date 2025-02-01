# SwissKnife
"Swiss knife" for electronics: function generator, voltmeter, PWM generator etc. by Pico + some analog parts

When I began to have a look at the possibilities that the Pico PIO offer, I did not expect such a long and interesting journey.
While working on the documentation of my experiments the idea for a small inexpensive but powerful tool arose, a sort of "Swiss knife" with many accessories you nee in the daily work.
I started with the Arbitrary Waveform Generator ( see https://github.com/jean-claudeF/ArbitraryWaveformGenerator )
and added one little piece after the other.

## Overview
(As work in progress, this is still evolving)

### Ready to use
- Audio Function Generator ( Arbitrary Waveform Generator)
- PWM generator
- Quadruple voltmeter
- I2C scan gives addresses on the bus

### Planned but not yet ready
- Analog output
- Tester for I2C devices (e.g. OLED etc.)
- DS18x20 temperature sensor tester / recorder
- MIDI decoder

## Structure
- Hardware consisting of a Pico, R2R DA converter, amplifer for 20Vpp audio signal, buffer for AD converter
- Micropython firmware on the Pico providing functions that can be called from a serial terminal or a dedicated PC software written in Python.
- Tkinter GUI for the PC, written in Python

 
