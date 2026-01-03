"""flight_plan.py

Simple examples showing how to control a DJI Tello using
the ``djitellopy`` library.

This module provides a safe `setup()` helper and a small
`simple_flight_path()` routine. Functions are defensive when
the drone object is not available.
"""

from typing import Optional
from djitellopy import Tello
from time import sleep


def setup() -> Optional[Tello]:
    """Create and connect to a Tello drone.

    Returns:
        Optional[Tello]: A connected ``Tello`` instance, or ``None`` if
        the connection failed.
    """

    try:
        tello = Tello()
        tello.connect()
    except Exception as exc:
        print(f"Failed to connect to Tello: {exc}")
        return None

    return tello


def simple_flight_path(tello: Optional[Tello], dist: int = 20) -> None:
    """Execute a short, simple flight path.

    The routine is defensive: it returns immediately if ``tello`` is
    ``None``. Movements use centimetres; distances should be small
    (e.g. 10-50) for safety during testing.

    Args:
        tello: A connected ``Tello`` instance, or ``None`` to skip.
        dist: Distance in centimetres for each horizontal movement.
    """

    if tello is None:
        print("No Tello instance provided. Aborting flight path.")
        return

    try:
        tello.takeoff()
        sleep(2)

        # x-axis movement
        tello.move_left(dist)
        sleep(1)
        tello.move_right(dist)
        sleep(1)

        # y-axis movement
        tello.move_forward(dist)
        sleep(1)
        tello.move_back(dist)
        sleep(1)

        # z-axis movement (use smaller steps for safety)
        tello.move_up(dist // 2)
        sleep(1)
        tello.move_down(dist // 2)
        sleep(1)

        tello.land()

    except Exception as exc:
        print("Error in simple_flight_path:\n", exc)
        try:
            if tello is not None and hasattr(tello, "land"):
                tello.land()
        except Exception:
            pass


if __name__ == "__main__":
    tello = setup()
    if tello is None:
        print("Setup failed; exiting.")
    else:
        try:
            simple_flight_path(tello, 15)
        except Exception as exc:
            print("Unhandled error in __main__:\n", exc)
        finally:
            try:
                if hasattr(tello, "end"):
                    tello.end()
            except Exception:
                pass
            del tello
