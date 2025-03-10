# -*- coding: utf-8 -*-
"""
System-related binary handling
"""

import sys

from mathics.core.atoms import Integer, Integer1, IntegerM1
from mathics.core.builtin import Predefined


class ByteOrdering(Predefined):
    """
    <url>
    :WMA link:
    https://reference.wolfram.com/language/ref/ByteOrdering.html</url>
    <dl>
      <dt>'ByteOrdering'
      <dd> is an option for BinaryRead, BinaryWrite, and related functions \
      that specifies what ordering of bytes should be assumed for your \
      computer system..
    </dl>

    """

    name = "ByteOrdering"
    rules = {"ByteOrdering": "$ByteOrdering"}
    summary_text = "ordering of the bits in a byte"


class ByteOrdering_(Predefined):
    r"""
    <url>:WMA link:https://reference.wolfram.com/language/ref/$ByteOrdering.html</url>
        <dl>
          <dt>'\$ByteOrdering'
          <dd>returns the native ordering of bytes in binary data on your computer system.
        </dl>

    """

    name = "$ByteOrdering"
    summary_text = "native machine byte ordering of the computer system"

    def evaluate(self, evaluation) -> Integer:
        return Integer1 if sys.byteorder == "big" else IntegerM1
