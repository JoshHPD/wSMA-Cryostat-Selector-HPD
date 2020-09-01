=====
Usage
=====

To use wSMA-Cryostat-Selector in a project::

	import wsma_cryostat_selector

Then create a Selector object::

    sel = wsma_cryostat_selector.Selector(ip_address=192.168.42.100)

This opens a PyModbusTCP client with the selector controller at ip_address and
reads the current state from it.

Move the selector wheel to a given position with::

    sel.set_position(<position>)

where <position> is one of 1, 2, 3 or 4.

Home the selector wheel with::

    sel.home()

The current state is available via the Selector properties of .position, .speed,
.delta, and .time.  Delta is the position error in units of 1/100ths of a degree.
Time is the time taken for the last move in milliseconds.
