#!/bin/env python2.7
from gtk.gdk import *
import gtk.gdk
import time
import sys
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Set gtk window properties")
    parser.add_argument('-o', '--override-redirect',
                        help="Set override redirect flag",
                        type=int,
                        dest="override_redirect")
    parser.add_argument('-d', '--decorations',
                        help="Hide or show window decorations",
                        type=int,
                        dest="decorations")
    parser.add_argument('-a', '--keep-above',
                        help="Keep window above others",
                        type=int,
                        dest="keep_above")
    parser.add_argument('-b', '--keep-below',
                        help="Keep window below others",
                        type=int,
                        dest="keep_below")
    parser.add_argument('-m', '--move',
                        dest='position',
                        metavar="X,Y",
                        default=None,
                        type=lambda x: [int(x) for x in x.split(",")],
                        help="Move window to position X,Y (default: None)")
    parser.add_argument('-r', '--resize',
                        dest='size',
                        metavar="WxH",
                        default=None,
                        type=lambda x: [int(x) for x in x.split("x")],
                        help="Resize window to WxH (default: None)")
    parser.add_argument('windows',
                        metavar='WINDOWID',
                        type=str,
                        nargs='+',
                        help='Apply actions to window with WINDOWID')
    args = parser.parse_args()

    for window in args.windows:
        if window == "ACTIVE":
            w = window_foreign_new(
                (get_default_root_window().property_get(
                    "_NET_ACTIVE_WINDOW")[2][0])
            )
        else:
            w = window_foreign_new(int(window, 16))

        if args.keep_above is not None:
            w.set_keep_above(args.keep_above)

        if args.decorations is not None:
            if args.decorations:
                print("Decorations True")
                time.sleep(1)
                w.set_decorations(gtk.gdk.DECOR_ALL)
            else:
                time.sleep(1)
                w.set_decorations(0)

        if args.override_redirect is not None:
            w.set_override_redirect(args.override_redirect)
            gtk.gdk.flush()
            time.sleep(0.5)

        if args.position:
            # Sleep to give time for other properties to be applied
            time.sleep(1)
            w.move(args.position[0], args.position[1])
        elif args.keep_above is not None:
            w.set_keep_above(args.keep_above)

        gtk.gdk.flush()

