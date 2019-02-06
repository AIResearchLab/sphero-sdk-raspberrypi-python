#!/usr/bin/env python3
# This file is automatically generated!
# Toy Name:           Sphero Mock
# Prefix:             MK
# Command Count:      0
# Timestamp:          01/23/2019 @ 18:37:41.354353 (UTC)

from threading import Thread
from spheroboros.blocking.common.toys.blocking_sphero_toy import BlockingSpheroToy
from spheroboros.blocking.client.dal.restful_blocking_dal import RestfulBlockingDal


class BlockingSpheroMock(BlockingSpheroToy):
    def __init__(self, dal=RestfulBlockingDal(prefix='mk')):
        BlockingSpheroToy.__init__(self)
        self._dal = dal
