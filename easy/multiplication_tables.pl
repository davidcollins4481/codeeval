#!/usr/bin/env perl

use strict;
use warnings;

my ($rows, $columns) = (12,12);

for my $row (1 .. $rows) {
    for my $column (1 .. $columns) {
        my $number = $row * $column;
        my $spaces;

        if ($column > 1) {
            $spaces = " " x (4 - length($number));
        } else {
            $spaces = ""; 
        } 

        print $spaces,$number;
    }
    print "\n";
}
