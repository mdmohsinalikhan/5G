HY poster
=========

An unoffical LaTeX poster template themed for the University of Helsinki

How to use
----------

Download your faculty logo from [Helsinki University logodomain](http://hy.logodomain.com/), preferably in eps format, to include it in the header of your poster. It is recommended to autocrop the logo using `epstool` to get rid of the extra margin in the image:

    epstool --copy --bbox inputfile.eps outputfile.eps

There is also a space for the logo of your division/project/campaign.

Change `facultyColor` to match the color of your faculty.

You can easily set the desired size of the poster (a1 by default) and the number of columns (2 by default).

Licensing
---------

The poster template is licensed under CC BY 4.0 International License. See LICENSE for the full license text.
