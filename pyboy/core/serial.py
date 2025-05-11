#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

class Serial:
    def __init__(self):
        self.SB = 0xFF  # Always 0xFF for a disconnected link cable
        self.SC = 0
        self._cycles_to_interrupt = 0
        self.last_cycles = 0

    def tick(self, _cycles):
        cycles = _cycles - self.last_cycles
        if cycles == 0:
            return False
        self.last_cycles = _cycles

        if self.SC & 0b10000000:
            self._cycles_to_interrupt -= cycles
            if self._cycles_to_interrupt <= 0:
                self.SC &= 0b01111111
                self._cycles_to_interrupt = 8 * 122
                return True
            return False
        return False

    def save_state(self, f):
        f.write(self.SB)
        f.write(self.SC)
        f.write_64bit(self.last_cycles)
        f.write_64bit(self._cycles_to_interrupt)

    def load_state(self, f, state_version):
        self.SB = f.read()
        self.SC = f.read()
        self.last_cycles = f.read_64bit()
        self._cycles_to_interrupt = f.read_64bit()
