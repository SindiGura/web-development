#!/usr/bin/perl -wT
use strict;
use warnings;
use CGI qw(:standard);
use CGI::Carp qw(warningsToBrowser fatalsToBrowser);
use File::Basename;

$CGI::POST_MAX = 102400000 * 50000000;

my $safe_filename_characters = "a-zA-Z0-9_.-";
my $upload_dir = "../lab07/images/";  # Update the path to your upload directory
my $query = new CGI;
my $photo = $query->param("photo");  # Update the parameter name to match your HTML form

print header(-type => 'text/html', -charset => 'utf-8');
print start_html(
    -title => 'Registration Result',
    -head  => Link({-rel => 'stylesheet', -type => 'text/css', -href => '../lab07/styles07.css'}),
);



my $filename;

if (!$photo) {
    print "<h2>Error:</h2>There was a problem uploading your picture (try a smaller file).";
    exit;
}

my ($name, $path, $extension) = fileparse($photo, '\..*');
$filename = $name . $extension;
$filename =~ tr/ /_/;
$filename =~ s/[^$safe_filename_characters]//g;

if ($filename =~ /^([$safe_filename_characters]+)$/) {
    $filename = $1;
} else {
    die "Filename contains invalid characters";
}

my $upload_filehandle = $query->upload("photo");

open(UPLOADFILE, ">$upload_dir/$filename") or die "$!";
binmode UPLOADFILE;

while (<$upload_filehandle>) {
    print UPLOADFILE;
}

close UPLOADFILE;

chmod 0755, "$upload_dir/$filename" or die "Failed to change permissions: $!";

# Retrieve other variables from the HTML form
my $firstName    = $query->param("firstName");
my $lastName     = $query->param("lastName");
my $street       = $query->param("street");
my $city         = $query->param("city");
my $postalCode   = $query->param("postalCode");
my $province     = $query->param("province");
my $phoneNumber  = $query->param("phoneNumber");
my $email        = $query->param("email");

print <<END_HTML;
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>Thanks!</title>
</head>
<body>
    <p>Thank you!</p>
    <p><img src="/upload/$filename" alt="Uploaded picture" /></p>

    <!-- Display other variables -->
    <p>First Name: $firstName</p>
    <p>Last Name: $lastName</p>
    <p>Street: $street</p>
    <p>City: $city</p>
    <p>Postal Code: $postalCode</p>
    <p>Province: $province</p>
    <p>Phone Number: $phoneNumber</p>
    <p>Email Address: $email</p>
</body>
</html>
END_HTML

print end_html();;
