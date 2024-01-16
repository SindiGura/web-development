#!/usr/bin/perl
use strict;
use warnings;
use CGI qw(:standard);

print header(-type => 'text/html', -charset => 'utf-8');
print start_html(
    -title => 'My First Perl Program',
    -style => {
        -code => '
            body {
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
                background-color: #f0fcfc;
            }

            h1 {
                font-family: \'Pacifico\', cursive;
                font-size: 3em;
                color: #008080;
            }
        '
    }
);

print '<h1>This is my first Perl program</h1>';

print end_html();
