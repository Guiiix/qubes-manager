# The Qubes OS Project, https://www.qubes-os.org/
#
# Copyright (C) 2024 Marta Marczykowska-Górecka
#                                       <marmarta@invisiblethingslab.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
#

import pytest
from qubesadmin.tests.mock_app import MockQubesComplete


@pytest.fixture
def test_qubes_app():
    test_qapp = MockQubesComplete()
    test_qapp._qubes['sys-usb'].features[
        'supported-feature.keyboard-layout'] = '1'
    test_qapp._qubes['test-standalone'].features['prohibit-start'] = \
        'Control qube which should be start prohibited from Manager launch'
    test_qapp.update_vm_calls()

    return test_qapp
