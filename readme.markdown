# xmgrace_parser.py

This module provides a thin parser around [XMGrace][1] agr files

It provides the central AgrFile class, which simply stores all the lines
of an agr file, but in a small tree-like structure that make it easier to
access the different parts of the file. See the documentation of the
AgrFile class for more information about the layout of an agr file.
AgrFile provides methods for editing the different parts of the agr file
and making common modifications (such as exchanging the data for a plot).

The module fulfills two purposes:

1) Assisting in simple scripts that generate xmgrace plots based on an
   existing template (e.g. by replacing the plot data).

2) Allowing to *interactively* explore an agr file in [ipython][2], to edit its
   various parts, and to make common modifications to the file. A special
   emphasis is on controlling the plot layout in absolute units.

The module's purpose is *not* to create an agr file from scratch. For this,
use the [pygrace][3] module.

[1]: http://plasma-gate.weizmann.ac.il/Grace/
[2]: http://ipython.org
[3]: http://pygrace.github.io

## Installation ##

    pip install xmgrace_parser

## Example interactive usage ##

    # load ipython with agr object instantiated
    % xmgrace_parser plot.agr

    >>> agr.print_summary()
    Canvas size: 29.70 x 20.99 cm
    There are 3 drawing objects in the plot
    There are 5 regions in the plot
    There are 3 graphs in the plot
    Graph 0 [size 18.27 x 7.35 cm at (6.17, 11.54) cm]
        Set G0S0 (xy): 2000 data points
            comment: points_1_1.dat
            legend : f1(x)
        Set G0S1 (xy): 2000 data points
            comment: points_1_2.dat
            legend : f2(x)
    Graph 1 [size 6.05 x 7.35 cm at (6.17, 2.10) cm]
        Set G1S0 (xy): 2000 data points
            comment: points_2_1.dat
            legend : g1(x)
        Set G1S1 (xy): 1901 data points
            comment: points_2_2.dat
            legend : g2(x)
    Graph 2 [size 9.51 x 7.35 cm at (14.94, 2.099028.2) cm]
        Set G2S0 (xy): 2000 data points
            comment: points_3_1.dat

    # open EDITOR with header lines, to allow modifications
    >>> agr.edit_header()

    # read data of dataset G0S0 into numpy arrays
    >>> x, y = agr.get_data(0,0)

    # overwrite data of dataset G0S1
    >>> agr.set_data(0, 1, x, y, comment='new data')

    # overwrite data of dataset G0S0
    >>> agr.set_data(0, 0, filename='new.dat', columns=(0,1), legend='new')

    # change color of G0S0
    >>> g0s0 = agr.get_set(0,0)
    >>> g0s0.update_properties(line_color=2, symbol_color=2)

    # or, using the dictionary interface (less efficient if multiple
    # properties are set)
    >>> g0s0['line_color'] = 2
    >>> g0s0['symbol_color'] = 2

    # switch G0S0 and G0S1
    >>> agr.reorder_sets(0, (1,0))

    # Move down G0 by 1 cm
    >>> agr.set_graph_view(0, x_min=6.14, y_min=10.54,
    ... width=18.27, height=7.35)

    # What font size should I set if the text should be 10pt in the output PDF?
    >>> agr.fontsize(10)
    0.5379011902408587

    # If you prefer to work in inches, you can set the default unit:
    >>> DEFAULT_UNIT = 'inch'

    # set the canvas size to 8.5 x 4 cm
    >>> agr.set_size(8.5, 4)

    # kill graph 1 and 2
    >>> agr.kill_graph(1)
    >>> agr.kill_graph(1)

    # Set position of G0S0 in absolute units
    >>> agr.set_graph_view(0, 0, x_min=1.0, y_min=0.75, width=6, height=3)

    # You can do some rudimentary conversion between TeX and XmGrace
    # strings (and back with grace2tex):
    >>> tex2grace(r'|\epsilon_1(t)|')
    |\xe\f{}\s1\N(t)|

    # write out
    >>> agr.write()


The above examples are just a small subset of what is possible; please
explore the module using ipython's interactive capabilities (tab
completion!)

