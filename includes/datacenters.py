#!/usr/bin/env python
# Functions to draw and mark Azure Regions on the global map...

"""
Copyright (c) 2016, Marcelo Leal
Description: The power is in the terminal...
License: MIT (see LICENSE.txt file for details)
"""

import sys
from unicurses import *
from maps import *

#DC Coordinates (row x col)...
dc_coords = {
             'brazilsouth':[9,18], \
             'southcentralus':[20,39], \
             'northcentralus':[16,45], \
             'westcentralus':[16,30], \
             'eastus':[19,46], \
             'eastus2':[18,49], \
             'centralus':[14,41], \
             'westus':[17,24], \
             'westus2':[15,25], \
             'canadacentral':[14,50], \
             'canadaeast':[13,57], \
             'northeurope':[12,1], \
             'uksouth':[13,2], \
             'ukwest':[12,4], \
             'westeurope':[12,8], \
             'francecentral':[14,6], \
             'francesouth':[15,7], \
             'germanynortheast':[12,15], \
             'germanycentral':[13,14], \
             'eastasia':[20,64], \
             'southeastasia':[24,60], \
             'japaneast':[15,81], \
             'japanwest':[16,79], \
             'westindia':[20,43], \
             'centralindia':[21,46], \
             'southindia':[23,47], \
             'chinaeast':[18,70], \
             'chinanorth':[14,67], \
             'koreacentral':[15,73], \
             'koreasouth':[17,74], \
             'chinanorth2':[14,69], \
             'australiaeast':[8,33], \
             'australiacentral':[9,31], \
             'australiasoutheast':[10,27]
};

#SYMBOL
dc_symbol = u"\u2588";

#Do the work...
def do_dcmark(window, coords, cor=11):
	if sys.version_info.major >= 3:
		#In Python +3 we can print in unicode a nice and bright block out-of-the-box!
		wmove(window, coords[0], coords[1]); waddstr(window, dc_symbol, color_pair(cor) + A_BOLD);
	else:
		wmove(window, coords[0], coords[1]); waddstr(window, dc_symbol.encode("utf-8"), color_pair(cor) + A_BOLD);

#Mark Datacenters on world map...
def mark_datacenters_map(window, continent):
	if (continent == "southamerica"):
		do_dcmark(window, dc_coords['brazilsouth']);
	if (continent == "northandcentralamerica"):
		do_dcmark(window, dc_coords['southcentralus']);
		do_dcmark(window, dc_coords['northcentralus']);
		do_dcmark(window, dc_coords['westcentralus']);
		do_dcmark(window, dc_coords['eastus']);
		do_dcmark(window, dc_coords['eastus2']);
		do_dcmark(window, dc_coords['centralus']);
		do_dcmark(window, dc_coords['westus']);
		do_dcmark(window, dc_coords['westus2']);
		do_dcmark(window, dc_coords['canadacentral']);
		do_dcmark(window, dc_coords['canadaeast']);
	if (continent == "europeandasia"):
		do_dcmark(window, dc_coords['northeurope']);
		do_dcmark(window, dc_coords['uksouth']);
		do_dcmark(window, dc_coords['ukwest']);
		do_dcmark(window, dc_coords['westeurope']);
		do_dcmark(window, dc_coords['francecentral']);
		do_dcmark(window, dc_coords['francesouth']);
		do_dcmark(window, dc_coords['germanynortheast']);
		do_dcmark(window, dc_coords['germanycentral']);
		do_dcmark(window, dc_coords['eastasia']);
		do_dcmark(window, dc_coords['southeastasia']);
		do_dcmark(window, dc_coords['japaneast']);
		do_dcmark(window, dc_coords['japanwest']);
		do_dcmark(window, dc_coords['centralindia']);
		do_dcmark(window, dc_coords['westindia']);
		do_dcmark(window, dc_coords['southindia']);
		do_dcmark(window, dc_coords['chinaeast']);
		do_dcmark(window, dc_coords['chinanorth']);
		do_dcmark(window, dc_coords['chinanorth2']);
		do_dcmark(window, dc_coords['koreacentral']);
		do_dcmark(window, dc_coords['koreasouth']);
	if (continent == "oceania"):
		do_dcmark(window, dc_coords['australiaeast']);
		do_dcmark(window, dc_coords['australiacentral']);
		do_dcmark(window, dc_coords['australiasoutheast']);

#Mark Deployment dc...
def mark_vmss_dc(continent, window_old, old_location, window_new, new_location, dc):
	if (new_location != old_location):
		#Free up some memory...
		wclear(dc); delwin(dc);
		draw_map(window_old, continent);
		mark_datacenters_map(window_old, continent);

	do_dcmark(window_new, dc_coords[new_location], 5);
	dc = derwin(window_new, 3, 3, dc_coords[new_location][0] - 1, dc_coords[new_location][1] - 1);
	#Alternative target mark to highlight DC on map...
	#box(dc, 2, 2);
	box(dc);
	wrefresh(dc);
	return dc;
