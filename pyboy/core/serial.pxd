#
# License: See LICENSE.md file
# GitHub: https://github.com/Baekalfen/PyBoy
#

from libc.stdint cimport int64_t, uint8_t, uint16_t, uint32_t, uint64_t

from pyboy.utils cimport IntIOInterface

import cython

from pyboy.logging.logging cimport Logger


cdef Logger logger

cdef class Serial:
    cdef uint64_t SB, SC
    cdef int64_t _cycles_to_interrupt
    cdef uint64_t last_cycles

    cdef bint tick(self, uint64_t) noexcept nogil

    cdef int save_state(self, IntIOInterface) except -1
    cdef int load_state(self, IntIOInterface, int) except -1
