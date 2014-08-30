#!/usr/bin/env python
import os
import SimpleHTTPServer
import SocketServer
import socket
import urllib2

if os.name != "nt":
    import fcntl
    import struct

    def get_interface_ip(ifname):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915, struct.pack('256s',
                                ifname[:15]))[20:24])

def get_lan_ip():
    ip = socket.gethostbyname(socket.gethostname())
    if ip.startswith("127.") and os.name != "nt":
        interfaces = [
            "eth0",
            "eth1",
            "eth2",
            "wlan0",
            "wlan1",
            "wifi1",
            "ath0",
            "ath1",
            "ppp0",
            ]
        for ifname in interfaces:
            try:
                ip = get_interface_ip(ifname)
                break
            except IOError:
                pass
    return ip

print "\n\n\n\nWelcome To No PENDRIVE initiative Of GDSOL \n\n\n\n"

print "Enter The Directory which You want to List "
print "Example : c:\\program files\\some_directory"
print "          g:\\softwares"
print "          f:\\movies\\some Movie"
print "\n Note: Dont Worry about spaces in the path"

directory=raw_input("Enter The Directory :  ")
try:
	os.chdir(directory)
except OSError:
	print "\n Incorrect Directory path \n\n"
	exit(0)
	
PORT = raw_input("Enter Port Number")
if PORT=='':
	PORT=4000
else:
	PORT=int(PORT)

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", PORT), Handler)

index_1='''  <!doctype html>
<!--[if IE 9]><html class="lt-ie10" lang="en" > <![endif]-->
<html class="no-js" lang="en" data-useragent="Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Foundation Template | Feed</title>

    
    <meta name="description" content="Documentation and reference library for ZURB Foundation. JavaScript, CSS, components, grid and more." />
    
    <meta name="author" content="ZURB, inc. ZURB network also includes zurb.com" />
    <meta name="copyright" content="ZURB, inc. Copyright (c) 2013" />

    <style>
@import url("//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,700italic,400,300,700");
meta.foundation-mq-small {
  font-family: "/only screen and (max-width: 40em)/";
  width: 0em; }

meta.foundation-mq-medium {
  font-family: "/only screen and (min-width:40.063em) and (max-width:64em)/";
  width: 40.063em; }

meta.foundation-mq-large {
  font-family: "/only screen and (min-width:64.063em)/";
  width: 64.063em; }

meta.foundation-mq-xlarge {
  font-family: "/only screen and (min-width:90.063em)/";
  width: 90.063em; }

meta.foundation-mq-xxlarge {
  font-family: "/only screen and (min-width:120.063em)/";
  width: 120.063em; }

*, *:before, *:after {
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box; }

html, body {
  font-size: 100%; }

body {
  background: white;
  color: #222222;
  padding: 0;
  margin: 0;
  font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
  font-weight: normal;
  font-style: normal;
  line-height: 1;
  position: relative;
  cursor: default; }

a:hover {
  cursor: pointer; }

img, object, embed {
  max-width: 100%;
  height: auto; }

object, embed {
  height: 100%; }

img {
  -ms-interpolation-mode: bicubic; }

#map_canvas img, #map_canvas embed, #map_canvas object, .map_canvas img, .map_canvas embed, .map_canvas object {
  max-width: none !important; }

.left {
  float: left !important; }

.right {
  float: right !important; }

.clearfix {
  *zoom: 1; }
  .clearfix:before, .clearfix:after {
    content: " ";
    display: table; }
  .clearfix:after {
    clear: both; }

.text-left {
  text-align: left !important; }

.text-right {
  text-align: right !important; }

.text-center {
  text-align: center !important; }

.text-justify {
  text-align: justify !important; }

.hide {
  display: none; }

.antialiased {
  -webkit-font-smoothing: antialiased; }

img {
  display: inline-block;
  vertical-align: middle; }

textarea {
  height: auto;
  min-height: 50px; }

select {
  width: 100%; }

.row {
  width: 100%;
  margin-left: auto;
  margin-right: auto;
  margin-top: 0;
  margin-bottom: 0;
  max-width: 62.5rem;
  *zoom: 1; }
  .row:before, .row:after {
    content: " ";
    display: table; }
  .row:after {
    clear: both; }
  .row.collapse > .column, .row.collapse > .columns {
    position: relative;
    padding-left: 0;
    padding-right: 0;
    float: left; }
  .row.collapse .row {
    margin-left: 0;
    margin-right: 0; }
  .row .row {
    width: auto;
    margin-left: -0.9375rem;
    margin-right: -0.9375rem;
    margin-top: 0;
    margin-bottom: 0;
    max-width: none;
    *zoom: 1; }
    .row .row:before, .row .row:after {
      content: " ";
      display: table; }
    .row .row:after {
      clear: both; }
    .row .row.collapse {
      width: auto;
      margin: 0;
      max-width: none;
      *zoom: 1; }
      .row .row.collapse:before, .row .row.collapse:after {
        content: " ";
        display: table; }
      .row .row.collapse:after {
        clear: both; }

.column, .columns {
  position: relative;
  padding-left: 0.9375rem;
  padding-right: 0.9375rem;
  width: 100%;
  float: left; }

@media only screen {
  .small-push-1 {
    position: relative;
    left: 8.33333%;
    right: auto; }
  .small-pull-1 {
    position: relative;
    right: 8.33333%;
    left: auto; }
  .small-push-2 {
    position: relative;
    left: 16.66667%;
    right: auto; }
  .small-pull-2 {
    position: relative;
    right: 16.66667%;
    left: auto; }
  .small-push-3 {
    position: relative;
    left: 25%;
    right: auto; }
  .small-pull-3 {
    position: relative;
    right: 25%;
    left: auto; }
  .small-push-4 {
    position: relative;
    left: 33.33333%;
    right: auto; }
  .small-pull-4 {
    position: relative;
    right: 33.33333%;
    left: auto; }
  .small-push-5 {
    position: relative;
    left: 41.66667%;
    right: auto; }
  .small-pull-5 {
    position: relative;
    right: 41.66667%;
    left: auto; }
  .small-push-6 {
    position: relative;
    left: 50%;
    right: auto; }
  .small-pull-6 {
    position: relative;
    right: 50%;
    left: auto; }
  .small-push-7 {
    position: relative;
    left: 58.33333%;
    right: auto; }
  .small-pull-7 {
    position: relative;
    right: 58.33333%;
    left: auto; }
  .small-push-8 {
    position: relative;
    left: 66.66667%;
    right: auto; }
  .small-pull-8 {
    position: relative;
    right: 66.66667%;
    left: auto; }
  .small-push-9 {
    position: relative;
    left: 75%;
    right: auto; }
  .small-pull-9 {
    position: relative;
    right: 75%;
    left: auto; }
  .small-push-10 {
    position: relative;
    left: 83.33333%;
    right: auto; }
  .small-pull-10 {
    position: relative;
    right: 83.33333%;
    left: auto; }
  .small-push-11 {
    position: relative;
    left: 91.66667%;
    right: auto; }
  .small-pull-11 {
    position: relative;
    right: 91.66667%;
    left: auto; }
  .column, .columns {
    position: relative;
    padding-left: 0.9375rem;
    padding-right: 0.9375rem;
    float: left; }
  .small-1 {
    position: relative;
    width: 8.33333%; }
  .small-2 {
    position: relative;
    width: 16.66667%; }
  .small-3 {
    position: relative;
    width: 25%; }
  .small-4 {
    position: relative;
    width: 33.33333%; }
  .small-5 {
    position: relative;
    width: 41.66667%; }
  .small-6 {
    position: relative;
    width: 50%; }
  .small-7 {
    position: relative;
    width: 58.33333%; }
  .small-8 {
    position: relative;
    width: 66.66667%; }
  .small-9 {
    position: relative;
    width: 75%; }
  .small-10 {
    position: relative;
    width: 83.33333%; }
  .small-11 {
    position: relative;
    width: 91.66667%; }
  .small-12 {
    position: relative;
    width: 100%; }
  .small-offset-0 {
    position: relative;
    margin-left: 0%; }
  .small-offset-1 {
    position: relative;
    margin-left: 8.33333%; }
  .small-offset-2 {
    position: relative;
    margin-left: 16.66667%; }
  .small-offset-3 {
    position: relative;
    margin-left: 25%; }
  .small-offset-4 {
    position: relative;
    margin-left: 33.33333%; }
  .small-offset-5 {
    position: relative;
    margin-left: 41.66667%; }
  .small-offset-6 {
    position: relative;
    margin-left: 50%; }
  .small-offset-7 {
    position: relative;
    margin-left: 58.33333%; }
  .small-offset-8 {
    position: relative;
    margin-left: 66.66667%; }
  .small-offset-9 {
    position: relative;
    margin-left: 75%; }
  .small-offset-10 {
    position: relative;
    margin-left: 83.33333%; }
  [class*="column"] + [class*="column"]:last-child {
    float: right; }
  [class*="column"] + [class*="column"].end {
    float: left; }
  .column.small-centered, .columns.small-centered {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    float: none !important; }
  .column.small-uncentered, .columns.small-uncentered {
    margin-left: 0;
    margin-right: 0;
    float: left !important; }
  .column.small-uncentered.opposite, .columns.small-uncentered.opposite {
    float: right !important; } }

@media only screen and (min-width:40.063em) {
  .medium-push-1 {
    position: relative;
    left: 8.33333%;
    right: auto; }
  .medium-pull-1 {
    position: relative;
    right: 8.33333%;
    left: auto; }
  .medium-push-2 {
    position: relative;
    left: 16.66667%;
    right: auto; }
  .medium-pull-2 {
    position: relative;
    right: 16.66667%;
    left: auto; }
  .medium-push-3 {
    position: relative;
    left: 25%;
    right: auto; }
  .medium-pull-3 {
    position: relative;
    right: 25%;
    left: auto; }
  .medium-push-4 {
    position: relative;
    left: 33.33333%;
    right: auto; }
  .medium-pull-4 {
    position: relative;
    right: 33.33333%;
    left: auto; }
  .medium-push-5 {
    position: relative;
    left: 41.66667%;
    right: auto; }
  .medium-pull-5 {
    position: relative;
    right: 41.66667%;
    left: auto; }
  .medium-push-6 {
    position: relative;
    left: 50%;
    right: auto; }
  .medium-pull-6 {
    position: relative;
    right: 50%;
    left: auto; }
  .medium-push-7 {
    position: relative;
    left: 58.33333%;
    right: auto; }
  .medium-pull-7 {
    position: relative;
    right: 58.33333%;
    left: auto; }
  .medium-push-8 {
    position: relative;
    left: 66.66667%;
    right: auto; }
  .medium-pull-8 {
    position: relative;
    right: 66.66667%;
    left: auto; }
  .medium-push-9 {
    position: relative;
    left: 75%;
    right: auto; }
  .medium-pull-9 {
    position: relative;
    right: 75%;
    left: auto; }
  .medium-push-10 {
    position: relative;
    left: 83.33333%;
    right: auto; }
  .medium-pull-10 {
    position: relative;
    right: 83.33333%;
    left: auto; }
  .medium-push-11 {
    position: relative;
    left: 91.66667%;
    right: auto; }
  .medium-pull-11 {
    position: relative;
    right: 91.66667%;
    left: auto; }
  .column, .columns {
    position: relative;
    padding-left: 0.9375rem;
    padding-right: 0.9375rem;
    float: left; }
  .medium-1 {
    position: relative;
    width: 8.33333%; }
  .medium-2 {
    position: relative;
    width: 16.66667%; }
  .medium-3 {
    position: relative;
    width: 25%; }
  .medium-4 {
    position: relative;
    width: 33.33333%; }
  .medium-5 {
    position: relative;
    width: 41.66667%; }
  .medium-6 {
    position: relative;
    width: 50%; }
  .medium-7 {
    position: relative;
    width: 58.33333%; }
  .medium-8 {
    position: relative;
    width: 66.66667%; }
  .medium-9 {
    position: relative;
    width: 75%; }
  .medium-10 {
    position: relative;
    width: 83.33333%; }
  .medium-11 {
    position: relative;
    width: 91.66667%; }
  .medium-12 {
    position: relative;
    width: 100%; }
  .medium-offset-0 {
    position: relative;
    margin-left: 0%; }
  .medium-offset-1 {
    position: relative;
    margin-left: 8.33333%; }
  .medium-offset-2 {
    position: relative;
    margin-left: 16.66667%; }
  .medium-offset-3 {
    position: relative;
    margin-left: 25%; }
  .medium-offset-4 {
    position: relative;
    margin-left: 33.33333%; }
  .medium-offset-5 {
    position: relative;
    margin-left: 41.66667%; }
  .medium-offset-6 {
    position: relative;
    margin-left: 50%; }
  .medium-offset-7 {
    position: relative;
    margin-left: 58.33333%; }
  .medium-offset-8 {
    position: relative;
    margin-left: 66.66667%; }
  .medium-offset-9 {
    position: relative;
    margin-left: 75%; }
  .medium-offset-10 {
    position: relative;
    margin-left: 83.33333%; }
  [class*="column"] + [class*="column"]:last-child {
    float: right; }
  [class*="column"] + [class*="column"].end {
    float: left; }
  .column.medium-centered, .columns.medium-centered {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    float: none !important; }
  .column.medium-uncentered, .columns.medium-uncentered {
    margin-left: 0;
    margin-right: 0;
    float: left !important; }
  .column.medium-uncentered.opposite, .columns.medium-uncentered.opposite {
    float: right !important; }
  .push-1 {
    position: relative;
    left: 8.33333%;
    right: auto; }
  .pull-1 {
    position: relative;
    right: 8.33333%;
    left: auto; }
  .push-2 {
    position: relative;
    left: 16.66667%;
    right: auto; }
  .pull-2 {
    position: relative;
    right: 16.66667%;
    left: auto; }
  .push-3 {
    position: relative;
    left: 25%;
    right: auto; }
  .pull-3 {
    position: relative;
    right: 25%;
    left: auto; }
  .push-4 {
    position: relative;
    left: 33.33333%;
    right: auto; }
  .pull-4 {
    position: relative;
    right: 33.33333%;
    left: auto; }
  .push-5 {
    position: relative;
    left: 41.66667%;
    right: auto; }
  .pull-5 {
    position: relative;
    right: 41.66667%;
    left: auto; }
  .push-6 {
    position: relative;
    left: 50%;
    right: auto; }
  .pull-6 {
    position: relative;
    right: 50%;
    left: auto; }
  .push-7 {
    position: relative;
    left: 58.33333%;
    right: auto; }
  .pull-7 {
    position: relative;
    right: 58.33333%;
    left: auto; }
  .push-8 {
    position: relative;
    left: 66.66667%;
    right: auto; }
  .pull-8 {
    position: relative;
    right: 66.66667%;
    left: auto; }
  .push-9 {
    position: relative;
    left: 75%;
    right: auto; }
  .pull-9 {
    position: relative;
    right: 75%;
    left: auto; }
  .push-10 {
    position: relative;
    left: 83.33333%;
    right: auto; }
  .pull-10 {
    position: relative;
    right: 83.33333%;
    left: auto; }
  .push-11 {
    position: relative;
    left: 91.66667%;
    right: auto; }
  .pull-11 {
    position: relative;
    right: 91.66667%;
    left: auto; } }

@media only screen and (min-width:64.063em) {
  .large-push-1 {
    position: relative;
    left: 8.33333%;
    right: auto; }
  .large-pull-1 {
    position: relative;
    right: 8.33333%;
    left: auto; }
  .large-push-2 {
    position: relative;
    left: 16.66667%;
    right: auto; }
  .large-pull-2 {
    position: relative;
    right: 16.66667%;
    left: auto; }
  .large-push-3 {
    position: relative;
    left: 25%;
    right: auto; }
  .large-pull-3 {
    position: relative;
    right: 25%;
    left: auto; }
  .large-push-4 {
    position: relative;
    left: 33.33333%;
    right: auto; }
  .large-pull-4 {
    position: relative;
    right: 33.33333%;
    left: auto; }
  .large-push-5 {
    position: relative;
    left: 41.66667%;
    right: auto; }
  .large-pull-5 {
    position: relative;
    right: 41.66667%;
    left: auto; }
  .large-push-6 {
    position: relative;
    left: 50%;
    right: auto; }
  .large-pull-6 {
    position: relative;
    right: 50%;
    left: auto; }
  .large-push-7 {
    position: relative;
    left: 58.33333%;
    right: auto; }
  .large-pull-7 {
    position: relative;
    right: 58.33333%;
    left: auto; }
  .large-push-8 {
    position: relative;
    left: 66.66667%;
    right: auto; }
  .large-pull-8 {
    position: relative;
    right: 66.66667%;
    left: auto; }
  .large-push-9 {
    position: relative;
    left: 75%;
    right: auto; }
  .large-pull-9 {
    position: relative;
    right: 75%;
    left: auto; }
  .large-push-10 {
    position: relative;
    left: 83.33333%;
    right: auto; }
  .large-pull-10 {
    position: relative;
    right: 83.33333%;
    left: auto; }
  .large-push-11 {
    position: relative;
    left: 91.66667%;
    right: auto; }
  .large-pull-11 {
    position: relative;
    right: 91.66667%;
    left: auto; }
  .column, .columns {
    position: relative;
    padding-left: 0.9375rem;
    padding-right: 0.9375rem;
    float: left; }
  .large-1 {
    position: relative;
    width: 8.33333%; }
  .large-2 {
    position: relative;
    width: 16.66667%; }
  .large-3 {
    position: relative;
    width: 25%; }
  .large-4 {
    position: relative;
    width: 33.33333%; }
  .large-5 {
    position: relative;
    width: 41.66667%; }
  .large-6 {
    position: relative;
    width: 50%; }
  .large-7 {
    position: relative;
    width: 58.33333%; }
  .large-8 {
    position: relative;
    width: 66.66667%; }
  .large-9 {
    position: relative;
    width: 75%; }
  .large-10 {
    position: relative;
    width: 83.33333%; }
  .large-11 {
    position: relative;
    width: 91.66667%; }
  .large-12 {
    position: relative;
    width: 100%; }
  .large-offset-0 {
    position: relative;
    margin-left: 0%; }
  .large-offset-1 {
    position: relative;
    margin-left: 8.33333%; }
  .large-offset-2 {
    position: relative;
    margin-left: 16.66667%; }
  .large-offset-3 {
    position: relative;
    margin-left: 25%; }
  .large-offset-4 {
    position: relative;
    margin-left: 33.33333%; }
  .large-offset-5 {
    position: relative;
    margin-left: 41.66667%; }
  .large-offset-6 {
    position: relative;
    margin-left: 50%; }
  .large-offset-7 {
    position: relative;
    margin-left: 58.33333%; }
  .large-offset-8 {
    position: relative;
    margin-left: 66.66667%; }
  .large-offset-9 {
    position: relative;
    margin-left: 75%; }
  .large-offset-10 {
    position: relative;
    margin-left: 83.33333%; }
  [class*="column"] + [class*="column"]:last-child {
    float: right; }
  [class*="column"] + [class*="column"].end {
    float: left; }
  .column.large-centered, .columns.large-centered {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    float: none !important; }
  .column.large-uncentered, .columns.large-uncentered {
    margin-left: 0;
    margin-right: 0;
    float: left !important; }
  .column.large-uncentered.opposite, .columns.large-uncentered.opposite {
    float: right !important; } }

@media only screen and (min-width:90.063em) {
  .xlarge-push-1 {
    position: relative;
    left: 8.33333%;
    right: auto; }
  .xlarge-pull-1 {
    position: relative;
    right: 8.33333%;
    left: auto; }
  .xlarge-push-2 {
    position: relative;
    left: 16.66667%;
    right: auto; }
  .xlarge-pull-2 {
    position: relative;
    right: 16.66667%;
    left: auto; }
  .xlarge-push-3 {
    position: relative;
    left: 25%;
    right: auto; }
  .xlarge-pull-3 {
    position: relative;
    right: 25%;
    left: auto; }
  .xlarge-push-4 {
    position: relative;
    left: 33.33333%;
    right: auto; }
  .xlarge-pull-4 {
    position: relative;
    right: 33.33333%;
    left: auto; }
  .xlarge-push-5 {
    position: relative;
    left: 41.66667%;
    right: auto; }
  .xlarge-pull-5 {
    position: relative;
    right: 41.66667%;
    left: auto; }
  .xlarge-push-6 {
    position: relative;
    left: 50%;
    right: auto; }
  .xlarge-pull-6 {
    position: relative;
    right: 50%;
    left: auto; }
  .xlarge-push-7 {
    position: relative;
    left: 58.33333%;
    right: auto; }
  .xlarge-pull-7 {
    position: relative;
    right: 58.33333%;
    left: auto; }
  .xlarge-push-8 {
    position: relative;
    left: 66.66667%;
    right: auto; }
  .xlarge-pull-8 {
    position: relative;
    right: 66.66667%;
    left: auto; }
  .xlarge-push-9 {
    position: relative;
    left: 75%;
    right: auto; }
  .xlarge-pull-9 {
    position: relative;
    right: 75%;
    left: auto; }
  .xlarge-push-10 {
    position: relative;
    left: 83.33333%;
    right: auto; }
  .xlarge-pull-10 {
    position: relative;
    right: 83.33333%;
    left: auto; }
  .xlarge-push-11 {
    position: relative;
    left: 91.66667%;
    right: auto; }
  .xlarge-pull-11 {
    position: relative;
    right: 91.66667%;
    left: auto; }
  .column, .columns {
    position: relative;
    padding-left: 0.9375rem;
    padding-right: 0.9375rem;
    float: left; }
  .xlarge-1 {
    position: relative;
    width: 8.33333%; }
  .xlarge-2 {
    position: relative;
    width: 16.66667%; }
  .xlarge-3 {
    position: relative;
    width: 25%; }
  .xlarge-4 {
    position: relative;
    width: 33.33333%; }
  .xlarge-5 {
    position: relative;
    width: 41.66667%; }
  .xlarge-6 {
    position: relative;
    width: 50%; }
  .xlarge-7 {
    position: relative;
    width: 58.33333%; }
  .xlarge-8 {
    position: relative;
    width: 66.66667%; }
  .xlarge-9 {
    position: relative;
    width: 75%; }
  .xlarge-10 {
    position: relative;
    width: 83.33333%; }
  .xlarge-11 {
    position: relative;
    width: 91.66667%; }
  .xlarge-12 {
    position: relative;
    width: 100%; }
  .xlarge-offset-0 {
    position: relative;
    margin-left: 0%; }
  .xlarge-offset-1 {
    position: relative;
    margin-left: 8.33333%; }
  .xlarge-offset-2 {
    position: relative;
    margin-left: 16.66667%; }
  .xlarge-offset-3 {
    position: relative;
    margin-left: 25%; }
  .xlarge-offset-4 {
    position: relative;
    margin-left: 33.33333%; }
  .xlarge-offset-5 {
    position: relative;
    margin-left: 41.66667%; }
  .xlarge-offset-6 {
    position: relative;
    margin-left: 50%; }
  .xlarge-offset-7 {
    position: relative;
    margin-left: 58.33333%; }
  .xlarge-offset-8 {
    position: relative;
    margin-left: 66.66667%; }
  .xlarge-offset-9 {
    position: relative;
    margin-left: 75%; }
  .xlarge-offset-10 {
    position: relative;
    margin-left: 83.33333%; }
  [class*="column"] + [class*="column"]:last-child {
    float: right; }
  [class*="column"] + [class*="column"].end {
    float: left; }
  .column.xlarge-centered, .columns.xlarge-centered {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    float: none !important; }
  .column.xlarge-uncentered, .columns.xlarge-uncentered {
    margin-left: 0;
    margin-right: 0;
    float: left !important; }
  .column.xlarge-uncentered.opposite, .columns.xlarge-uncentered.opposite {
    float: right !important; } }

@media only screen and (min-width:120.063em) {
  .xxlarge-push-1 {
    position: relative;
    left: 8.33333%;
    right: auto; }
  .xxlarge-pull-1 {
    position: relative;
    right: 8.33333%;
    left: auto; }
  .xxlarge-push-2 {
    position: relative;
    left: 16.66667%;
    right: auto; }
  .xxlarge-pull-2 {
    position: relative;
    right: 16.66667%;
    left: auto; }
  .xxlarge-push-3 {
    position: relative;
    left: 25%;
    right: auto; }
  .xxlarge-pull-3 {
    position: relative;
    right: 25%;
    left: auto; }
  .xxlarge-push-4 {
    position: relative;
    left: 33.33333%;
    right: auto; }
  .xxlarge-pull-4 {
    position: relative;
    right: 33.33333%;
    left: auto; }
  .xxlarge-push-5 {
    position: relative;
    left: 41.66667%;
    right: auto; }
  .xxlarge-pull-5 {
    position: relative;
    right: 41.66667%;
    left: auto; }
  .xxlarge-push-6 {
    position: relative;
    left: 50%;
    right: auto; }
  .xxlarge-pull-6 {
    position: relative;
    right: 50%;
    left: auto; }
  .xxlarge-push-7 {
    position: relative;
    left: 58.33333%;
    right: auto; }
  .xxlarge-pull-7 {
    position: relative;
    right: 58.33333%;
    left: auto; }
  .xxlarge-push-8 {
    position: relative;
    left: 66.66667%;
    right: auto; }
  .xxlarge-pull-8 {
    position: relative;
    right: 66.66667%;
    left: auto; }
  .xxlarge-push-9 {
    position: relative;
    left: 75%;
    right: auto; }
  .xxlarge-pull-9 {
    position: relative;
    right: 75%;
    left: auto; }
  .xxlarge-push-10 {
    position: relative;
    left: 83.33333%;
    right: auto; }
  .xxlarge-pull-10 {
    position: relative;
    right: 83.33333%;
    left: auto; }
  .xxlarge-push-11 {
    position: relative;
    left: 91.66667%;
    right: auto; }
  .xxlarge-pull-11 {
    position: relative;
    right: 91.66667%;
    left: auto; }
  .column, .columns {
    position: relative;
    padding-left: 0.9375rem;
    padding-right: 0.9375rem;
    float: left; }
  .xxlarge-1 {
    position: relative;
    width: 8.33333%; }
  .xxlarge-2 {
    position: relative;
    width: 16.66667%; }
  .xxlarge-3 {
    position: relative;
    width: 25%; }
  .xxlarge-4 {
    position: relative;
    width: 33.33333%; }
  .xxlarge-5 {
    position: relative;
    width: 41.66667%; }
  .xxlarge-6 {
    position: relative;
    width: 50%; }
  .xxlarge-7 {
    position: relative;
    width: 58.33333%; }
  .xxlarge-8 {
    position: relative;
    width: 66.66667%; }
  .xxlarge-9 {
    position: relative;
    width: 75%; }
  .xxlarge-10 {
    position: relative;
    width: 83.33333%; }
  .xxlarge-11 {
    position: relative;
    width: 91.66667%; }
  .xxlarge-12 {
    position: relative;
    width: 100%; }
  .xxlarge-offset-0 {
    position: relative;
    margin-left: 0%; }
  .xxlarge-offset-1 {
    position: relative;
    margin-left: 8.33333%; }
  .xxlarge-offset-2 {
    position: relative;
    margin-left: 16.66667%; }
  .xxlarge-offset-3 {
    position: relative;
    margin-left: 25%; }
  .xxlarge-offset-4 {
    position: relative;
    margin-left: 33.33333%; }
  .xxlarge-offset-5 {
    position: relative;
    margin-left: 41.66667%; }
  .xxlarge-offset-6 {
    position: relative;
    margin-left: 50%; }
  .xxlarge-offset-7 {
    position: relative;
    margin-left: 58.33333%; }
  .xxlarge-offset-8 {
    position: relative;
    margin-left: 66.66667%; }
  .xxlarge-offset-9 {
    position: relative;
    margin-left: 75%; }
  .xxlarge-offset-10 {
    position: relative;
    margin-left: 83.33333%; }
  [class*="column"] + [class*="column"]:last-child {
    float: right; }
  [class*="column"] + [class*="column"].end {
    float: left; }
  .column.xxlarge-centered, .columns.xxlarge-centered {
    position: relative;
    margin-left: auto;
    margin-right: auto;
    float: none !important; }
  .column.xxlarge-uncentered, .columns.xxlarge-uncentered {
    margin-left: 0;
    margin-right: 0;
    float: left !important; }
  .column.xxlarge-uncentered.opposite, .columns.xxlarge-uncentered.opposite {
    float: right !important; } }

.accordion {
  *zoom: 1;
  margin-bottom: 0; }
  .accordion:before, .accordion:after {
    content: " ";
    display: table; }
  .accordion:after {
    clear: both; }
  .accordion dd {
    display: block;
    margin-bottom: 0 !important; }
    .accordion dd.active a {
      background: #e7e7e7; }
    .accordion dd > a {
      background: #efefef;
      color: #222222;
      padding: 1rem;
      display: block;
      font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
      font-size: 1rem; }
      .accordion dd > a:hover {
        background: #e2e2e2; }
  .accordion .content {
    display: none;
    padding: 0.9375rem; }
    .accordion .content.active {
      display: block;
      background: white; }

.alert-box {
  border-style: solid;
  border-width: 1px;
  display: block;
  font-weight: normal;
  margin-bottom: 1.25rem;
  position: relative;
  padding: 0.875rem 1.5rem 0.875rem 0.875rem;
  font-size: 0.8125rem;
  background-color: #008cba;
  border-color: #007ba1;
  color: white; }
  .alert-box .close {
    font-size: 1.375rem;
    padding: 9px 6px 4px;
    line-height: 0;
    position: absolute;
    top: 50%;
    margin-top: -0.6875rem;
    right: 0.25rem;
    color: #333333;
    opacity: 0.3; }
    .alert-box .close:hover, .alert-box .close:focus {
      opacity: 0.5; }
  .alert-box.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }
  .alert-box.round {
    -webkit-border-radius: 1000px;
    border-radius: 1000px; }
  .alert-box.success {
    background-color: #43ac6a;
    border-color: #3c9a5e;
    color: white; }
  .alert-box.alert {
    background-color: #f04124;
    border-color: #ea2d10;
    color: white; }
  .alert-box.secondary {
    background-color: #e7e7e7;
    border-color: #dadada;
    color: #4e4e4e; }
  .alert-box.warning {
    background-color: #f08a24;
    border-color: #ea7d10;
    color: white; }
  .alert-box.info {
    background-color: #a0d3e8;
    border-color: #8bcae3;
    color: #4e4e4e; }

[class*="block-grid-"] {
  display: block;
  padding: 0;
  margin: 0 -0.625rem;
  *zoom: 1; }
  [class*="block-grid-"]:before, [class*="block-grid-"]:after {
    content: " ";
    display: table; }
  [class*="block-grid-"]:after {
    clear: both; }
  [class*="block-grid-"] > li {
    display: inline;
    height: auto;
    float: left;
    padding: 0 0.625rem 1.25rem; }

@media only screen {
  .small-block-grid-1 > li {
    width: 100%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-1 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-1 > li:nth-of-type(1n+1) {
      clear: both; }
  .small-block-grid-2 > li {
    width: 50%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-2 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-2 > li:nth-of-type(2n+1) {
      clear: both; }
  .small-block-grid-3 > li {
    width: 33.33333%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-3 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-3 > li:nth-of-type(3n+1) {
      clear: both; }
  .small-block-grid-4 > li {
    width: 25%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-4 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-4 > li:nth-of-type(4n+1) {
      clear: both; }
  .small-block-grid-5 > li {
    width: 20%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-5 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-5 > li:nth-of-type(5n+1) {
      clear: both; }
  .small-block-grid-6 > li {
    width: 16.66667%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-6 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-6 > li:nth-of-type(6n+1) {
      clear: both; }
  .small-block-grid-7 > li {
    width: 14.28571%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-7 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-7 > li:nth-of-type(7n+1) {
      clear: both; }
  .small-block-grid-8 > li {
    width: 12.5%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-8 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-8 > li:nth-of-type(8n+1) {
      clear: both; }
  .small-block-grid-9 > li {
    width: 11.11111%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-9 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-9 > li:nth-of-type(9n+1) {
      clear: both; }
  .small-block-grid-10 > li {
    width: 10%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-10 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-10 > li:nth-of-type(10n+1) {
      clear: both; }
  .small-block-grid-11 > li {
    width: 9.09091%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-11 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-11 > li:nth-of-type(11n+1) {
      clear: both; }
  .small-block-grid-12 > li {
    width: 8.33333%;
    padding: 0 0.625rem 1.25rem; }
    .small-block-grid-12 > li:nth-of-type(n) {
      clear: none; }
    .small-block-grid-12 > li:nth-of-type(12n+1) {
      clear: both; } }

@media only screen and (min-width:40.063em) {
  .medium-block-grid-1 > li {
    width: 100%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-1 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-1 > li:nth-of-type(1n+1) {
      clear: both; }
  .medium-block-grid-2 > li {
    width: 50%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-2 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-2 > li:nth-of-type(2n+1) {
      clear: both; }
  .medium-block-grid-3 > li {
    width: 33.33333%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-3 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-3 > li:nth-of-type(3n+1) {
      clear: both; }
  .medium-block-grid-4 > li {
    width: 25%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-4 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-4 > li:nth-of-type(4n+1) {
      clear: both; }
  .medium-block-grid-5 > li {
    width: 20%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-5 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-5 > li:nth-of-type(5n+1) {
      clear: both; }
  .medium-block-grid-6 > li {
    width: 16.66667%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-6 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-6 > li:nth-of-type(6n+1) {
      clear: both; }
  .medium-block-grid-7 > li {
    width: 14.28571%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-7 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-7 > li:nth-of-type(7n+1) {
      clear: both; }
  .medium-block-grid-8 > li {
    width: 12.5%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-8 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-8 > li:nth-of-type(8n+1) {
      clear: both; }
  .medium-block-grid-9 > li {
    width: 11.11111%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-9 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-9 > li:nth-of-type(9n+1) {
      clear: both; }
  .medium-block-grid-10 > li {
    width: 10%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-10 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-10 > li:nth-of-type(10n+1) {
      clear: both; }
  .medium-block-grid-11 > li {
    width: 9.09091%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-11 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-11 > li:nth-of-type(11n+1) {
      clear: both; }
  .medium-block-grid-12 > li {
    width: 8.33333%;
    padding: 0 0.625rem 1.25rem; }
    .medium-block-grid-12 > li:nth-of-type(n) {
      clear: none; }
    .medium-block-grid-12 > li:nth-of-type(12n+1) {
      clear: both; } }

@media only screen and (min-width:64.063em) {
  .large-block-grid-1 > li {
    width: 100%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-1 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-1 > li:nth-of-type(1n+1) {
      clear: both; }
  .large-block-grid-2 > li {
    width: 50%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-2 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-2 > li:nth-of-type(2n+1) {
      clear: both; }
  .large-block-grid-3 > li {
    width: 33.33333%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-3 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-3 > li:nth-of-type(3n+1) {
      clear: both; }
  .large-block-grid-4 > li {
    width: 25%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-4 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-4 > li:nth-of-type(4n+1) {
      clear: both; }
  .large-block-grid-5 > li {
    width: 20%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-5 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-5 > li:nth-of-type(5n+1) {
      clear: both; }
  .large-block-grid-6 > li {
    width: 16.66667%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-6 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-6 > li:nth-of-type(6n+1) {
      clear: both; }
  .large-block-grid-7 > li {
    width: 14.28571%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-7 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-7 > li:nth-of-type(7n+1) {
      clear: both; }
  .large-block-grid-8 > li {
    width: 12.5%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-8 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-8 > li:nth-of-type(8n+1) {
      clear: both; }
  .large-block-grid-9 > li {
    width: 11.11111%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-9 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-9 > li:nth-of-type(9n+1) {
      clear: both; }
  .large-block-grid-10 > li {
    width: 10%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-10 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-10 > li:nth-of-type(10n+1) {
      clear: both; }
  .large-block-grid-11 > li {
    width: 9.09091%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-11 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-11 > li:nth-of-type(11n+1) {
      clear: both; }
  .large-block-grid-12 > li {
    width: 8.33333%;
    padding: 0 0.625rem 1.25rem; }
    .large-block-grid-12 > li:nth-of-type(n) {
      clear: none; }
    .large-block-grid-12 > li:nth-of-type(12n+1) {
      clear: both; } }

.breadcrumbs {
  display: block;
  padding: 0.5625rem 0.875rem 0.5625rem;
  overflow: hidden;
  margin-left: 0;
  list-style: none;
  border-style: solid;
  border-width: 1px;
  background-color: #f4f4f4;
  border-color: #dbdbdb;
  -webkit-border-radius: 3px;
  border-radius: 3px; }
  .breadcrumbs > * {
    margin: 0;
    float: left;
    font-size: 0.6875rem;
    text-transform: uppercase; }
    .breadcrumbs > *:hover a, .breadcrumbs > *:focus a {
      text-decoration: underline; }
    .breadcrumbs > * a, .breadcrumbs > * span {
      text-transform: uppercase;
      color: #008cba; }
    .breadcrumbs > *.current {
      cursor: default;
      color: #333333; }
      .breadcrumbs > *.current a {
        cursor: default;
        color: #333333; }
      .breadcrumbs > *.current:hover, .breadcrumbs > *.current:hover a, .breadcrumbs > *.current:focus, .breadcrumbs > *.current:focus a {
        text-decoration: none; }
    .breadcrumbs > *.unavailable {
      color: #999999; }
      .breadcrumbs > *.unavailable a {
        color: #999999; }
      .breadcrumbs > *.unavailable:hover, .breadcrumbs > *.unavailable:hover a, .breadcrumbs > *.unavailable:focus, .breadcrumbs > *.unavailable a:focus {
        text-decoration: none;
        color: #999999;
        cursor: default; }
    .breadcrumbs > *:before {
      content: "/";
      color: #aaaaaa;
      margin: 0 0.75rem;
      position: relative;
      top: 1px; }
    .breadcrumbs > *:first-child:before {
      content: " ";
      margin: 0; }

button, .button {
  cursor: pointer;
  font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
  font-weight: normal;
  line-height: normal;
  margin: 0 0 1.25rem;
  position: relative;
  text-decoration: none;
  text-align: center;
  display: inline-block;
  padding-top: 1rem;
  padding-right: 2rem;
  padding-bottom: 1.0625rem;
  padding-left: 2rem;
  font-size: 1rem;
  /*     @else                            { font-size: $padding - rem-calc(2); } */
  background-color: #008cba;
  border-color: #007ba1;
  color: white;
  -webkit-transition: background-color 300ms ease-out;
  -moz-transition: background-color 300ms ease-out;
  transition: background-color 300ms ease-out;
  padding-top: 1.0625rem;
  padding-bottom: 1rem;
  -webkit-appearance: none;
  border: none;
  font-weight: normal !important; }
  button:hover, button:focus, .button:hover, .button:focus {
    background-color: #007ba1; }
  button:hover, button:focus, .button:hover, .button:focus {
    color: white; }
  button.secondary, .button.secondary {
    background-color: #e7e7e7;
    border-color: #dadada;
    color: #333333; }
    button.secondary:hover, button.secondary:focus, .button.secondary:hover, .button.secondary:focus {
      background-color: #dadada; }
    button.secondary:hover, button.secondary:focus, .button.secondary:hover, .button.secondary:focus {
      color: #333333; }
  button.success, .button.success {
    background-color: #43ac6a;
    border-color: #3c9a5e;
    color: white; }
    button.success:hover, button.success:focus, .button.success:hover, .button.success:focus {
      background-color: #3c9a5e; }
    button.success:hover, button.success:focus, .button.success:hover, .button.success:focus {
      color: white; }
  button.alert, .button.alert {
    background-color: #f04124;
    border-color: #ea2d10;
    color: white; }
    button.alert:hover, button.alert:focus, .button.alert:hover, .button.alert:focus {
      background-color: #ea2d10; }
    button.alert:hover, button.alert:focus, .button.alert:hover, .button.alert:focus {
      color: white; }
  button.large, .button.large {
    padding-top: 1.125rem;
    padding-right: 2.25rem;
    padding-bottom: 1.1875rem;
    padding-left: 2.25rem;
    font-size: 1.25rem;
    /*     @else                            { font-size: $padding - rem-calc(2); } */ }
  button.small, .button.small {
    padding-top: 0.875rem;
    padding-right: 1.75rem;
    padding-bottom: 0.9375rem;
    padding-left: 1.75rem;
    font-size: 0.8125rem;
    /*     @else                            { font-size: $padding - rem-calc(2); } */ }
  button.tiny, .button.tiny {
    padding-top: 0.625rem;
    padding-right: 1.25rem;
    padding-bottom: 0.6875rem;
    padding-left: 1.25rem;
    font-size: 0.6875rem;
    /*     @else                            { font-size: $padding - rem-calc(2); } */ }
  button.expand, .button.expand {
    padding-right: 0;
    padding-left: 0;
    width: 100%; }
  button.left-align, .button.left-align {
    text-align: left;
    text-indent: 0.75rem; }
  button.right-align, .button.right-align {
    text-align: right;
    padding-right: 0.75rem; }
  button.radius, .button.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }
  button.round, .button.round {
    -webkit-border-radius: 1000px;
    border-radius: 1000px; }
  button.disabled, button[disabled], .button.disabled, .button[disabled] {
    background-color: #008cba;
    border-color: #007ba1;
    color: white;
    cursor: default;
    opacity: 0.7;
    -webkit-box-shadow: none;
    box-shadow: none; }
    button.disabled:hover, button.disabled:focus, button[disabled]:hover, button[disabled]:focus, .button.disabled:hover, .button.disabled:focus, .button[disabled]:hover, .button[disabled]:focus {
      background-color: #007ba1; }
    button.disabled:hover, button.disabled:focus, button[disabled]:hover, button[disabled]:focus, .button.disabled:hover, .button.disabled:focus, .button[disabled]:hover, .button[disabled]:focus {
      color: white; }
    button.disabled:hover, button.disabled:focus, button[disabled]:hover, button[disabled]:focus, .button.disabled:hover, .button.disabled:focus, .button[disabled]:hover, .button[disabled]:focus {
      background-color: #008cba; }
    button.disabled.secondary, button[disabled].secondary, .button.disabled.secondary, .button[disabled].secondary {
      background-color: #e7e7e7;
      border-color: #dadada;
      color: #333333;
      cursor: default;
      opacity: 0.7;
      -webkit-box-shadow: none;
      box-shadow: none; }
      button.disabled.secondary:hover, button.disabled.secondary:focus, button[disabled].secondary:hover, button[disabled].secondary:focus, .button.disabled.secondary:hover, .button.disabled.secondary:focus, .button[disabled].secondary:hover, .button[disabled].secondary:focus {
        background-color: #dadada; }
      button.disabled.secondary:hover, button.disabled.secondary:focus, button[disabled].secondary:hover, button[disabled].secondary:focus, .button.disabled.secondary:hover, .button.disabled.secondary:focus, .button[disabled].secondary:hover, .button[disabled].secondary:focus {
        color: #333333; }
      button.disabled.secondary:hover, button.disabled.secondary:focus, button[disabled].secondary:hover, button[disabled].secondary:focus, .button.disabled.secondary:hover, .button.disabled.secondary:focus, .button[disabled].secondary:hover, .button[disabled].secondary:focus {
        background-color: #e7e7e7; }
    button.disabled.success, button[disabled].success, .button.disabled.success, .button[disabled].success {
      background-color: #43ac6a;
      border-color: #3c9a5e;
      color: white;
      cursor: default;
      opacity: 0.7;
      -webkit-box-shadow: none;
      box-shadow: none; }
      button.disabled.success:hover, button.disabled.success:focus, button[disabled].success:hover, button[disabled].success:focus, .button.disabled.success:hover, .button.disabled.success:focus, .button[disabled].success:hover, .button[disabled].success:focus {
        background-color: #3c9a5e; }
      button.disabled.success:hover, button.disabled.success:focus, button[disabled].success:hover, button[disabled].success:focus, .button.disabled.success:hover, .button.disabled.success:focus, .button[disabled].success:hover, .button[disabled].success:focus {
        color: white; }
      button.disabled.success:hover, button.disabled.success:focus, button[disabled].success:hover, button[disabled].success:focus, .button.disabled.success:hover, .button.disabled.success:focus, .button[disabled].success:hover, .button[disabled].success:focus {
        background-color: #43ac6a; }
    button.disabled.alert, button[disabled].alert, .button.disabled.alert, .button[disabled].alert {
      background-color: #f04124;
      border-color: #ea2d10;
      color: white;
      cursor: default;
      opacity: 0.7;
      -webkit-box-shadow: none;
      box-shadow: none; }
      button.disabled.alert:hover, button.disabled.alert:focus, button[disabled].alert:hover, button[disabled].alert:focus, .button.disabled.alert:hover, .button.disabled.alert:focus, .button[disabled].alert:hover, .button[disabled].alert:focus {
        background-color: #ea2d10; }
      button.disabled.alert:hover, button.disabled.alert:focus, button[disabled].alert:hover, button[disabled].alert:focus, .button.disabled.alert:hover, .button.disabled.alert:focus, .button[disabled].alert:hover, .button[disabled].alert:focus {
        color: white; }
      button.disabled.alert:hover, button.disabled.alert:focus, button[disabled].alert:hover, button[disabled].alert:focus, .button.disabled.alert:hover, .button.disabled.alert:focus, .button[disabled].alert:hover, .button[disabled].alert:focus {
        background-color: #f04124; }

@media only screen and (min-width:40.063em) {
  button, .button {
    display: inline-block; } }

.button-group {
  list-style: none;
  margin: 0;
  *zoom: 1; }
  .button-group:before, .button-group:after {
    content: " ";
    display: table; }
  .button-group:after {
    clear: both; }
  .button-group > * {
    margin: 0;
    float: left; }
    .button-group > * > button, .button-group > * .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group > *:first-child {
      margin-left: 0; }
  .button-group.radius > * > button, .button-group.radius > * .button {
    border-right: 1px solid;
    border-color: rgba(255, 255, 255, 0.5); }
  .button-group.radius > *:first-child, .button-group.radius > *:first-child > a, .button-group.radius > *:first-child > button, .button-group.radius > *:first-child > .button {
    -moz-border-radius-bottomleft: 3px;
    -moz-border-radius-topleft: 3px;
    -webkit-border-bottom-left-radius: 3px;
    -webkit-border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    border-top-left-radius: 3px; }
  .button-group.radius > *:last-child, .button-group.radius > *:last-child > a, .button-group.radius > *:last-child > button, .button-group.radius > *:last-child > .button {
    -moz-border-radius-topright: 3px;
    -moz-border-radius-bottomright: 3px;
    -webkit-border-top-right-radius: 3px;
    -webkit-border-bottom-right-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px; }
  .button-group.round > * > button, .button-group.round > * .button {
    border-right: 1px solid;
    border-color: rgba(255, 255, 255, 0.5); }
  .button-group.round > *:first-child, .button-group.round > *:first-child > a, .button-group.round > *:first-child > button, .button-group.round > *:first-child > .button {
    -moz-border-radius-bottomleft: 1000px;
    -moz-border-radius-topleft: 1000px;
    -webkit-border-bottom-left-radius: 1000px;
    -webkit-border-top-left-radius: 1000px;
    border-bottom-left-radius: 1000px;
    border-top-left-radius: 1000px; }
  .button-group.round > *:last-child, .button-group.round > *:last-child > a, .button-group.round > *:last-child > button, .button-group.round > *:last-child > .button {
    -moz-border-radius-topright: 1000px;
    -moz-border-radius-bottomright: 1000px;
    -webkit-border-top-right-radius: 1000px;
    -webkit-border-bottom-right-radius: 1000px;
    border-top-right-radius: 1000px;
    border-bottom-right-radius: 1000px; }
  .button-group.even-2 li {
    width: 50%; }
    .button-group.even-2 li > button, .button-group.even-2 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-2 li button, .button-group.even-2 li .button {
      width: 100%; }
  .button-group.even-3 li {
    width: 33.33333%; }
    .button-group.even-3 li > button, .button-group.even-3 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-3 li button, .button-group.even-3 li .button {
      width: 100%; }
  .button-group.even-4 li {
    width: 25%; }
    .button-group.even-4 li > button, .button-group.even-4 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-4 li button, .button-group.even-4 li .button {
      width: 100%; }
  .button-group.even-5 li {
    width: 20%; }
    .button-group.even-5 li > button, .button-group.even-5 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-5 li button, .button-group.even-5 li .button {
      width: 100%; }
  .button-group.even-6 li {
    width: 16.66667%; }
    .button-group.even-6 li > button, .button-group.even-6 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-6 li button, .button-group.even-6 li .button {
      width: 100%; }
  .button-group.even-7 li {
    width: 14.28571%; }
    .button-group.even-7 li > button, .button-group.even-7 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-7 li button, .button-group.even-7 li .button {
      width: 100%; }
  .button-group.even-8 li {
    width: 12.5%; }
    .button-group.even-8 li > button, .button-group.even-8 li .button {
      border-right: 1px solid;
      border-color: rgba(255, 255, 255, 0.5); }
    .button-group.even-8 li button, .button-group.even-8 li .button {
      width: 100%; }

.button-bar {
  *zoom: 1; }
  .button-bar:before, .button-bar:after {
    content: " ";
    display: table; }
  .button-bar:after {
    clear: both; }
  .button-bar .button-group {
    float: left;
    margin-right: 0.625rem; }
    .button-bar .button-group div {
      overflow: hidden; }

/* Clearing Styles */
[data-clearing] {
  *zoom: 1;
  margin-bottom: 0;
  margin-left: 0;
  list-style: none; }
  [data-clearing]:before, [data-clearing]:after {
    content: " ";
    display: table; }
  [data-clearing]:after {
    clear: both; }
  [data-clearing] li {
    float: left;
    margin-right: 10px; }

.clearing-blackout {
  background: #333333;
  position: fixed;
  width: 100%;
  height: 100%;
  top: 0;
  left: 0;
  z-index: 998; }
  .clearing-blackout .clearing-close {
    display: block; }

.clearing-container {
  position: relative;
  z-index: 998;
  height: 100%;
  overflow: hidden;
  margin: 0; }

.visible-img {
  height: 95%;
  position: relative; }
  .visible-img img {
    position: absolute;
    left: 50%;
    top: 50%;
    margin-left: -50%;
    max-height: 100%;
    max-width: 100%; }

.clearing-caption {
  color: #cccccc;
  font-size: 0.875em;
  line-height: 1.3;
  margin-bottom: 0;
  text-align: center;
  bottom: 0;
  background: #333333;
  width: 100%;
  padding: 10px 30px 20px;
  position: absolute;
  left: 0; }

.clearing-close {
  z-index: 999;
  padding-left: 20px;
  padding-top: 10px;
  font-size: 30px;
  line-height: 1;
  color: #cccccc;
  display: none; }
  .clearing-close:hover, .clearing-close:focus {
    color: #cccccc; }

.clearing-assembled .clearing-container {
  height: 100%; }
  .clearing-assembled .clearing-container .carousel > ul {
    display: none; }

.clearing-feature li {
  display: none; }
  .clearing-feature li.clearing-featured-img {
    display: block; }

@media only screen and (min-width:40.063em) {
  .clearing-main-prev, .clearing-main-next {
    position: absolute;
    height: 100%;
    width: 40px;
    top: 0; }
    .clearing-main-prev > span, .clearing-main-next > span {
      position: absolute;
      top: 50%;
      display: block;
      width: 0;
      height: 0;
      border: solid 12px; }
      .clearing-main-prev > span:hover, .clearing-main-next > span:hover {
        opacity: 0.8; }
  .clearing-main-prev {
    left: 0; }
    .clearing-main-prev > span {
      left: 5px;
      border-color: transparent;
      border-right-color: #cccccc; }
  .clearing-main-next {
    right: 0; }
    .clearing-main-next > span {
      border-color: transparent;
      border-left-color: #cccccc; }
  .clearing-main-prev.disabled, .clearing-main-next.disabled {
    opacity: 0.3; }
  .clearing-assembled .clearing-container .carousel {
    background: rgba(51, 51, 51, 0.8);
    height: 120px;
    margin-top: 10px;
    text-align: center; }
    .clearing-assembled .clearing-container .carousel > ul {
      display: inline-block;
      z-index: 999;
      height: 100%;
      position: relative;
      float: none; }
      .clearing-assembled .clearing-container .carousel > ul li {
        display: block;
        width: 120px;
        min-height: inherit;
        float: left;
        overflow: hidden;
        margin-right: 0;
        padding: 0;
        position: relative;
        cursor: pointer;
        opacity: 0.4; }
        .clearing-assembled .clearing-container .carousel > ul li.fix-height img {
          height: 100%;
          max-width: none; }
        .clearing-assembled .clearing-container .carousel > ul li a.th {
          border: none;
          -webkit-box-shadow: none;
          box-shadow: none;
          display: block; }
        .clearing-assembled .clearing-container .carousel > ul li img {
          cursor: pointer !important;
          width: 100% !important; }
        .clearing-assembled .clearing-container .carousel > ul li.visible {
          opacity: 1; }
        .clearing-assembled .clearing-container .carousel > ul li:hover {
          opacity: 0.8; }
  .clearing-assembled .clearing-container .visible-img {
    background: #333333;
    overflow: hidden;
    height: 85%; }
  .clearing-close {
    position: absolute;
    top: 10px;
    right: 20px;
    padding-left: 0;
    padding-top: 0; } }

@media only screen and (max-width: 40em) {
  .f-dropdown {
    max-width: 100%;
    left: 0; } }

/* Foundation Dropdowns */
.f-dropdown {
  position: absolute;
  top: -9999px;
  list-style: none;
  margin-left: 0;
  width: 100%;
  max-height: none;
  height: auto;
  background: white;
  border: solid 1px #cccccc;
  font-size: 16px;
  z-index: 99;
  margin-top: 2px;
  max-width: 200px; }
  .f-dropdown > *:first-child {
    margin-top: 0; }
  .f-dropdown > *:last-child {
    margin-bottom: 0; }
  .f-dropdown:before {
    content: "";
    display: block;
    width: 0;
    height: 0;
    border: inset 6px;
    border-color: transparent transparent white transparent;
    border-bottom-style: solid;
    position: absolute;
    top: -12px;
    left: 10px;
    z-index: 99; }
  .f-dropdown:after {
    content: "";
    display: block;
    width: 0;
    height: 0;
    border: inset 7px;
    border-color: transparent transparent #cccccc transparent;
    border-bottom-style: solid;
    position: absolute;
    top: -14px;
    left: 9px;
    z-index: 98; }
  .f-dropdown.right:before {
    left: auto;
    right: 10px; }
  .f-dropdown.right:after {
    left: auto;
    right: 9px; }
  .f-dropdown li {
    font-size: 0.875rem;
    cursor: pointer;
    line-height: 1.125rem;
    margin: 0; }
    .f-dropdown li:hover, .f-dropdown li:focus {
      background: #eeeeee; }
    .f-dropdown li a {
      display: block;
      padding: 0.5rem;
      color: #555555; }
  .f-dropdown.content {
    position: absolute;
    top: -9999px;
    list-style: none;
    margin-left: 0;
    padding: 1.25rem;
    width: 100%;
    height: auto;
    max-height: none;
    background: white;
    border: solid 1px #cccccc;
    font-size: 16px;
    z-index: 99;
    max-width: 200px; }
    .f-dropdown.content > *:first-child {
      margin-top: 0; }
    .f-dropdown.content > *:last-child {
      margin-bottom: 0; }
  .f-dropdown.tiny {
    max-width: 200px; }
  .f-dropdown.small {
    max-width: 300px; }
  .f-dropdown.medium {
    max-width: 500px; }
  .f-dropdown.large {
    max-width: 800px; }

.dropdown.button {
  position: relative;
  padding-right: 3.5625rem; }
  .dropdown.button:before {
    position: absolute;
    content: "";
    width: 0;
    height: 0;
    display: block;
    border-style: solid;
    border-color: white transparent transparent transparent;
    top: 50%; }
  .dropdown.button:before {
    border-width: 0.375rem;
    right: 1.40625rem;
    margin-top: -0.15625rem; }
  .dropdown.button:before {
    border-color: white transparent transparent transparent; }
  .dropdown.button.tiny {
    padding-right: 2.625rem; }
    .dropdown.button.tiny:before {
      border-width: 0.375rem;
      right: 1.125rem;
      margin-top: -0.125rem; }
    .dropdown.button.tiny:before {
      border-color: white transparent transparent transparent; }
  .dropdown.button.small {
    padding-right: 3.0625rem; }
    .dropdown.button.small:before {
      border-width: 0.4375rem;
      right: 1.3125rem;
      margin-top: -0.15625rem; }
    .dropdown.button.small:before {
      border-color: white transparent transparent transparent; }
  .dropdown.button.large {
    padding-right: 3.625rem; }
    .dropdown.button.large:before {
      border-width: 0.3125rem;
      right: 1.71875rem;
      margin-top: -0.15625rem; }
    .dropdown.button.large:before {
      border-color: white transparent transparent transparent; }
  .dropdown.button.secondary:before {
    border-color: #333333 transparent transparent transparent; }

.flex-video {
  position: relative;
  padding-top: 1.5625rem;
  padding-bottom: 67.5%;
  height: 0;
  margin-bottom: 1rem;
  overflow: hidden; }
  .flex-video.widescreen {
    padding-bottom: 57.25%; }
  .flex-video.vimeo {
    padding-top: 0; }
  .flex-video iframe, .flex-video object, .flex-video embed, .flex-video video {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%; }

/* Standard Forms */
form {
  margin: 0 0 1rem; }

/* Using forms within rows, we need to set some defaults */
form .row .row {
  margin: 0 -0.5rem; }
  form .row .row .column, form .row .row .columns {
    padding: 0 0.5rem; }
  form .row .row.collapse {
    margin: 0; }
    form .row .row.collapse .column, form .row .row.collapse .columns {
      padding: 0; }
    form .row .row.collapse input {
      -moz-border-radius-bottomright: 0;
      -moz-border-radius-topright: 0;
      -webkit-border-bottom-right-radius: 0;
      -webkit-border-top-right-radius: 0; }
form .row input.column, form .row input.columns, form .row textarea.column, form .row textarea.columns {
  padding-left: 0.5rem; }

/* Label Styles */
label {
  font-size: 0.875rem;
  color: #4d4d4d;
  cursor: pointer;
  display: block;
  font-weight: normal;
  margin-bottom: 0.5rem;
  /* Styles for required inputs */ }
  label.right {
    float: none;
    text-align: right; }
  label.inline {
    margin: 0 0 1rem 0;
    padding: 0.625rem 0; }
  label small {
    text-transform: capitalize;
    color: #676767; }

select {
  -webkit-appearance: none !important;
  background: #fafafa url('data:image/svg+xml;base64, PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeD0iMHB4IiB5PSIwcHgiIHdpZHRoPSI2cHgiIGhlaWdodD0iM3B4IiB2aWV3Qm94PSIwIDAgNiAzIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA2IDMiIHhtbDpzcGFjZT0icHJlc2VydmUiPjxwb2x5Z29uIHBvaW50cz0iNS45OTIsMCAyLjk5MiwzIC0wLjAwOCwwICIvPjwvc3ZnPg==') no-repeat;
  background-position-x: 97%;
  background-position-y: center;
  border: 1px solid #cccccc;
  padding: 0.5rem;
  font-size: 0.875rem;
  -webkit-border-radius: 0;
  border-radius: 0; }
  select.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }
  select:hover {
    background: #f2f2f2 url('data:image/svg+xml;base64, PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZlcnNpb249IjEuMSIgeD0iMHB4IiB5PSIwcHgiIHdpZHRoPSI2cHgiIGhlaWdodD0iM3B4IiB2aWV3Qm94PSIwIDAgNiAzIiBlbmFibGUtYmFja2dyb3VuZD0ibmV3IDAgMCA2IDMiIHhtbDpzcGFjZT0icHJlc2VydmUiPjxwb2x5Z29uIHBvaW50cz0iNS45OTIsMCAyLjk5MiwzIC0wLjAwOCwwICIvPjwvc3ZnPg==') no-repeat;
    background-position-x: 97%;
    background-position-y: center;
    border-color: #999999; }

@-moz-document url-prefix() {
  select {
    background: #fafafa; }

  select:hover {
    background: #f2f2f2; } }

/* Attach elements to the beginning or end of an input */
.prefix, .postfix {
  display: block;
  position: relative;
  z-index: 2;
  text-align: center;
  width: 100%;
  padding-top: 0;
  padding-bottom: 0;
  border-style: solid;
  border-width: 1px;
  overflow: hidden;
  font-size: 0.875rem;
  height: 2.3125rem;
  line-height: 2.3125rem; }

/* Adjust padding, alignment and radius if pre/post element is a button */
.postfix.button {
  padding-left: 0;
  padding-right: 0;
  padding-top: 0;
  padding-bottom: 0;
  text-align: center;
  line-height: 2.125rem;
  border: none; }

.prefix.button {
  padding-left: 0;
  padding-right: 0;
  padding-top: 0;
  padding-bottom: 0;
  text-align: center;
  line-height: 2.125rem;
  border: none; }

.prefix.button.radius {
  -webkit-border-radius: 0;
  border-radius: 0;
  -moz-border-radius-bottomleft: 3px;
  -moz-border-radius-topleft: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -webkit-border-top-left-radius: 3px;
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px; }

.postfix.button.radius {
  -webkit-border-radius: 0;
  border-radius: 0;
  -moz-border-radius-topright: 3px;
  -moz-border-radius-bottomright: 3px;
  -webkit-border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px; }

.prefix.button.round {
  -webkit-border-radius: 0;
  border-radius: 0;
  -moz-border-radius-bottomleft: 1000px;
  -moz-border-radius-topleft: 1000px;
  -webkit-border-bottom-left-radius: 1000px;
  -webkit-border-top-left-radius: 1000px;
  border-bottom-left-radius: 1000px;
  border-top-left-radius: 1000px; }

.postfix.button.round {
  -webkit-border-radius: 0;
  border-radius: 0;
  -moz-border-radius-topright: 1000px;
  -moz-border-radius-bottomright: 1000px;
  -webkit-border-top-right-radius: 1000px;
  -webkit-border-bottom-right-radius: 1000px;
  border-top-right-radius: 1000px;
  border-bottom-right-radius: 1000px; }

/* Separate prefix and postfix styles when on span or label so buttons keep their own */
span.prefix, label.prefix {
  background: #f2f2f2;
  border-color: #d8d8d8;
  border-right: none;
  color: #333333; }
  span.prefix.radius, label.prefix.radius {
    -webkit-border-radius: 0;
    border-radius: 0;
    -moz-border-radius-bottomleft: 3px;
    -moz-border-radius-topleft: 3px;
    -webkit-border-bottom-left-radius: 3px;
    -webkit-border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    border-top-left-radius: 3px; }

span.postfix, label.postfix {
  background: #f2f2f2;
  border-color: #cccccc;
  border-left: none;
  color: #333333; }
  span.postfix.radius, label.postfix.radius {
    -webkit-border-radius: 0;
    border-radius: 0;
    -moz-border-radius-topright: 3px;
    -moz-border-radius-bottomright: 3px;
    -webkit-border-top-right-radius: 3px;
    -webkit-border-bottom-right-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px; }

/* Input groups will automatically style first and last elements of the group */
.input-group.radius > *:first-child, .input-group.radius > *:first-child * {
  -moz-border-radius-bottomleft: 3px;
  -moz-border-radius-topleft: 3px;
  -webkit-border-bottom-left-radius: 3px;
  -webkit-border-top-left-radius: 3px;
  border-bottom-left-radius: 3px;
  border-top-left-radius: 3px; }
.input-group.radius > *:last-child, .input-group.radius > *:last-child * {
  -moz-border-radius-topright: 3px;
  -moz-border-radius-bottomright: 3px;
  -webkit-border-top-right-radius: 3px;
  -webkit-border-bottom-right-radius: 3px;
  border-top-right-radius: 3px;
  border-bottom-right-radius: 3px; }
.input-group.round > *:first-child, .input-group.round > *:first-child * {
  -moz-border-radius-bottomleft: 1000px;
  -moz-border-radius-topleft: 1000px;
  -webkit-border-bottom-left-radius: 1000px;
  -webkit-border-top-left-radius: 1000px;
  border-bottom-left-radius: 1000px;
  border-top-left-radius: 1000px; }
.input-group.round > *:last-child, .input-group.round > *:last-child * {
  -moz-border-radius-topright: 1000px;
  -moz-border-radius-bottomright: 1000px;
  -webkit-border-top-right-radius: 1000px;
  -webkit-border-bottom-right-radius: 1000px;
  border-top-right-radius: 1000px;
  border-bottom-right-radius: 1000px; }

/* We use this to get basic styling on all basic form elements */
input[type="text"], input[type="password"], input[type="date"], input[type="datetime"], input[type="datetime-local"], input[type="month"], input[type="week"], input[type="email"], input[type="number"], input[type="search"], input[type="tel"], input[type="time"], input[type="url"], textarea {
  -webkit-appearance: none;
  -webkit-border-radius: 0;
  border-radius: 0;
  background-color: white;
  font-family: inherit;
  border: 1px solid #cccccc;
  -webkit-box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.1);
  color: rgba(0, 0, 0, 0.75);
  display: block;
  font-size: 0.875rem;
  margin: 0 0 1rem 0;
  padding: 0.5rem;
  height: 2.3125rem;
  width: 100%;
  -moz-box-sizing: border-box;
  -webkit-box-sizing: border-box;
  box-sizing: border-box;
  -webkit-transition: -webkit-box-shadow 0.45s, border-color 0.45s ease-in-out;
  -moz-transition: -moz-box-shadow 0.45s, border-color 0.45s ease-in-out;
  transition: box-shadow 0.45s, border-color 0.45s ease-in-out;
  -webkit-transition: all 0.15s linear;
  -moz-transition: all 0.15s linear;
  transition: all 0.15s linear; }
  input[type="text"]:focus, input[type="password"]:focus, input[type="date"]:focus, input[type="datetime"]:focus, input[type="datetime-local"]:focus, input[type="month"]:focus, input[type="week"]:focus, input[type="email"]:focus, input[type="number"]:focus, input[type="search"]:focus, input[type="tel"]:focus, input[type="time"]:focus, input[type="url"]:focus, textarea:focus {
    -webkit-box-shadow: 0 0 5px #999999;
    -moz-box-shadow: 0 0 5px #999999;
    box-shadow: 0 0 5px #999999;
    border-color: #999999; }
  input[type="text"]:focus, input[type="password"]:focus, input[type="date"]:focus, input[type="datetime"]:focus, input[type="datetime-local"]:focus, input[type="month"]:focus, input[type="week"]:focus, input[type="email"]:focus, input[type="number"]:focus, input[type="search"]:focus, input[type="tel"]:focus, input[type="time"]:focus, input[type="url"]:focus, textarea:focus {
    background: #fafafa;
    border-color: #999999;
    outline: none; }
  input[type="text"][disabled], input[type="password"][disabled], input[type="date"][disabled], input[type="datetime"][disabled], input[type="datetime-local"][disabled], input[type="month"][disabled], input[type="week"][disabled], input[type="email"][disabled], input[type="number"][disabled], input[type="search"][disabled], input[type="tel"][disabled], input[type="time"][disabled], input[type="url"][disabled], textarea[disabled] {
    background-color: #dddddd; }

/* Adjust margin for form elements below */
input[type="file"], input[type="checkbox"], input[type="radio"], select {
  margin: 0 0 1rem 0; }

input[type="checkbox"] + label, input[type="radio"] + label {
  display: inline-block;
  margin-left: 0.5rem;
  margin-right: 1rem;
  margin-bottom: 0;
  vertical-align: baseline; }

/* Normalize file input width */
input[type="file"] {
  width: 100%; }

/* We add basic fieldset styling */
fieldset {
  border: solid 1px #dddddd;
  padding: 1.25rem;
  margin: 1.125rem 0; }
  fieldset legend {
    font-weight: bold;
    background: white;
    padding: 0 0.1875rem;
    margin: 0;
    margin-left: -0.1875rem; }

/* Error Handling */
[data-abide] .error small.error, [data-abide] span.error, [data-abide] small.error {
  display: block;
  padding: 0.375rem 0.5625rem 0.5625rem;
  margin-top: -1px;
  margin-bottom: 1rem;
  font-size: 0.75rem;
  font-weight: normal;
  font-style: italic;
  background: #f04124;
  color: white; }
[data-abide] span.error, [data-abide] small.error {
  display: none; }

span.error, small.error {
  display: block;
  padding: 0.375rem 0.5625rem 0.5625rem;
  margin-top: -1px;
  margin-bottom: 1rem;
  font-size: 0.75rem;
  font-weight: normal;
  font-style: italic;
  background: #f04124;
  color: white; }

.error input, .error textarea, .error select {
  margin-bottom: 0; }
.error label, .error label.error {
  color: #f04124; }
.error > small, .error small.error {
  display: block;
  padding: 0.375rem 0.5625rem 0.5625rem;
  margin-top: -1px;
  margin-bottom: 1rem;
  font-size: 0.75rem;
  font-weight: normal;
  font-style: italic;
  background: #f04124;
  color: white; }
.error span.error-message {
  display: block; }

input.error, textarea.error {
  margin-bottom: 0; }

label.error {
  color: #f04124; }

.inline-list {
  margin: 0 auto 1.0625rem auto;
  margin-left: -1.375rem;
  margin-right: 0;
  padding: 0;
  list-style: none;
  overflow: hidden; }
  .inline-list > li {
    list-style: none;
    float: left;
    margin-left: 1.375rem;
    display: block; }
    .inline-list > li > * {
      display: block; }

/* Foundation Joyride */
.joyride-list {
  display: none; }

/* Default styles for the container */
.joyride-tip-guide {
  display: none;
  position: absolute;
  background: #333333;
  color: white;
  z-index: 101;
  top: 0;
  left: 2.5%;
  font-family: inherit;
  font-weight: normal;
  width: 95%; }

.lt-ie9 .joyride-tip-guide {
  max-width: 800px;
  left: 50%;
  margin-left: -400px; }

.joyride-content-wrapper {
  width: 100%;
  padding: 1.125rem 1.25rem 1.5rem; }
  .joyride-content-wrapper .button {
    margin-bottom: 0 !important; }

/* Add a little css triangle pip, older browser just miss out on the fanciness of it */
.joyride-tip-guide .joyride-nub {
  display: block;
  position: absolute;
  left: 22px;
  width: 0;
  height: 0;
  border: 10px solid #333333; }
  .joyride-tip-guide .joyride-nub.top {
    border-top-style: solid;
    border-color: #333333;
    border-top-color: transparent !important;
    border-left-color: transparent !important;
    border-right-color: transparent !important;
    top: -20px; }
  .joyride-tip-guide .joyride-nub.bottom {
    border-bottom-style: solid;
    border-color: #333333 !important;
    border-bottom-color: transparent !important;
    border-left-color: transparent !important;
    border-right-color: transparent !important;
    bottom: -20px; }
  .joyride-tip-guide .joyride-nub.right {
    right: -20px; }
  .joyride-tip-guide .joyride-nub.left {
    left: -20px; }

/* Typography */
.joyride-tip-guide h1, .joyride-tip-guide h2, .joyride-tip-guide h3, .joyride-tip-guide h4, .joyride-tip-guide h5, .joyride-tip-guide h6 {
  line-height: 1.25;
  margin: 0;
  font-weight: bold;
  color: white; }

.joyride-tip-guide p {
  margin: 0 0 1.125rem 0;
  font-size: 0.875rem;
  line-height: 1.3; }

.joyride-timer-indicator-wrap {
  width: 50px;
  height: 3px;
  border: solid 1px #555555;
  position: absolute;
  right: 1.0625rem;
  bottom: 1rem; }

.joyride-timer-indicator {
  display: block;
  width: 0;
  height: inherit;
  background: #666666; }

.joyride-close-tip {
  position: absolute;
  right: 12px;
  top: 10px;
  color: #777777 !important;
  text-decoration: none;
  font-size: 24px;
  font-weight: normal;
  line-height: 0.5 !important; }
  .joyride-close-tip:hover, .joyride-close-tip:focus {
    color: #eeeeee !important; }

.joyride-modal-bg {
  position: fixed;
  height: 100%;
  width: 100%;
  background: transparent;
  background: rgba(0, 0, 0, 0.5);
  z-index: 100;
  display: none;
  top: 0;
  left: 0;
  cursor: pointer; }

.joyride-expose-wrapper {
  background-color: white;
  position: absolute;
  border-radius: 3px;
  z-index: 102;
  -moz-box-shadow: 0 0 30px white;
  -webkit-box-shadow: 0 0 15px white;
  box-shadow: 0 0 15px white; }

.joyride-expose-cover {
  background: transparent;
  border-radius: 3px;
  position: absolute;
  z-index: 9999;
  top: 0;
  left: 0; }

/* Styles for screens that are atleast 768px; */
@media only screen and (min-width:40.063em) {
  .joyride-tip-guide {
    width: 300px;
    left: inherit; }
    .joyride-tip-guide .joyride-nub.bottom {
      border-color: #333333 !important;
      border-bottom-color: transparent !important;
      border-left-color: transparent !important;
      border-right-color: transparent !important;
      bottom: -20px; }
    .joyride-tip-guide .joyride-nub.right {
      border-color: #333333 !important;
      border-top-color: transparent !important;
      border-right-color: transparent !important;
      border-bottom-color: transparent !important;
      top: 22px;
      left: auto;
      right: -20px; }
    .joyride-tip-guide .joyride-nub.left {
      border-color: #333333 !important;
      border-top-color: transparent !important;
      border-left-color: transparent !important;
      border-bottom-color: transparent !important;
      top: 22px;
      left: -20px;
      right: auto; } }

.keystroke, kbd {
  background-color: #ededed;
  border-color: #dbdbdb;
  color: #222222;
  border-style: solid;
  border-width: 1px;
  margin: 0;
  font-family: "Consolas", "Menlo", "Courier", monospace;
  font-size: 0.875rem;
  padding: 0.125rem 0.25rem 0;
  -webkit-border-radius: 3px;
  border-radius: 3px; }

.label {
  font-weight: normal;
  font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
  text-align: center;
  text-decoration: none;
  line-height: 1;
  white-space: nowrap;
  display: inline-block;
  position: relative;
  margin-bottom: inherit;
  padding: 0.25rem 0.5rem 0.375rem;
  font-size: 0.6875rem;
  background-color: #008cba;
  color: white; }
  .label.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }
  .label.round {
    -webkit-border-radius: 1000px;
    border-radius: 1000px; }
  .label.alert {
    background-color: #f04124;
    color: white; }
  .label.success {
    background-color: #43ac6a;
    color: white; }
  .label.secondary {
    background-color: #e7e7e7;
    color: #333333; }

[data-magellan-expedition] {
  background: white;
  z-index: 50;
  min-width: 100%;
  padding: 10px; }
  [data-magellan-expedition] .sub-nav {
    margin-bottom: 0; }
    [data-magellan-expedition] .sub-nav dd {
      margin-bottom: 0; }
    [data-magellan-expedition] .sub-nav .active {
      line-height: 1.8em; }

@-webkit-keyframes rotate {
  from {
    -webkit-transform: rotate(0deg); }

  to {
    -webkit-transform: rotate(360deg); } }

@-moz-keyframes rotate {
  from {
    -moz-transform: rotate(0deg); }

  to {
    -moz-transform: rotate(360deg); } }

@-o-keyframes rotate {
  from {
    -o-transform: rotate(0deg); }

  to {
    -o-transform: rotate(360deg); } }

@keyframes rotate {
  from {
    transform: rotate(0deg); }

  to {
    transform: rotate(360deg); } }

/* Orbit Graceful Loading */
.slideshow-wrapper {
  position: relative; }
  .slideshow-wrapper ul {
    list-style-type: none;
    margin: 0; }
    .slideshow-wrapper ul li, .slideshow-wrapper ul li .orbit-caption {
      display: none; }
    .slideshow-wrapper ul li:first-child {
      display: block; }
  .slideshow-wrapper .orbit-container {
    background-color: transparent; }
    .slideshow-wrapper .orbit-container li {
      display: block; }
      .slideshow-wrapper .orbit-container li .orbit-caption {
        display: block; }

.preloader {
  display: block;
  width: 40px;
  height: 40px;
  position: absolute;
  top: 50%;
  left: 50%;
  margin-top: -20px;
  margin-left: -20px;
  border: solid 3px;
  border-color: #555555 white;
  -webkit-border-radius: 1000px;
  border-radius: 1000px;
  -webkit-animation-name: rotate;
  -webkit-animation-duration: 1.5s;
  -webkit-animation-iteration-count: infinite;
  -webkit-animation-timing-function: linear;
  -moz-animation-name: rotate;
  -moz-animation-duration: 1.5s;
  -moz-animation-iteration-count: infinite;
  -moz-animation-timing-function: linear;
  -o-animation-name: rotate;
  -o-animation-duration: 1.5s;
  -o-animation-iteration-count: infinite;
  -o-animation-timing-function: linear;
  animation-name: rotate;
  animation-duration: 1.5s;
  animation-iteration-count: infinite;
  animation-timing-function: linear; }

.orbit-container {
  overflow: hidden;
  width: 100%;
  position: relative;
  background: none; }
  .orbit-container .orbit-slides-container {
    list-style: none;
    margin: 0;
    padding: 0;
    position: relative; }
    .orbit-container .orbit-slides-container img {
      display: block;
      max-width: 100%; }
    .orbit-container .orbit-slides-container > * {
      position: absolute;
      top: 0;
      width: 100%;
      margin-left: 100%; }
      .orbit-container .orbit-slides-container > *:first-child {
        margin-left: 0%; }
      .orbit-container .orbit-slides-container > * .orbit-caption {
        position: absolute;
        bottom: 0;
        background-color: rgba(51, 51, 51, 0.8);
        color: white;
        width: 100%;
        padding: 10px 14px;
        font-size: 0.875rem; }
  .orbit-container .orbit-slide-number {
    position: absolute;
    top: 10px;
    left: 10px;
    font-size: 12px;
    color: white;
    background: rgba(0, 0, 0, 0);
    z-index: 10; }
    .orbit-container .orbit-slide-number span {
      font-weight: 700;
      padding: 0.3125rem; }
  .orbit-container .orbit-timer {
    position: absolute;
    top: 12px;
    right: 10px;
    height: 6px;
    width: 100px;
    z-index: 10; }
    .orbit-container .orbit-timer .orbit-progress {
      height: 3px;
      background-color: rgba(255, 255, 255, 0.3);
      display: block;
      width: 0%;
      position: relative;
      right: 20px;
      top: 5px; }
    .orbit-container .orbit-timer > span {
      display: none;
      position: absolute;
      top: 0px;
      right: 0;
      width: 11px;
      height: 14px;
      border: solid 4px white;
      border-top: none;
      border-bottom: none; }
    .orbit-container .orbit-timer.paused > span {
      right: -4px;
      top: 0px;
      width: 11px;
      height: 14px;
      border: inset 8px;
      border-right-style: solid;
      border-color: transparent transparent transparent white; }
      .orbit-container .orbit-timer.paused > span.dark {
        border-color: transparent transparent transparent #333333; }
  .orbit-container:hover .orbit-timer > span {
    display: block; }
  .orbit-container .orbit-prev, .orbit-container .orbit-next {
    position: absolute;
    top: 45%;
    margin-top: -25px;
    width: 36px;
    height: 60px;
    line-height: 50px;
    color: white;
    text-indent: -9999px !important;
    z-index: 10; }
    .orbit-container .orbit-prev:hover, .orbit-container .orbit-next:hover {
      background-color: rgba(0, 0, 0, 0.3); }
    .orbit-container .orbit-prev > span, .orbit-container .orbit-next > span {
      position: absolute;
      top: 50%;
      margin-top: -10px;
      display: block;
      width: 0;
      height: 0;
      border: inset 10px; }
  .orbit-container .orbit-prev {
    left: 0; }
    .orbit-container .orbit-prev > span {
      border-right-style: solid;
      border-color: transparent;
      border-right-color: white; }
    .orbit-container .orbit-prev:hover > span {
      border-right-color: white; }
  .orbit-container .orbit-next {
    right: 0; }
    .orbit-container .orbit-next > span {
      border-color: transparent;
      border-left-style: solid;
      border-left-color: white;
      left: 50%;
      margin-left: -4px; }
    .orbit-container .orbit-next:hover > span {
      border-left-color: white; }

.orbit-bullets-container {
  text-align: center; }

.orbit-bullets {
  margin: 0 auto 30px auto;
  overflow: hidden;
  position: relative;
  top: 10px;
  float: none;
  text-align: center;
  display: inline-block; }
  .orbit-bullets li {
    display: block;
    width: 0.5625rem;
    height: 0.5625rem;
    background: #cccccc;
    float: left;
    margin-right: 6px;
    -webkit-border-radius: 1000px;
    border-radius: 1000px; }
    .orbit-bullets li.active {
      background: #999999; }
    .orbit-bullets li:last-child {
      margin-right: 0; }

.touch .orbit-container .orbit-prev, .touch .orbit-container .orbit-next {
  display: none; }
.touch .orbit-bullets {
  display: none; }

@media only screen and (min-width:40.063em) {
  .touch .orbit-container .orbit-prev, .touch .orbit-container .orbit-next {
    display: inherit; }
  .touch .orbit-bullets {
    display: block; } }

@media only screen and (max-width: 40em) {
  .orbit-stack-on-small .orbit-slides-container {
    height: auto !important; }
  .orbit-stack-on-small .orbit-slides-container > * {
    position: relative;
    margin-left: 0% !important; }
  .orbit-stack-on-small .orbit-timer, .orbit-stack-on-small .orbit-next, .orbit-stack-on-small .orbit-prev, .orbit-stack-on-small .orbit-bullets {
    display: none; } }

ul.pagination {
  display: block;
  height: 1.5rem;
  margin-left: -0.3125rem; }
  ul.pagination li {
    height: 1.5rem;
    color: #222222;
    font-size: 0.875rem;
    margin-left: 0.3125rem; }
    ul.pagination li a {
      display: block;
      padding: 0.0625rem 0.625rem 0.0625rem;
      color: #999999;
      -webkit-border-radius: 3px;
      border-radius: 3px; }
    ul.pagination li:hover a, ul.pagination li a:focus {
      background: #e6e6e6; }
    ul.pagination li.unavailable a {
      cursor: default;
      color: #999999; }
    ul.pagination li.unavailable:hover a, ul.pagination li.unavailable a:focus {
      background: transparent; }
    ul.pagination li.current a {
      background: #008cba;
      color: white;
      font-weight: bold;
      cursor: default; }
      ul.pagination li.current a:hover, ul.pagination li.current a:focus {
        background: #008cba; }
  ul.pagination li {
    float: left;
    display: block; }

/* Pagination centred wrapper */
.pagination-centered {
  text-align: center; }
  .pagination-centered ul.pagination li {
    float: none;
    display: inline-block; }

/* Panels */
.panel {
  border-style: solid;
  border-width: 1px;
  border-color: #d8d8d8;
  margin-bottom: 1.25rem;
  padding: 1.25rem;
  background: #f2f2f2; }
  .panel > :first-child {
    margin-top: 0; }
  .panel > :last-child {
    margin-bottom: 0; }
  .panel h1, .panel h2, .panel h3, .panel h4, .panel h5, .panel h6, .panel p {
    color: #333333; }
  .panel h1, .panel h2, .panel h3, .panel h4, .panel h5, .panel h6 {
    line-height: 1;
    margin-bottom: 0.625rem; }
    .panel h1.subheader, .panel h2.subheader, .panel h3.subheader, .panel h4.subheader, .panel h5.subheader, .panel h6.subheader {
      line-height: 1.4; }
  .panel.callout {
    border-style: solid;
    border-width: 1px;
    border-color: #baf0ff;
    margin-bottom: 1.25rem;
    padding: 1.25rem;
    background: #edfbff; }
    .panel.callout > :first-child {
      margin-top: 0; }
    .panel.callout > :last-child {
      margin-bottom: 0; }
    .panel.callout h1, .panel.callout h2, .panel.callout h3, .panel.callout h4, .panel.callout h5, .panel.callout h6, .panel.callout p {
      color: #333333; }
    .panel.callout h1, .panel.callout h2, .panel.callout h3, .panel.callout h4, .panel.callout h5, .panel.callout h6 {
      line-height: 1;
      margin-bottom: 0.625rem; }
      .panel.callout h1.subheader, .panel.callout h2.subheader, .panel.callout h3.subheader, .panel.callout h4.subheader, .panel.callout h5.subheader, .panel.callout h6.subheader {
        line-height: 1.4; }
    .panel.callout a {
      color: #008cba; }
  .panel.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }

/* Pricing Tables */
.pricing-table {
  border: solid 1px #dddddd;
  margin-left: 0;
  margin-bottom: 1.25rem; }
  .pricing-table * {
    list-style: none;
    line-height: 1; }
  .pricing-table .title {
    background-color: #333333;
    padding: 0.9375rem 1.25rem;
    text-align: center;
    color: #eeeeee;
    font-weight: normal;
    font-size: 1rem;
    font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; }
  .pricing-table .price {
    background-color: #f6f6f6;
    padding: 0.9375rem 1.25rem;
    text-align: center;
    color: #333333;
    font-weight: normal;
    font-size: 2rem;
    font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; }
  .pricing-table .description {
    background-color: white;
    padding: 0.9375rem;
    text-align: center;
    color: #777777;
    font-size: 0.75rem;
    font-weight: normal;
    line-height: 1.4;
    border-bottom: dotted 1px #dddddd; }
  .pricing-table .bullet-item {
    background-color: white;
    padding: 0.9375rem;
    text-align: center;
    color: #333333;
    font-size: 0.875rem;
    font-weight: normal;
    border-bottom: dotted 1px #dddddd; }
  .pricing-table .cta-button {
    background-color: white;
    text-align: center;
    padding: 1.25rem 1.25rem 0; }

/* Progress Bar */
.progress {
  background-color: #f6f6f6;
  height: 1.5625rem;
  border: 1px solid #cccccc;
  padding: 0.125rem;
  margin-bottom: 0.625rem; }
  .progress .meter {
    background: #008cba;
    height: 100%;
    display: block; }
  .progress.secondary .meter {
    background: #e7e7e7;
    height: 100%;
    display: block; }
  .progress.success .meter {
    background: #43ac6a;
    height: 100%;
    display: block; }
  .progress.alert .meter {
    background: #f04124;
    height: 100%;
    display: block; }
  .progress.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }
    .progress.radius .meter {
      -webkit-border-radius: 2px;
      border-radius: 2px; }
  .progress.round {
    -webkit-border-radius: 1000px;
    border-radius: 1000px; }
    .progress.round .meter {
      -webkit-border-radius: 999px;
      border-radius: 999px; }

.reveal-modal-bg {
  position: fixed;
  height: 100%;
  width: 100%;
  background: black;
  background: rgba(0, 0, 0, 0.45);
  z-index: 98;
  display: none;
  top: 0;
  left: 0; }

.reveal-modal {
  visibility: hidden;
  display: none;
  position: absolute;
  left: 50%;
  z-index: 99;
  height: auto;
  margin-left: -40%;
  width: 80%;
  background-color: white;
  padding: 1.25rem;
  border: solid 1px #666666;
  -webkit-box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.4);
  top: 50px; }
  .reveal-modal .column, .reveal-modal .columns {
    min-width: 0; }
  .reveal-modal > :first-child {
    margin-top: 0; }
  .reveal-modal > :last-child {
    margin-bottom: 0; }
  .reveal-modal .close-reveal-modal {
    font-size: 1.375rem;
    line-height: 1;
    position: absolute;
    top: 0.5rem;
    right: 0.6875rem;
    color: #aaaaaa;
    font-weight: bold;
    cursor: pointer; }

@media only screen and (min-width:40.063em) {
  .reveal-modal {
    padding: 1.875rem;
    top: 6.25rem; }
    .reveal-modal.tiny {
      margin-left: -15%;
      width: 30%; }
    .reveal-modal.small {
      margin-left: -20%;
      width: 40%; }
    .reveal-modal.medium {
      margin-left: -30%;
      width: 60%; }
    .reveal-modal.large {
      margin-left: -35%;
      width: 70%; }
    .reveal-modal.xlarge {
      margin-left: -47.5%;
      width: 95%; } }

@media print {
  .reveal-modal {
    background: white !important; } }

.side-nav {
  display: block;
  margin: 0;
  padding: 0.875rem 0;
  list-style-type: none;
  list-style-position: inside;
  font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; }
  .side-nav li {
    margin: 0 0 0.4375rem 0;
    font-size: 0.875rem; }
    .side-nav li a {
      display: block;
      color: #008cba; }
    .side-nav li.active > a:first-child {
      color: #4d4d4d;
      font-weight: normal;
      font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; }
    .side-nav li.divider {
      border-top: 1px solid;
      height: 0;
      padding: 0;
      list-style: none;
      border-top-color: #e6e6e6; }

.split.button {
  position: relative;
  padding-right: 5.0625rem; }
  .split.button span {
    display: block;
    height: 100%;
    position: absolute;
    right: 0;
    top: 0;
    border-left: solid 1px; }
    .split.button span:before {
      position: absolute;
      content: "";
      width: 0;
      height: 0;
      display: block;
      border-style: inset;
      top: 50%;
      left: 50%; }
    .split.button span:active {
      background-color: rgba(0, 0, 0, 0.1); }
  .split.button span {
    border-left-color: rgba(255, 255, 255, 0.5); }
  .split.button span {
    width: 3.09375rem; }
    .split.button span:before {
      border-top-style: solid;
      border-width: 0.375rem;
      top: 48%;
      margin-left: -0.375rem; }
  .split.button span:before {
    border-color: white transparent transparent transparent; }
  .split.button.secondary span {
    border-left-color: rgba(255, 255, 255, 0.5); }
  .split.button.secondary span:before {
    border-color: white transparent transparent transparent; }
  .split.button.alert span {
    border-left-color: rgba(255, 255, 255, 0.5); }
  .split.button.success span {
    border-left-color: rgba(255, 255, 255, 0.5); }
  .split.button.tiny {
    padding-right: 3.75rem; }
    .split.button.tiny span {
      width: 2.25rem; }
      .split.button.tiny span:before {
        border-top-style: solid;
        border-width: 0.375rem;
        top: 48%;
        margin-left: -0.375rem; }
  .split.button.small {
    padding-right: 4.375rem; }
    .split.button.small span {
      width: 2.625rem; }
      .split.button.small span:before {
        border-top-style: solid;
        border-width: 0.4375rem;
        top: 48%;
        margin-left: -0.375rem; }
  .split.button.large {
    padding-right: 5.5rem; }
    .split.button.large span {
      width: 3.4375rem; }
      .split.button.large span:before {
        border-top-style: solid;
        border-width: 0.3125rem;
        top: 48%;
        margin-left: -0.375rem; }
  .split.button.expand {
    padding-left: 2rem; }
  .split.button.secondary span:before {
    border-color: #333333 transparent transparent transparent; }
  .split.button.radius span {
    -moz-border-radius-topright: 3px;
    -moz-border-radius-bottomright: 3px;
    -webkit-border-top-right-radius: 3px;
    -webkit-border-bottom-right-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px; }
  .split.button.round span {
    -moz-border-radius-topright: 1000px;
    -moz-border-radius-bottomright: 1000px;
    -webkit-border-top-right-radius: 1000px;
    -webkit-border-bottom-right-radius: 1000px;
    border-top-right-radius: 1000px;
    border-bottom-right-radius: 1000px; }

.sub-nav {
  display: block;
  width: auto;
  overflow: hidden;
  margin: -0.25rem 0 1.125rem;
  padding-top: 0.25rem;
  margin-right: 0;
  margin-left: -0.75rem; }
  .sub-nav dt {
    text-transform: uppercase; }
  .sub-nav dt, .sub-nav dd, .sub-nav li {
    float: left;
    display: inline;
    margin-left: 1rem;
    margin-bottom: 0.625rem;
    font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
    font-weight: normal;
    font-size: 0.875rem;
    color: #999999; }
    .sub-nav dt a, .sub-nav dd a, .sub-nav li a {
      text-decoration: none;
      color: #999999; }
      .sub-nav dt a:hover, .sub-nav dd a:hover, .sub-nav li a:hover {
        color: #007ba1; }
    .sub-nav dt.active a, .sub-nav dd.active a, .sub-nav li.active a {
      -webkit-border-radius: 3px;
      border-radius: 3px;
      font-weight: normal;
      background: #008cba;
      padding: 0.1875rem 1rem;
      cursor: default;
      color: white; }
      .sub-nav dt.active a:hover, .sub-nav dd.active a:hover, .sub-nav li.active a:hover {
        background: #007ba1; }

div.switch {
  position: relative;
  padding: 0;
  display: block;
  overflow: hidden;
  border-style: solid;
  border-width: 1px;
  margin-bottom: 1.25rem;
  height: 2.25rem;
  background: white;
  border-color: #cccccc; }
  div.switch label {
    position: relative;
    left: 0;
    z-index: 2;
    float: left;
    width: 50%;
    height: 100%;
    margin: 0;
    font-weight: bold;
    text-align: left;
    -webkit-transition: all 0.1s ease-out;
    -moz-transition: all 0.1s ease-out;
    transition: all 0.1s ease-out; }
  div.switch input {
    position: absolute;
    z-index: 3;
    opacity: 0;
    width: 100%;
    height: 100%;
    -moz-appearance: none; }
    div.switch input:hover, div.switch input:focus {
      cursor: pointer; }
  div.switch span:last-child {
    position: absolute;
    top: -1px;
    left: -1px;
    z-index: 1;
    display: block;
    padding: 0;
    border-width: 1px;
    border-style: solid;
    -webkit-transition: all 0.1s ease-out;
    -moz-transition: all 0.1s ease-out;
    transition: all 0.1s ease-out; }
  div.switch input:not(:checked) + label {
    opacity: 0; }
  div.switch input:checked {
    display: none !important; }
  div.switch input {
    left: 0;
    display: block !important; }
  div.switch input:first-of-type + label, div.switch input:first-of-type + span + label {
    left: -50%; }
  div.switch input:first-of-type:checked + label, div.switch input:first-of-type:checked + span + label {
    left: 0%; }
  div.switch input:last-of-type + label, div.switch input:last-of-type + span + label {
    right: -50%;
    left: auto;
    text-align: right; }
  div.switch input:last-of-type:checked + label, div.switch input:last-of-type:checked + span + label {
    right: 0%;
    left: auto; }
  div.switch span.custom {
    display: none !important; }
  form.custom div.switch .hidden-field {
    margin-left: auto;
    position: absolute;
    visibility: visible; }
  div.switch label {
    padding: 0;
    line-height: 2.3rem;
    font-size: 0.875rem; }
  div.switch input:first-of-type:checked ~ span:last-child {
    left: 100%;
    margin-left: -2.1875rem; }
  div.switch span:last-child {
    width: 2.25rem;
    height: 2.25rem; }
  div.switch span:last-child {
    border-color: #b3b3b3;
    background: white;
    background: -moz-linear-gradient(top, #ffffff 0%, #f2f2f2 100%);
    background: -webkit-linear-gradient(top, #ffffff 0%, #f2f2f2 100%);
    background: linear-gradient(to bottom, #ffffff 0%, #f2f2f2 100%);
    -webkit-box-shadow: 2px 0 10px 0 rgba(0, 0, 0, 0.07), 1000px 0 0 1000px #f3fbf6, -2px 0 10px 0 rgba(0, 0, 0, 0.07), -1000px 0 0 1000px whitesmoke;
    box-shadow: 2px 0 10px 0 rgba(0, 0, 0, 0.07), 1000px 0 0 980px #f3fbf6, -2px 0 10px 0 rgba(0, 0, 0, 0.07), -1000px 0 0 1000px whitesmoke; }
  div.switch:hover span:last-child, div.switch:focus span:last-child {
    background: white;
    background: -moz-linear-gradient(top, #ffffff 0%, #e6e6e6 100%);
    background: -webkit-linear-gradient(top, #ffffff 0%, #e6e6e6 100%);
    background: linear-gradient(to bottom, #ffffff 0%, #e6e6e6 100%); }
  div.switch:active {
    background: transparent; }
  div.switch.large {
    height: 2.75rem; }
    div.switch.large label {
      padding: 0;
      line-height: 2.3rem;
      font-size: 1.0625rem; }
    div.switch.large input:first-of-type:checked ~ span:last-child {
      left: 100%;
      margin-left: -2.6875rem; }
    div.switch.large span:last-child {
      width: 2.75rem;
      height: 2.75rem; }
  div.switch.small {
    height: 1.75rem; }
    div.switch.small label {
      padding: 0;
      line-height: 2.1rem;
      font-size: 0.75rem; }
    div.switch.small input:first-of-type:checked ~ span:last-child {
      left: 100%;
      margin-left: -1.6875rem; }
    div.switch.small span:last-child {
      width: 1.75rem;
      height: 1.75rem; }
  div.switch.tiny {
    height: 1.375rem; }
    div.switch.tiny label {
      padding: 0;
      line-height: 1.9rem;
      font-size: 0.6875rem; }
    div.switch.tiny input:first-of-type:checked ~ span:last-child {
      left: 100%;
      margin-left: -1.3125rem; }
    div.switch.tiny span:last-child {
      width: 1.375rem;
      height: 1.375rem; }
  div.switch.radius {
    -webkit-border-radius: 4px;
    border-radius: 4px; }
    div.switch.radius span:last-child {
      -webkit-border-radius: 3px;
      border-radius: 3px; }
  div.switch.round {
    -webkit-border-radius: 1000px;
    border-radius: 1000px; }
    div.switch.round span:last-child {
      -webkit-border-radius: 999px;
      border-radius: 999px; }
    div.switch.round label {
      padding: 0 0.5625rem; }

@-webkit-keyframes webkitSiblingBugfix {
  from {
    position: relative; }

  to {
    position: relative; } }

table {
  background: white;
  margin-bottom: 1.25rem;
  border: solid 1px #dddddd; }
  table thead, table tfoot {
    background: whitesmoke;
    font-weight: bold; }
    table thead tr th, table thead tr td, table tfoot tr th, table tfoot tr td {
      padding: 0.5rem 0.625rem 0.625rem;
      font-size: 0.875rem;
      color: #222222;
      text-align: left; }
  table tr th, table tr td {
    padding: 0.5625rem 0.625rem;
    font-size: 0.875rem;
    color: #222222; }
  table tr.even, table tr.alt, table tr:nth-of-type(even) {
    background: #f9f9f9; }
  table thead tr th, table tfoot tr th, table tbody tr td, table tr td, table tfoot tr td {
    display: table-cell;
    line-height: 1.125rem; }

.tabs {
  *zoom: 1;
  margin-bottom: 0 !important; }
  .tabs:before, .tabs:after {
    content: " ";
    display: table; }
  .tabs:after {
    clear: both; }
  .tabs dd {
    position: relative;
    margin-bottom: 0 !important;
    top: 1px;
    float: left; }
    .tabs dd > a {
      display: block;
      background: #efefef;
      color: #222222;
      padding-top: 1rem;
      padding-right: 2rem;
      padding-bottom: 1.0625rem;
      padding-left: 2rem;
      font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
      font-size: 1rem; }
      .tabs dd > a:hover {
        background: #e2e2e2; }
    .tabs dd.active a {
      background: white; }
  .tabs.radius dd:first-child a {
    -moz-border-radius-bottomleft: 3px;
    -moz-border-radius-topleft: 3px;
    -webkit-border-bottom-left-radius: 3px;
    -webkit-border-top-left-radius: 3px;
    border-bottom-left-radius: 3px;
    border-top-left-radius: 3px; }
  .tabs.radius dd:last-child a {
    -moz-border-radius-topright: 3px;
    -moz-border-radius-bottomright: 3px;
    -webkit-border-top-right-radius: 3px;
    -webkit-border-bottom-right-radius: 3px;
    border-top-right-radius: 3px;
    border-bottom-right-radius: 3px; }
  .tabs.vertical dd {
    position: inherit;
    float: none;
    display: block;
    top: auto; }

.tabs-content {
  *zoom: 1;
  margin-bottom: 1.5rem; }
  .tabs-content:before, .tabs-content:after {
    content: " ";
    display: table; }
  .tabs-content:after {
    clear: both; }
  .tabs-content > .content {
    display: none;
    float: left;
    padding: 0.9375rem 0; }
    .tabs-content > .content.active {
      display: block; }
    .tabs-content > .content.contained {
      padding: 0.9375rem; }
  .tabs-content.vertical {
    display: block; }
    .tabs-content.vertical > .content {
      padding: 0 0.9375rem; }

@media only screen and (min-width:40.063em) {
  .tabs.vertical {
    width: 20%;
    float: left;
    margin-bottom: 1.25rem; }
  .tabs-content.vertical {
    width: 80%;
    float: left;
    margin-left: -1px; } }

/* Image Thumbnails */
.th {
  line-height: 0;
  display: inline-block;
  border: solid 4px white;
  -webkit-box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.2);
  box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.2);
  -webkit-transition: all 200ms ease-out;
  -moz-transition: all 200ms ease-out;
  transition: all 200ms ease-out; }
  .th:hover, .th:focus {
    -webkit-box-shadow: 0 0 6px 1px rgba(0, 140, 186, 0.5);
    box-shadow: 0 0 6px 1px rgba(0, 140, 186, 0.5); }
  .th.radius {
    -webkit-border-radius: 3px;
    border-radius: 3px; }

a.th {
  display: inline-block;
  max-width: 100%; }

/* Tooltips */
.has-tip {
  border-bottom: dotted 1px #cccccc;
  cursor: help;
  font-weight: bold;
  color: #333333; }
  .has-tip:hover, .has-tip:focus {
    border-bottom: dotted 1px #004054;
    color: #008cba; }
  .has-tip.tip-left, .has-tip.tip-right {
    float: none !important; }

.tooltip {
  display: none;
  position: absolute;
  z-index: 999;
  font-weight: normal;
  font-size: 0.875rem;
  line-height: 1.3;
  padding: 0.75rem;
  max-width: 85%;
  left: 50%;
  width: 100%;
  color: white;
  background: #333333;
  -webkit-border-radius: 3px;
  border-radius: 3px; }
  .tooltip > .nub {
    display: block;
    left: 5px;
    position: absolute;
    width: 0;
    height: 0;
    border: solid 5px;
    border-color: transparent transparent #333333 transparent;
    top: -10px; }
  .tooltip.opened {
    color: #008cba !important;
    border-bottom: dotted 1px #004054 !important; }

.tap-to-close {
  display: block;
  font-size: 0.625rem;
  color: #777777;
  font-weight: normal; }

@media only screen and (min-width:40.063em) {
  .tooltip > .nub {
    border-color: transparent transparent #333333 transparent;
    top: -10px; }
  .tooltip.tip-top > .nub {
    border-color: #333333 transparent transparent transparent;
    top: auto;
    bottom: -10px; }
  .tooltip.tip-left, .tooltip.tip-right {
    float: none !important; }
  .tooltip.tip-left > .nub {
    border-color: transparent transparent transparent #333333;
    right: -10px;
    left: auto;
    top: 50%;
    margin-top: -5px; }
  .tooltip.tip-right > .nub {
    border-color: transparent #333333 transparent transparent;
    right: auto;
    left: -10px;
    top: 50%;
    margin-top: -5px; } }

p.lead {
  font-size: 1.21875rem;
  line-height: 1.6; }

.subheader {
  line-height: 1.4;
  color: #6f6f6f;
  font-weight: 300;
  margin-top: 0.2rem;
  margin-bottom: 0.5rem; }

/* Typography resets */
div, dl, dt, dd, ul, ol, li, h1, h2, h3, h4, h5, h6, pre, form, p, blockquote, th, td {
  margin: 0;
  padding: 0;
  direction: ltr; }

/* Default Link Styles */
a {
  color: #008cba;
  text-decoration: none;
  line-height: inherit; }
  a:hover, a:focus {
    color: #007ba1; }
  a img {
    border: none; }

/* Default paragraph styles */
p {
  font-family: inherit;
  font-weight: normal;
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1.25rem;
  text-rendering: optimizeLegibility; }
  p aside {
    font-size: 0.875rem;
    line-height: 1.35;
    font-style: italic; }

/* Default header styles */
h1, h2, h3, h4, h5, h6 {
  font-family: "Open Sans", "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
  font-weight: 300;
  font-style: normal;
  color: #222222;
  text-rendering: optimizeLegibility;
  margin-top: 0.2rem;
  margin-bottom: 0.5rem;
  line-height: 1.4; }
  h1 small, h2 small, h3 small, h4 small, h5 small, h6 small {
    font-size: 60%;
    color: #6f6f6f;
    line-height: 0; }

h1 {
  font-size: 2.125rem; }

h2 {
  font-size: 1.6875rem; }

h3 {
  font-size: 1.375rem; }

h4 {
  font-size: 1.125rem; }

h5 {
  font-size: 1.125rem; }

h6 {
  font-size: 1rem; }


hr {
  border: solid #dddddd;
  border-width: 1px 0 0;
  clear: both;
  margin: 1.25rem 0 1.1875rem;
  height: 0; }

/* Helpful Typography Defaults */
em, i {
  font-style: italic;
  line-height: inherit; }

strong, b {
  font-weight: bold;
  line-height: inherit; }

small {
  font-size: 60%;
  line-height: inherit; }

code {
  font-family: Consolas, 'Liberation Mono', Courier, monospace;
  font-weight: bold;
  color: #bb240d; }

/* Lists */
ul, ol, dl {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1.25rem;
  list-style-position: outside;
  font-family: inherit; }

ul {
  margin-left: 1.1rem; }
  ul.no-bullet {
    margin-left: 0; }
    ul.no-bullet li ul, ul.no-bullet li ol {
      margin-left: 1.25rem;
      margin-bottom: 0;
      list-style: none; }

/* Unordered Lists */
ul li ul, ul li ol {
  margin-left: 1.25rem;
  margin-bottom: 0;
  font-size: 1rem;
  /* Override nested font-size change */ }
ul.square li ul, ul.circle li ul, ul.disc li ul {
  list-style: inherit; }
ul.square {
  list-style-type: square;
  margin-left: 1.1rem; }
ul.circle {
  list-style-type: circle;
  margin-left: 1.1rem; }
ul.disc {
  list-style-type: disc;
  margin-left: 1.1rem; }
ul.no-bullet {
  list-style: none; }

/* Ordered Lists */
ol {
  margin-left: 1.4rem; }
  ol li ul, ol li ol {
    margin-left: 1.25rem;
    margin-bottom: 0; }

/* Definition Lists */
dl dt {
  margin-bottom: 0.3rem;
  font-weight: bold; }
dl dd {
  margin-bottom: 0.75rem; }

/* Abbreviations */
abbr, acronym {
  text-transform: uppercase;
  font-size: 90%;
  color: #222222;
  border-bottom: 1px dotted #dddddd;
  cursor: help; }

abbr {
  text-transform: none; }

/* Blockquotes */
blockquote {
  margin: 0 0 1.25rem;
  padding: 0.5625rem 1.25rem 0 1.1875rem;
  border-left: 1px solid #dddddd; }
  blockquote cite {
    display: block;
    font-size: 0.8125rem;
    color: #555555; }
    blockquote cite:before {
      content: "\814 0"; }
    blockquote cite a, blockquote cite a:visited {
      color: #555555; }

blockquote, blockquote p {
  line-height: 1.6;
  color: #6f6f6f; }

/* Microformats */
.vcard {
  display: inline-block;
  margin: 0 0 1.25rem 0;
  border: 1px solid #dddddd;
  padding: 0.625rem 0.75rem; }
  .vcard li {
    margin: 0;
    display: block; }
  .vcard .fn {
    font-weight: bold;
    font-size: 0.9375rem; }

.vevent .summary {
  font-weight: bold; }
.vevent abbr {
  cursor: default;
  text-decoration: none;
  font-weight: bold;
  border: none;
  padding: 0 0.0625rem; }

@media only screen and (min-width:40.063em) {
  h1, h2, h3, h4, h5, h6 {
    line-height: 1.4; }
  h1 {
    font-size: 2.75rem; }
  h2 {
    font-size: 2.3125rem; }
  h3 {
    font-size: 1.6875rem; }
  h4 {
    font-size: 1.4375rem; } }

/*
       * Print styles.
       *
       * Inlined to avoid required HTTP connection: www.phpied.com/delay-loading-your-print-css/
       * Credit to Paul Irish and HTML5 Boilerplate (html5boilerplate.com)
      */
.print-only {
  display: none !important; }

@media print {
  @page {
    margin: 0.5cm; }

  * {
    background: transparent !important;
    color: black !important;
    /* Black prints faster: h5bp.com/s */
    box-shadow: none !important;
    text-shadow: none !important; }
  a, a:visited {
    text-decoration: underline; }
  a[href]:after {
    content: " (" attr(href) ")"; }
  abbr[title]:after {
    content: " (" attr(title) ")"; }
  .ir a:after, a[href^="javascript:"]:after, a[href^="#"]:after {
    content: ""; }
  pre, blockquote {
    border: 1px solid #999999;
    page-break-inside: avoid; }
  thead {
    display: table-header-group;
    /* h5bp.com/t */ }
  tr, img {
    page-break-inside: avoid; }
  img {
    max-width: 100% !important; }
  p, h2, h3 {
    orphans: 3;
    widows: 3; }
  h2, h3 {
    page-break-after: avoid; }
  .hide-on-print {
    display: none !important; }
  .print-only {
    display: block !important; }
  .hide-for-print {
    display: none !important; }
  .show-for-print {
    display: inherit !important; } }

meta.foundation-mq-topbar {
  font-family: "/only screen and (min-width:40.063em)/";
  width: 40.063em; }

/* Wrapped around .top-bar to contain to grid width */
.contain-to-grid {
  width: 100%;
  background: #333333; }
  .contain-to-grid .top-bar {
    margin-bottom: 0; }

.fixed {
  width: 100%;
  left: 0;
  position: fixed;
  top: 0;
  z-index: 99; }
  .fixed.expanded:not(.top-bar) {
    overflow-y: auto;
    height: auto;
    width: 100%;
    max-height: 100%; }
    .fixed.expanded:not(.top-bar) .title-area {
      position: fixed;
      width: 100%;
      z-index: 99; }
    .fixed.expanded:not(.top-bar) .top-bar-section {
      z-index: 98;
      margin-top: 45px; }

.top-bar {
  overflow: hidden;
  height: 45px;
  line-height: 45px;
  position: relative;
  background: #333333;
  margin-bottom: 0; }
  .top-bar ul {
    margin-bottom: 0;
    list-style: none; }
  .top-bar .row {
    max-width: none; }
  .top-bar form, .top-bar input {
    margin-bottom: 0; }
  .top-bar input {
    height: auto;
    padding-top: 0.35rem;
    padding-bottom: 0.35rem;
    font-size: 0.75rem; }
  .top-bar .button {
    padding-top: 0.45rem;
    padding-bottom: 0.35rem;
    margin-bottom: 0;
    font-size: 0.75rem; }
  .top-bar .title-area {
    position: relative;
    margin: 0; }
  .top-bar .name {
    height: 45px;
    margin: 0;
    font-size: 16px; }
    .top-bar .name h1 {
      line-height: 45px;
      font-size: 1.0625rem;
      margin: 0; }
      .top-bar .name h1 a {
        font-weight: normal;
        color: white;
        width: 50%;
        display: block;
        padding: 0 15px; }
  .top-bar .toggle-topbar {
    position: absolute;
    right: 0;
    top: 0; }
    .top-bar .toggle-topbar a {
      color: white;
      text-transform: uppercase;
      font-size: 0.8125rem;
      font-weight: bold;
      position: relative;
      display: block;
      padding: 0 15px;
      height: 45px;
      line-height: 45px; }
    .top-bar .toggle-topbar.menu-icon {
      right: 15px;
      top: 50%;
      margin-top: -16px;
      padding-left: 40px; }
      .top-bar .toggle-topbar.menu-icon a {
        text-indent: -48px;
        width: 34px;
        height: 34px;
        line-height: 33px;
        padding: 0;
        color: white; }
        .top-bar .toggle-topbar.menu-icon a span {
          position: absolute;
          right: 0;
          display: block;
          width: 16px;
          height: 0;
          -webkit-box-shadow: 0 10px 0 1px white, 0 16px 0 1px white, 0 22px 0 1px white;
          box-shadow: 0 10px 0 1px white, 0 16px 0 1px white, 0 22px 0 1px white; }
  .top-bar.expanded {
    height: auto;
    background: transparent; }
    .top-bar.expanded .title-area {
      background: #333333; }
    .top-bar.expanded .toggle-topbar a {
      color: #888888; }
      .top-bar.expanded .toggle-topbar a span {
        -webkit-box-shadow: 0 10px 0 1px #888888, 0 16px 0 1px #888888, 0 22px 0 1px #888888;
        box-shadow: 0 10px 0 1px #888888, 0 16px 0 1px #888888, 0 22px 0 1px #888888; }

.top-bar-section {
  left: 0;
  position: relative;
  width: auto;
  -webkit-transition: left 300ms ease-out;
  -moz-transition: left 300ms ease-out;
  transition: left 300ms ease-out; }
  .top-bar-section ul {
    width: 100%;
    height: auto;
    display: block;
    background: #333333;
    font-size: 16px;
    margin: 0; }
  .top-bar-section .divider, .top-bar-section [role="separator"] {
    border-top: solid 1px #1a1a1a;
    clear: both;
    height: 1px;
    width: 100%; }
  .top-bar-section ul li > a {
    display: block;
    width: 100%;
    color: white;
    padding: 12px 0 12px 0;
    padding-left: 15px;
    font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif;
    font-size: 0.8125rem;
    font-weight: normal;
    background: #333333; }
    .top-bar-section ul li > a.button {
      background: #008cba;
      font-size: 0.8125rem;
      padding-right: 15px;
      padding-left: 15px; }
      .top-bar-section ul li > a.button:hover {
        background: #006887; }
    .top-bar-section ul li > a.button.secondary {
      background: #e7e7e7; }
      .top-bar-section ul li > a.button.secondary:hover {
        background: #cecece; }
    .top-bar-section ul li > a.button.success {
      background: #43ac6a; }
      .top-bar-section ul li > a.button.success:hover {
        background: #358753; }
    .top-bar-section ul li > a.button.alert {
      background: #f04124; }
      .top-bar-section ul li > a.button.alert:hover {
        background: #d3290e; }
  .top-bar-section ul li:hover > a {
    background: #272727;
    color: white; }
  .top-bar-section ul li.active > a {
    background: #008cba;
    color: white; }
    .top-bar-section ul li.active > a:hover {
      background: #007ba1; }
  .top-bar-section .has-form {
    padding: 15px; }
  .top-bar-section .has-dropdown {
    position: relative; }
    .top-bar-section .has-dropdown > a:after {
      content: "";
      display: block;
      width: 0;
      height: 0;
      border: inset 5px;
      border-color: transparent transparent transparent rgba(255, 255, 255, 0.4);
      border-left-style: solid;
      margin-right: 15px;
      margin-top: -4.5px;
      position: absolute;
      top: 50%;
      right: 0; }
    .top-bar-section .has-dropdown.moved {
      position: static; }
      .top-bar-section .has-dropdown.moved > .dropdown {
        display: block; }
  .top-bar-section .dropdown {
    position: absolute;
    left: 100%;
    top: 0;
    display: none;
    z-index: 99; }
    .top-bar-section .dropdown li {
      width: 100%;
      height: auto; }
      .top-bar-section .dropdown li a {
        font-weight: normal;
        padding: 8px 15px; }
        .top-bar-section .dropdown li a.parent-link {
          font-weight: normal; }
      .top-bar-section .dropdown li.title h5 {
        margin-bottom: 0; }
        .top-bar-section .dropdown li.title h5 a {
          color: white;
          line-height: 22.5px;
          display: block; }
    .top-bar-section .dropdown label {
      padding: 8px 15px 2px;
      margin-bottom: 0;
      text-transform: uppercase;
      color: #777777;
      font-weight: bold;
      font-size: 0.625rem; }

.js-generated {
  display: block; }

@media only screen and (min-width:40.063em) {
  .top-bar {
    background: #333333;
    *zoom: 1;
    overflow: visible; }
    .top-bar:before, .top-bar:after {
      content: " ";
      display: table; }
    .top-bar:after {
      clear: both; }
    .top-bar .toggle-topbar {
      display: none; }
    .top-bar .title-area {
      float: left; }
    .top-bar .name h1 a {
      width: auto; }
    .top-bar input, .top-bar .button {
      font-size: 0.875rem;
      position: relative;
      top: 7px; }
    .top-bar.expanded {
      background: #333333; }
  .contain-to-grid .top-bar {
    max-width: 62.5rem;
    margin: 0 auto;
    margin-bottom: 0; }
  .top-bar-section {
    -webkit-transition: none 0 0;
    -moz-transition: none 0 0;
    transition: none 0 0;
    left: 0 !important; }
    .top-bar-section ul {
      width: auto;
      height: auto !important;
      display: inline; }
      .top-bar-section ul li {
        float: left; }
        .top-bar-section ul li .js-generated {
          display: none; }
    .top-bar-section li.hover > a:not(.button) {
      background: #272727;
      color: white; }
    .top-bar-section li a:not(.button) {
      padding: 0 15px;
      line-height: 45px;
      background: #333333; }
      .top-bar-section li a:not(.button):hover {
        background: #272727; }
    .top-bar-section .has-dropdown > a {
      padding-right: 35px !important; }
      .top-bar-section .has-dropdown > a:after {
        content: "";
        display: block;
        width: 0;
        height: 0;
        border: inset 5px;
        border-color: rgba(255, 255, 255, 0.4) transparent transparent transparent;
        border-top-style: solid;
        margin-top: -2.5px;
        top: 22.5px; }
    .top-bar-section .has-dropdown.moved {
      position: relative; }
      .top-bar-section .has-dropdown.moved > .dropdown {
        display: none; }
    .top-bar-section .has-dropdown.hover > .dropdown, .top-bar-section .has-dropdown.not-click:hover > .dropdown {
      display: block; }
    .top-bar-section .has-dropdown .dropdown li.has-dropdown > a:after {
      border: none;
      content: "\00bb";
      top: 1rem;
      margin-top: -2px;
      right: 5px; }
    .top-bar-section .dropdown {
      left: 0;
      top: auto;
      background: transparent;
      min-width: 100%; }
      .top-bar-section .dropdown li a {
        color: white;
        line-height: 1;
        white-space: nowrap;
        padding: 12px 15px;
        background: #333333; }
      .top-bar-section .dropdown li label {
        white-space: nowrap;
        background: #333333; }
      .top-bar-section .dropdown li .dropdown {
        left: 100%;
        top: 0; }
    .top-bar-section > ul > .divider, .top-bar-section > ul > [role="separator"] {
      border-bottom: none;
      border-top: none;
      border-right: solid 1px #4d4d4d;
      clear: none;
      height: 45px;
      width: 0; }
    .top-bar-section .has-form {
      background: #333333;
      padding: 0 15px;
      height: 45px; }
    .top-bar-section ul.right li .dropdown {
      left: auto;
      right: 0; }
      .top-bar-section ul.right li .dropdown li .dropdown {
        right: 100%; }
  .no-js .top-bar-section ul li:hover > a {
    background: #272727;
    color: white; }
  .no-js .top-bar-section ul li:active > a {
    background: #008cba;
    color: white; }
  .no-js .top-bar-section .has-dropdown:hover > .dropdown {
    display: block; } }

.off-canvas-wrap, .inner-wrap, nav.tab-bar, .left-off-canvas-menu, .left-off-canvas-menu *, .right-off-canvas-menu, .move-right a.exit-off-canvas, .move-left a.exit-off-canvas {
  -webkit-backface-visibility: hidden; }

.off-canvas-wrap, .inner-wrap {
  position: relative;
  width: 100%; }

.left-off-canvas-menu, .right-off-canvas-menu {
  width: 250px;
  top: 0;
  bottom: 0;
  height: 100%;
  position: absolute;
  overflow-y: auto;
  background: #333333;
  z-index: 1001;
  box-sizing: content-box; }

section.left-small, section.right-small {
  width: 2.8125rem;
  height: 2.8125rem;
  position: absolute;
  top: 0; }

.off-canvas-wrap {
  overflow: hidden; }

.inner-wrap {
  *zoom: 1;
  -webkit-transition: -webkit-transform 500ms ease;
  -moz-transition: -moz-transform 500ms ease;
  -ms-transition: -ms-transform 500ms ease;
  -o-transition: -o-transform 500ms ease;
  transition: transform 500ms ease; }
  .inner-wrap:before, .inner-wrap:after {
    content: " ";
    display: table; }
  .inner-wrap:after {
    clear: both; }

nav.tab-bar {
  background: #333333;
  color: white;
  height: 2.8125rem;
  line-height: 2.8125rem;
  position: relative; }
  nav.tab-bar h1, nav.tab-bar h2, nav.tab-bar h3, nav.tab-bar h4, nav.tab-bar h5, nav.tab-bar h6 {
    color: white;
    font-weight: bold;
    line-height: 2.8125rem;
    margin: 0; }
  nav.tab-bar h1, nav.tab-bar h2, nav.tab-bar h3, nav.tab-bar h4 {
    font-size: 1.125rem; }

section.left-small {
  border-right: solid 1px #1a1a1a;
  box-shadow: 1px 0 0 #4d4d4d;
  left: 0; }

section.right-small {
  border-left: solid 1px #4d4d4d;
  box-shadow: -1px 0 0 #1a1a1a;
  right: 0; }

section.tab-bar-section {
  padding: 0 0.625rem;
  position: absolute;
  text-align: center;
  height: 2.8125rem;
  top: 0; }
  @media only screen and (min-width:40.063em) {
    section.tab-bar-section {
      text-align: left; } }
  section.tab-bar-section.left {
    left: 0;
    right: 2.8125rem; }
  section.tab-bar-section.right {
    left: 2.8125rem;
    right: 0; }
  section.tab-bar-section.middle {
    left: 2.8125rem;
    right: 2.8125rem; }

a.menu-icon {
  text-indent: 2.1875rem;
  width: 2.8125rem;
  height: 2.8125rem;
  display: block;
  line-height: 2.0625rem;
  padding: 0;
  color: white;
  position: relative; }
  a.menu-icon span {
    position: absolute;
    display: block;
    width: 1rem;
    height: 0;
    left: 0.8125rem;
    top: 0.3125rem;
    -webkit-box-shadow: 0 10px 0 1px white, 0 16px 0 1px white, 0 22px 0 1px white;
    box-shadow: 0 10px 0 1px white, 0 16px 0 1px white, 0 22px 0 1px white; }
  a.menu-icon:hover span {
    -webkit-box-shadow: 0 10px 0 1px #b3b3b3, 0 16px 0 1px #b3b3b3, 0 22px 0 1px #b3b3b3;
    box-shadow: 0 10px 0 1px #b3b3b3, 0 16px 0 1px #b3b3b3, 0 22px 0 1px #b3b3b3; }

.left-off-canvas-menu {
  -webkit-transform: translate3d(-100%, 0, 0);
  -moz-transform: translate3d(-100%, 0, 0);
  -ms-transform: translate3d(-100%, 0, 0);
  -o-transform: translate3d(-100%, 0, 0);
  transform: translate3d(-100%, 0, 0); }

.right-off-canvas-menu {
  -webkit-transform: translate3d(100%, 0, 0);
  -moz-transform: translate3d(100%, 0, 0);
  -ms-transform: translate3d(100%, 0, 0);
  -o-transform: translate3d(100%, 0, 0);
  transform: translate3d(100%, 0, 0);
  right: 0; }

ul.off-canvas-list {
  list-style-type: none;
  padding: 0;
  margin: 0; }
  ul.off-canvas-list li label {
    padding: 0.3rem 0.9375rem;
    color: #999999;
    text-transform: uppercase;
    font-weight: bold;
    background: #444444;
    border-top: 1px solid #5e5e5e;
    border-bottom: none;
    margin: 0; }
  ul.off-canvas-list li a {
    display: block;
    padding: 0.66667rem;
    color: rgba(255, 255, 255, 0.7);
    border-bottom: 1px solid #262626; }

.move-right > .inner-wrap {
  -webkit-transform: translate3d(250px, 0, 0);
  -moz-transform: translate3d(250px, 0, 0);
  -ms-transform: translate3d(250px, 0, 0);
  -o-transform: translate3d(250px, 0, 0);
  transform: translate3d(250px, 0, 0); }
.move-right a.exit-off-canvas {
  transition: background 300ms ease;
  cursor: pointer;
  box-shadow: -4px 0 4px rgba(0, 0, 0, 0.5), 4px 0 4px rgba(0, 0, 0, 0.5);
  display: block;
  position: absolute;
  background: rgba(255, 255, 255, 0.2);
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1002; }
  @media only screen and (min-width:40.063em) {
    .move-right a.exit-off-canvas:hover {
      background: rgba(255, 255, 255, 0.05); } }

.move-left > .inner-wrap {
  -webkit-transform: translate3d(-250px, 0, 0);
  -moz-transform: translate3d(-250px, 0, 0);
  -ms-transform: translate3d(-250px, 0, 0);
  -o-transform: translate3d(-250px, 0, 0);
  transform: translate3d(-250px, 0, 0); }
.move-left a.exit-off-canvas {
  transition: background 300ms ease;
  cursor: pointer;
  box-shadow: -4px 0 4px rgba(0, 0, 0, 0.5), 4px 0 4px rgba(0, 0, 0, 0.5);
  display: block;
  position: absolute;
  background: rgba(255, 255, 255, 0.2);
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: 1002; }
  @media only screen and (min-width:40.063em) {
    .move-left a.exit-off-canvas:hover {
      background: rgba(255, 255, 255, 0.05); } }

.lt-ie10 .left-off-canvas-menu {
  left: -250px; }
.lt-ie10 .right-off-canvas-menu {
  right: -250px; }
.lt-ie10 .move-left > .inner-wrap {
  right: 250px; }
.lt-ie10 .move-right > .inner-wrap {
  left: 250px; }

/* Foundation Visibility HTML Classes */
.show-for-small, .show-for-small-only, .show-for-medium-down, .show-for-large-down, .hide-for-medium, .hide-for-medium-up, .hide-for-medium-only, .hide-for-large, .hide-for-large-up, .hide-for-large-only, .hide-for-xlarge, .hide-for-xlarge-up, .hide-for-xlarge-only, .hide-for-xxlarge-up, .hide-for-xxlarge-only {
  display: inherit !important; }

.hide-for-small, .hide-for-small-only, .hide-for-medium-down, .show-for-medium, .show-for-medium-up, .show-for-medium-only, .hide-for-large-down, .show-for-large, .show-for-large-up, .show-for-large-only, .show-for-xlarge, .show-for-xlarge-up, .show-for-xlarge-only, .show-for-xxlarge-up, .show-for-xxlarge-only {
  display: none !important; }

/* Specific visibility for tables */
table.show-for-small, table.show-for-small-only, table.show-for-medium-down, table.show-for-large-down, table.hide-for-medium, table.hide-for-medium-up, table.hide-for-medium-only, table.hide-for-large, table.hide-for-large-up, table.hide-for-large-only, table.hide-for-xlarge, table.hide-for-xlarge-up, table.hide-for-xlarge-only, table.hide-for-xxlarge-up, table.hide-for-xxlarge-only {
  display: table; }

thead.show-for-small, thead.show-for-small-only, thead.show-for-medium-down, thead.show-for-large-down, thead.hide-for-medium, thead.hide-for-medium-up, thead.hide-for-medium-only, thead.hide-for-large, thead.hide-for-large-up, thead.hide-for-large-only, thead.hide-for-xlarge, thead.hide-for-xlarge-up, thead.hide-for-xlarge-only, thead.hide-for-xxlarge-up, thead.hide-for-xxlarge-only {
  display: table-header-group !important; }

tbody.show-for-small, tbody.show-for-small-only, tbody.show-for-medium-down, tbody.show-for-large-down, tbody.hide-for-medium, tbody.hide-for-medium-up, tbody.hide-for-medium-only, tbody.hide-for-large, tbody.hide-for-large-up, tbody.hide-for-large-only, tbody.hide-for-xlarge, tbody.hide-for-xlarge-up, tbody.hide-for-xlarge-only, tbody.hide-for-xxlarge-up, tbody.hide-for-xxlarge-only {
  display: table-row-group !important; }

tr.show-for-small, tr.show-for-small-only, tr.show-for-medium-down, tr.show-for-large-down, tr.hide-for-medium, tr.hide-for-medium-up, tr.hide-for-medium-only, tr.hide-for-large, tr.hide-for-large-up, tr.hide-for-large-only, tr.hide-for-xlarge, tr.hide-for-xlarge-up, tr.hide-for-xlarge-only, tr.hide-for-xxlarge-up, tr.hide-for-xxlarge-only {
  display: table-row !important; }

td.show-for-small, td.show-for-small-only, td.show-for-medium-down td.show-for-large-down, td.hide-for-medium, td.hide-for-medium-up, td.hide-for-large, td.hide-for-large-up, td.hide-for-xlarge td.hide-for-xlarge-up, td.hide-for-xxlarge-up, th.show-for-small, th.show-for-small-only, th.show-for-medium-down th.show-for-large-down, th.hide-for-medium, th.hide-for-medium-up, th.hide-for-large, th.hide-for-large-up, th.hide-for-xlarge th.hide-for-xlarge-up, th.hide-for-xxlarge-up {
  display: table-cell !important; }

/* Medium Displays: 641px and up */
@media only screen and (min-width:40.063em) {
  /* Specific visibility for tables */
  .hide-for-small, .hide-for-small-only, .show-for-medium, .show-for-medium-down, .show-for-medium-up, .show-for-medium-only, .hide-for-large, .hide-for-large-up, .hide-for-large-only, .hide-for-xlarge, .hide-for-xlarge-up, .hide-for-xlarge-only, .hide-for-xxlarge-up, .hide-for-xxlarge-only {
    display: inherit !important; }
  .show-for-small, .show-for-small-only, .hide-for-medium, .hide-for-medium-down, .hide-for-medium-up, .hide-for-medium-only, .hide-for-large-down, .show-for-large, .show-for-large-up, .show-for-large-only, .show-for-xlarge, .show-for-xlarge-up, .show-for-xlarge-only, .show-for-xxlarge-up, .show-for-xxlarge-only {
    display: none !important; }
  table.hide-for-small, table.hide-for-small-only, table.show-for-medium, table.show-for-medium-down, table.show-for-medium-up, table.show-for-medium-only, table.hide-for-large, table.hide-for-large-up, table.hide-for-large-only, table.hide-for-xlarge, table.hide-for-xlarge-up, table.hide-for-xlarge-only, table.hide-for-xxlarge-up, table.hide-for-xxlarge-only {
    display: table; }
  thead.hide-for-small, thead.hide-for-small-only, thead.show-for-medium, thead.show-for-medium-down, thead.show-for-medium-up, thead.show-for-medium-only, thead.hide-for-large, thead.hide-for-large-up, thead.hide-for-large-only, thead.hide-for-xlarge, thead.hide-for-xlarge-up, thead.hide-for-xlarge-only, thead.hide-for-xxlarge-up, thead.hide-for-xxlarge-only {
    display: table-header-group !important; }
  tbody.hide-for-small, tbody.hide-for-small-only, tbody.show-for-medium, tbody.show-for-medium-down, tbody.show-for-medium-up, tbody.show-for-medium-only, tbody.hide-for-large, tbody.hide-for-large-up, tbody.hide-for-large-only, tbody.hide-for-xlarge, tbody.hide-for-xlarge-up, tbody.hide-for-xlarge-only, tbody.hide-for-xxlarge-up, tbody.hide-for-xxlarge-only {
    display: table-row-group !important; }
  tr.hide-for-small, tr.hide-for-small-only, tr.show-for-medium, tr.show-for-medium-down, tr.show-for-medium-up, tr.show-for-medium-only, tr.hide-for-large, tr.hide-for-large-up, tr.hide-for-large-only, tr.hide-for-xlarge, tr.hide-for-xlarge-up, tr.hide-for-xlarge-only, tr.hide-for-xxlarge-up, tr.hide-for-xxlarge-only {
    display: table-row !important; }
  td.hide-for-small, td.hide-for-small-only, td.show-for-medium, td.show-for-medium-down, td.show-for-medium-up, td.show-for-medium-only, td.hide-for-large, td.hide-for-large-up, td.hide-for-large-only, td.hide-for-xlarge, td.hide-for-xlarge-up, td.hide-for-xlarge-only, td.hide-for-xxlarge-up, td.hide-for-xxlarge-only, th.hide-for-small, th.hide-for-small-only, th.show-for-medium, th.show-for-medium-down, th.show-for-medium-up, th.show-for-medium-only, th.hide-for-large, th.hide-for-large-up, th.hide-for-large-only, th.hide-for-xlarge, th.hide-for-xlarge-up, th.hide-for-xlarge-only, th.hide-for-xxlarge-up, th.hide-for-xxlarge-only {
    display: table-cell !important; } }

/* Large Displays: 1024px and up */
@media only screen and (min-width:64.063em) {
  /* Specific visilbity for tables */
  .hide-for-small, .hide-for-small-only, .hide-for-medium, .hide-for-medium-down, .hide-for-medium-only, .show-for-medium-up, .show-for-large, .show-for-large-up, .show-for-large-only, .hide-for-xlarge, .hide-for-xlarge-up, .hide-for-xlarge-only, .hide-for-xxlarge-up, .hide-for-xxlarge-only {
    display: inherit !important; }
  .show-for-small-only, .show-for-medium, .show-for-medium-down, .show-for-medium-only, .hide-for-large, .hide-for-large-up, .hide-for-large-only, .show-for-xlarge, .show-for-xlarge-up, .show-for-xlarge-only, .show-for-xxlarge-up, .show-for-xxlarge-only {
    display: none !important; }
  table.hide-for-small, table.hide-for-small-only, table.hide-for-medium, table.hide-for-medium-down, table.hide-for-medium-only, table.show-for-medium-up, table.show-for-large, table.show-for-large-up, table.show-for-large-only, table.hide-for-xlarge, table.hide-for-xlarge-up, table.hide-for-xlarge-only, table.hide-for-xxlarge-up, table.hide-for-xxlarge-only {
    display: table; }
  thead.hide-for-small, thead.hide-for-small-only, thead.hide-for-medium, thead.hide-for-medium-down, thead.hide-for-medium-only, thead.show-for-medium-up, thead.show-for-large, thead.show-for-large-up, thead.show-for-large-only, thead.hide-for-xlarge, thead.hide-for-xlarge-up, thead.hide-for-xlarge-only, thead.hide-for-xxlarge-up, thead.hide-for-xxlarge-only {
    display: table-header-group !important; }
  tbody.hide-for-small, tbody.hide-for-small-only, tbody.hide-for-medium, tbody.hide-for-medium-down, tbody.hide-for-medium-only, tbody.show-for-medium-up, tbody.show-for-large, tbody.show-for-large-up, tbody.show-for-large-only, tbody.hide-for-xlarge, tbody.hide-for-xlarge-up, tbody.hide-for-xlarge-only, tbody.hide-for-xxlarge-up, tbody.hide-for-xxlarge-only {
    display: table-row-group !important; }
  tr.hide-for-small, tr.hide-for-small-only, tr.hide-for-medium, tr.hide-for-medium-down, tr.hide-for-medium-only, tr.show-for-medium-up, tr.show-for-large, tr.show-for-large-up, tr.show-for-large-only, tr.hide-for-xlarge, tr.hide-for-xlarge-up, tr.hide-for-xlarge-only, tr.hide-for-xxlarge-up, tr.hide-for-xxlarge-only {
    display: table-row !important; }
  td.hide-for-small, td.hide-for-small-only, td.hide-for-medium, td.hide-for-medium-down, td.hide-for-medium-only, td.show-for-medium-up, td.show-for-large, td.show-for-large-up, td.show-for-large-only, td.hide-for-xlarge, td.hide-for-xlarge-up, td.hide-for-xlarge-only, td.hide-for-xxlarge-up, td.hide-for-xxlarge-only, th.hide-for-small, th.hide-for-small-only, th.hide-for-medium, th.hide-for-medium-down, th.hide-for-medium-only, th.show-for-medium-up, th.show-for-large, th.show-for-large-up, th.show-for-large-only, th.hide-for-xlarge, th.hide-for-xlarge-up, th.hide-for-xlarge-only, th.hide-for-xxlarge-up, th.hide-for-xxlarge-only {
    display: table-cell !important; } }

/* X-Large Displays: 1441 and up */
@media only screen and (min-width:90.063em) {
  /* Specific visilbity for tables */
  .hide-for-small, .hide-for-small-only, .hide-for-medium, .hide-for-medium-down, .hide-for-medium-only, .show-for-medium-up, .show-for-large-up, .show-for-xlarge, .show-for-xlarge-up, .show-for-xlarge-only, .hide-for-xxlarge-up, .hide-for-xxlarge-only {
    display: inherit !important; }
  .show-for-small-only, .show-for-medium, .show-for-medium-down, .show-for-medium-only, .show-for-large, .show-for-large-only, .show-for-large-down, .hide-for-xlarge, .hide-for-xlarge-up, .hide-for-xlarge-only, .show-for-xxlarge-up, .show-for-xxlarge-only {
    display: none !important; }
  table.hide-for-small, table.hide-for-small-only, table.hide-for-medium, table.hide-for-medium-down, table.hide-for-medium-only, table.show-for-medium-up, table.show-for-large-up, table.show-for-xlarge, table.show-for-xlarge-up, table.show-for-xlarge-only, table.hide-for-xxlarge-up, table.hide-for-xxlarge-only {
    display: table; }
  thead.hide-for-small, thead.hide-for-small-only, thead.hide-for-medium, thead.hide-for-medium-down, thead.hide-for-medium-only, thead.show-for-medium-up, thead.show-for-large-up, thead.show-for-xlarge, thead.show-for-xlarge-up, thead.show-for-xlarge-only, thead.hide-for-xxlarge-up, thead.hide-for-xxlarge-only {
    display: table-header-group !important; }
  tbody.hide-for-small, tbody.hide-for-small-only, tbody.hide-for-medium, tbody.hide-for-medium-down, tbody.hide-for-medium-only, tbody.show-for-medium-up, tbody.show-for-large-up, tbody.show-for-xlarge, tbody.show-for-xlarge-up, tbody.show-for-xlarge-only, tbody.hide-for-xxlarge-up, tbody.hide-for-xxlarge-only {
    display: table-row-group !important; }
  tr.hide-for-small, tr.hide-for-small-only, tr.hide-for-medium, tr.hide-for-medium-down, tr.hide-for-medium-only, tr.show-for-medium-up, tr.show-for-large-up, tr.show-for-xlarge, tr.show-for-xlarge-up, tr.show-for-xlarge-only, tr.hide-for-xxlarge-up, tr.hide-for-xxlarge-only {
    display: table-row !important; }
  td.hide-for-small, td.hide-for-small-only, td.hide-for-medium, td.hide-for-medium-down, td.hide-for-medium-only, td.show-for-medium-up, td.show-for-large-up, td.show-for-xlarge, td.show-for-xlarge-up, td.show-for-xlarge-only, td.hide-for-xxlarge-up, td.hide-for-xxlarge-only, th.hide-for-small, th.hide-for-small-only, th.hide-for-medium, th.hide-for-medium-down, th.hide-for-medium-only, th.show-for-medium-up, th.show-for-large-up, th.show-for-xlarge, th.show-for-xlarge-up, th.show-for-xlarge-only, th.hide-for-xxlarge-up, th.hide-for-xxlarge-only {
    display: table-cell !important; } }

/* XX-Large Displays: 1920 and up */
@media only screen and (min-width:120.063em) {
  /* Specific visilbity for tables */
  .hide-for-small, .hide-for-small-only, .hide-for-medium, .hide-for-medium-down, .hide-for-medium-only, .show-for-medium-up, .show-for-large-up, .show-for-xlarge-up, .show-for-xxlarge-up, .show-for-xxlarge-only {
    display: inherit !important; }
  .show-for-small-only, .show-for-medium, .show-for-medium-down, .show-for-medium-only, .show-for-large, .show-for-large-only, .show-for-large-down, .hide-for-xlarge, .show-for-xlarge-only, .hide-for-xxlarge-up, .hide-for-xxlarge-only {
    display: none !important; }
  table.hide-for-small, table.hide-for-small-only, table.hide-for-medium, table.hide-for-medium-down, table.hide-for-medium-only, table.show-for-medium-up, table.show-for-large-up, table.show-for-xlarge-up, table.show-for-xxlarge-up, table.show-for-xxlarge-only {
    display: table; }
  thead.hide-for-small, thead.hide-for-small-only, thead.hide-for-medium, thead.hide-for-medium-down, thead.hide-for-medium-only, thead.show-for-medium-up, thead.show-for-large-up, thead.show-for-xlarge-up, thead.show-for-xxlarge-up, thead.show-for-xxlarge-only {
    display: table-header-group !important; }
  tbody.hide-for-small, tbody.hide-for-small-only, tbody.hide-for-medium, tbody.hide-for-medium-down, tbody.hide-for-medium-only, tbody.show-for-medium-up, tbody.show-for-large-up, tbody.show-for-xlarge-up, tbody.show-for-xxlarge-up, tbody.show-for-xxlarge-only {
    display: table-row-group !important; }
  tr.hide-for-small, tr.hide-for-small-only, tr.hide-for-medium, tr.hide-for-medium-down, tr.hide-for-medium-only, tr.show-for-medium-up, tr.show-for-large-up, tr.show-for-xlarge-up, tr.show-for-xxlarge-up, tr.show-for-xxlarge-only {
    display: table-row !important; }
  td.hide-for-small, td.hide-for-small-only, td.hide-for-medium, td.hide-for-medium-down, td.hide-for-medium-only, td.show-for-medium-up, td.show-for-large-up, td.show-for-xlarge-up, td.show-for-xxlarge-up, td.show-for-xxlarge-only, th.hide-for-small, th.hide-for-small-only, th.hide-for-medium, th.hide-for-medium-down, th.hide-for-medium-only, th.show-for-medium-up, th.show-for-large-up, th.show-for-xlarge-up, th.show-for-xxlarge-up, th.show-for-xxlarge-only {
    display: table-cell !important; } }

/* Orientation targeting */
.show-for-landscape, .hide-for-portrait {
  display: inherit !important; }

.hide-for-landscape, .show-for-portrait {
  display: none !important; }

/* Specific visilbity for tables */
table.hide-for-landscape, table.show-for-portrait {
  display: table; }

thead.hide-for-landscape, thead.show-for-portrait {
  display: table-header-group !important; }

tbody.hide-for-landscape, tbody.show-for-portrait {
  display: table-row-group !important; }

tr.hide-for-landscape, tr.show-for-portrait {
  display: table-row !important; }

td.hide-for-landscape, td.show-for-portrait, th.hide-for-landscape, th.show-for-portrait {
  display: table-cell !important; }

@media only screen and (orientation: landscape) {
  /* Specific visilbity for tables */
  .show-for-landscape, .hide-for-portrait {
    display: inherit !important; }
  .hide-for-landscape, .show-for-portrait {
    display: none !important; }
  table.show-for-landscape, table.hide-for-portrait {
    display: table; }
  thead.show-for-landscape, thead.hide-for-portrait {
    display: table-header-group !important; }
  tbody.show-for-landscape, tbody.hide-for-portrait {
    display: table-row-group !important; }
  tr.show-for-landscape, tr.hide-for-portrait {
    display: table-row !important; }
  td.show-for-landscape, td.hide-for-portrait, th.show-for-landscape, th.hide-for-portrait {
    display: table-cell !important; } }

@media only screen and (orientation: portrait) {
  /* Specific visilbity for tables */
  .show-for-portrait, .hide-for-landscape {
    display: inherit !important; }
  .hide-for-portrait, .show-for-landscape {
    display: none !important; }
  table.show-for-portrait, table.hide-for-landscape {
    display: table; }
  thead.show-for-portrait, thead.hide-for-landscape {
    display: table-header-group !important; }
  tbody.show-for-portrait, tbody.hide-for-landscape {
    display: table-row-group !important; }
  tr.show-for-portrait, tr.hide-for-landscape {
    display: table-row !important; }
  td.show-for-portrait, td.hide-for-landscape, th.show-for-portrait, th.hide-for-landscape {
    display: table-cell !important; } }

/* Touch-enabled device targeting */
.show-for-touch {
  display: none !important; }

.hide-for-touch {
  display: inherit !important; }

.touch .show-for-touch {
  display: inherit !important; }

.touch .hide-for-touch {
  display: none !important; }

/* Specific visilbity for tables */
table.hide-for-touch {
  display: table; }

.touch table.show-for-touch {
  display: table; }

thead.hide-for-touch {
  display: table-header-group !important; }

.touch thead.show-for-touch {
  display: table-header-group !important; }

tbody.hide-for-touch {
  display: table-row-group !important; }

.touch tbody.show-for-touch {
  display: table-row-group !important; }

tr.hide-for-touch {
  display: table-row !important; }

.touch tr.show-for-touch {
  display: table-row !important; }

td.hide-for-touch {
  display: table-cell !important; }

.touch td.show-for-touch {
  display: table-cell !important; }

th.hide-for-touch {
  display: table-cell !important; }

.touch th.show-for-touch {
  display: table-cell !important; }
</style>
<script>
/*!
 * Modernizr v2.7.0
 * www.modernizr.com
 *
 * Copyright (c) Faruk Ates, Paul Irish, Alex Sexton
 * Available under the BSD and MIT licenses: www.modernizr.com/license/
 */

/*
 * Modernizr tests which native CSS3 and HTML5 features are available in
 * the current UA and makes the results available to you in two ways:
 * as properties on a global Modernizr object, and as classes on the
 * <html> element. This information allows you to progressively enhance
 * your pages with a granular level of control over the experience.
 *
 * Modernizr has an optional (not included) conditional resource loader
 * called Modernizr.load(), based on Yepnope.js (yepnopejs.com).
 * To get a build that includes Modernizr.load(), as well as choosing
 * which tests to include, go to www.modernizr.com/download/
 *
 * Authors        Faruk Ates, Paul Irish, Alex Sexton
 * Contributors   Ryan Seddon, Ben Alman
 */

window.Modernizr = (function( window, document, undefined ) {

    var version = '2.7.0',

    Modernizr = {},

    /*>>cssclasses*/
    // option for enabling the HTML classes to be added
    enableClasses = true,
    /*>>cssclasses*/

    docElement = document.documentElement,

    /**
     * Create our "modernizr" element that we do most feature tests on.
     */
    mod = 'modernizr',
    modElem = document.createElement(mod),
    mStyle = modElem.style,

    /**
     * Create the input element for various Web Forms feature tests.
     */
    inputElem /*>>inputelem*/ = document.createElement('input') /*>>inputelem*/ ,

    /*>>smile*/
    smile = ':)',
    /*>>smile*/

    toString = {}.toString,

    // TODO :: make the prefixes more granular
    /*>>prefixes*/
    // List of property values to set for css tests. See ticket #21
    prefixes = ' -webkit- -moz- -o- -ms- '.split(' '),
    /*>>prefixes*/

    /*>>domprefixes*/
    // Following spec is to expose vendor-specific style properties as:
    //   elem.style.WebkitBorderRadius
    // and the following would be incorrect:
    //   elem.style.webkitBorderRadius

    // Webkit ghosts their properties in lowercase but Opera & Moz do not.
    // Microsoft uses a lowercase `ms` instead of the correct `Ms` in IE8+
    //   erik.eae.net/archives/2008/03/10/21.48.10/

    // More here: github.com/Modernizr/Modernizr/issues/issue/21
    omPrefixes = 'Webkit Moz O ms',

    cssomPrefixes = omPrefixes.split(' '),

    domPrefixes = omPrefixes.toLowerCase().split(' '),
    /*>>domprefixes*/

    /*>>ns*/
    ns = {'svg': 'http://www.w3.org/2000/svg'},
    /*>>ns*/

    tests = {},
    inputs = {},
    attrs = {},

    classes = [],

    slice = classes.slice,

    featureName, // used in testing loop


    /*>>teststyles*/
    // Inject element with style element and some CSS rules
    injectElementWithStyles = function( rule, callback, nodes, testnames ) {

      var style, ret, node, docOverflow,
          div = document.createElement('div'),
          // After page load injecting a fake body doesn't work so check if body exists
          body = document.body,
          // IE6 and 7 won't return offsetWidth or offsetHeight unless it's in the body element, so we fake it.
          fakeBody = body || document.createElement('body');

      if ( parseInt(nodes, 10) ) {
          // In order not to give false positives we create a node for each test
          // This also allows the method to scale for unspecified uses
          while ( nodes-- ) {
              node = document.createElement('div');
              node.id = testnames ? testnames[nodes] : mod + (nodes + 1);
              div.appendChild(node);
          }
      }

      // <style> elements in IE6-9 are considered 'NoScope' elements and therefore will be removed
      // when injected with innerHTML. To get around this you need to prepend the 'NoScope' element
      // with a 'scoped' element, in our case the soft-hyphen entity as it won't mess with our measurements.
      // msdn.microsoft.com/en-us/library/ms533897%28VS.85%29.aspx
      // Documents served as xml will throw if using &shy; so use xml friendly encoded version. See issue #277
      style = ['&#173;','<style id="s', mod, '">', rule, '</style>'].join('');
      div.id = mod;
      // IE6 will false positive on some tests due to the style element inside the test div somehow interfering offsetHeight, so insert it into body or fakebody.
      // Opera will act all quirky when injecting elements in documentElement when page is served as xml, needs fakebody too. #270
      (body ? div : fakeBody).innerHTML += style;
      fakeBody.appendChild(div);
      if ( !body ) {
          //avoid crashing IE8, if background image is used
          fakeBody.style.background = '';
          //Safari 5.13/5.1.4 OSX stops loading if ::-webkit-scrollbar is used and scrollbars are visible
          fakeBody.style.overflow = 'hidden';
          docOverflow = docElement.style.overflow;
          docElement.style.overflow = 'hidden';
          docElement.appendChild(fakeBody);
      }

      ret = callback(div, rule);
      // If this is done after page load we don't want to remove the body so check if body exists
      if ( !body ) {
          fakeBody.parentNode.removeChild(fakeBody);
          docElement.style.overflow = docOverflow;
      } else {
          div.parentNode.removeChild(div);
      }

      return !!ret;

    },
    /*>>teststyles*/

    /*>>mq*/
    // adapted from matchMedia polyfill
    // by Scott Jehl and Paul Irish
    // gist.github.com/786768
    testMediaQuery = function( mq ) {

      var matchMedia = window.matchMedia || window.msMatchMedia;
      if ( matchMedia ) {
        return matchMedia(mq).matches;
      }

      var bool;

      injectElementWithStyles('@media ' + mq + ' { #' + mod + ' { position: absolute; } }', function( node ) {
        bool = (window.getComputedStyle ?
                  getComputedStyle(node, null) :
                  node.currentStyle)['position'] == 'absolute';
      });

      return bool;

     },
     /*>>mq*/


    /*>>hasevent*/
    //
    // isEventSupported determines if a given element supports the given event
    // kangax.github.com/iseventsupported/
    //
    // The following results are known incorrects:
    //   Modernizr.hasEvent("webkitTransitionEnd", elem) // false negative
    //   Modernizr.hasEvent("textInput") // in Webkit. github.com/Modernizr/Modernizr/issues/333
    //   ...
    isEventSupported = (function() {

      var TAGNAMES = {
        'select': 'input', 'change': 'input',
        'submit': 'form', 'reset': 'form',
        'error': 'img', 'load': 'img', 'abort': 'img'
      };

      function isEventSupported( eventName, element ) {

        element = element || document.createElement(TAGNAMES[eventName] || 'div');
        eventName = 'on' + eventName;

        // When using `setAttribute`, IE skips "unload", WebKit skips "unload" and "resize", whereas `in` "catches" those
        var isSupported = eventName in element;

        if ( !isSupported ) {
          // If it has no `setAttribute` (i.e. doesn't implement Node interface), try generic element
          if ( !element.setAttribute ) {
            element = document.createElement('div');
          }
          if ( element.setAttribute && element.removeAttribute ) {
            element.setAttribute(eventName, '');
            isSupported = is(element[eventName], 'function');

            // If property was created, "remove it" (by setting value to `undefined`)
            if ( !is(element[eventName], 'undefined') ) {
              element[eventName] = undefined;
            }
            element.removeAttribute(eventName);
          }
        }

        element = null;
        return isSupported;
      }
      return isEventSupported;
    })(),
    /*>>hasevent*/

    // TODO :: Add flag for hasownprop ? didn't last time

    // hasOwnProperty shim by kangax needed for Safari 2.0 support
    _hasOwnProperty = ({}).hasOwnProperty, hasOwnProp;

    if ( !is(_hasOwnProperty, 'undefined') && !is(_hasOwnProperty.call, 'undefined') ) {
      hasOwnProp = function (object, property) {
        return _hasOwnProperty.call(object, property);
      };
    }
    else {
      hasOwnProp = function (object, property) { /* yes, this can give false positives/negatives, but most of the time we don't care about those */
        return ((property in object) && is(object.constructor.prototype[property], 'undefined'));
      };
    }

    // Adapted from ES5-shim https://github.com/kriskowal/es5-shim/blob/master/es5-shim.js
    // es5.github.com/#x15.3.4.5

    if (!Function.prototype.bind) {
      Function.prototype.bind = function bind(that) {

        var target = this;

        if (typeof target != "function") {
            throw new TypeError();
        }

        var args = slice.call(arguments, 1),
            bound = function () {

            if (this instanceof bound) {

              var F = function(){};
              F.prototype = target.prototype;
              var self = new F();

              var result = target.apply(
                  self,
                  args.concat(slice.call(arguments))
              );
              if (Object(result) === result) {
                  return result;
              }
              return self;

            } else {

              return target.apply(
                  that,
                  args.concat(slice.call(arguments))
              );

            }

        };

        return bound;
      };
    }

    /**
     * setCss applies given styles to the Modernizr DOM node.
     */
    function setCss( str ) {
        mStyle.cssText = str;
    }

    /**
     * setCssAll extrapolates all vendor-specific css strings.
     */
    function setCssAll( str1, str2 ) {
        return setCss(prefixes.join(str1 + ';') + ( str2 || '' ));
    }

    /**
     * is returns a boolean for if typeof obj is exactly type.
     */
    function is( obj, type ) {
        return typeof obj === type;
    }

    /**
     * contains returns a boolean for if substr is found within str.
     */
    function contains( str, substr ) {
        return !!~('' + str).indexOf(substr);
    }

    /*>>testprop*/

    // testProps is a generic CSS / DOM property test.

    // In testing support for a given CSS property, it's legit to test:
    //    `elem.style[styleName] !== undefined`
    // If the property is supported it will return an empty string,
    // if unsupported it will return undefined.

    // We'll take advantage of this quick test and skip setting a style
    // on our modernizr element, but instead just testing undefined vs
    // empty string.

    // Because the testing of the CSS property names (with "-", as
    // opposed to the camelCase DOM properties) is non-portable and
    // non-standard but works in WebKit and IE (but not Gecko or Opera),
    // we explicitly reject properties with dashes so that authors
    // developing in WebKit or IE first don't end up with
    // browser-specific content by accident.

    function testProps( props, prefixed ) {
        for ( var i in props ) {
            var prop = props[i];
            if ( !contains(prop, "-") && mStyle[prop] !== undefined ) {
                return prefixed == 'pfx' ? prop : true;
            }
        }
        return false;
    }
    /*>>testprop*/

    // TODO :: add testDOMProps
    /**
     * testDOMProps is a generic DOM property test; if a browser supports
     *   a certain property, it won't return undefined for it.
     */
    function testDOMProps( props, obj, elem ) {
        for ( var i in props ) {
            var item = obj[props[i]];
            if ( item !== undefined) {

                // return the property name as a string
                if (elem === false) return props[i];

                // let's bind a function
                if (is(item, 'function')){
                  // default to autobind unless override
                  return item.bind(elem || obj);
                }

                // return the unbound function or obj or value
                return item;
            }
        }
        return false;
    }

    /*>>testallprops*/
    /**
     * testPropsAll tests a list of DOM properties we want to check against.
     *   We specify literally ALL possible (known and/or likely) properties on
     *   the element including the non-vendor prefixed one, for forward-
     *   compatibility.
     */
    function testPropsAll( prop, prefixed, elem ) {

        var ucProp  = prop.charAt(0).toUpperCase() + prop.slice(1),
            props   = (prop + ' ' + cssomPrefixes.join(ucProp + ' ') + ucProp).split(' ');

        // did they call .prefixed('boxSizing') or are we just testing a prop?
        if(is(prefixed, "string") || is(prefixed, "undefined")) {
          return testProps(props, prefixed);

        // otherwise, they called .prefixed('requestAnimationFrame', window[, elem])
        } else {
          props = (prop + ' ' + (domPrefixes).join(ucProp + ' ') + ucProp).split(' ');
          return testDOMProps(props, prefixed, elem);
        }
    }
    /*>>testallprops*/


    /**
     * Tests
     * -----
     */

    // The *new* flexbox
    // dev.w3.org/csswg/css3-flexbox

    tests['flexbox'] = function() {
      return testPropsAll('flexWrap');
    };

    // The *old* flexbox
    // www.w3.org/TR/2009/WD-css3-flexbox-20090723/

    tests['flexboxlegacy'] = function() {
        return testPropsAll('boxDirection');
    };

    // On the S60 and BB Storm, getContext exists, but always returns undefined
    // so we actually have to call getContext() to verify
    // github.com/Modernizr/Modernizr/issues/issue/97/

    tests['canvas'] = function() {
        var elem = document.createElement('canvas');
        return !!(elem.getContext && elem.getContext('2d'));
    };

    tests['canvastext'] = function() {
        return !!(Modernizr['canvas'] && is(document.createElement('canvas').getContext('2d').fillText, 'function'));
    };

    // webk.it/70117 is tracking a legit WebGL feature detect proposal

    // We do a soft detect which may false positive in order to avoid
    // an expensive context creation: bugzil.la/732441

    tests['webgl'] = function() {
        return !!window.WebGLRenderingContext;
    };

    /*
     * The Modernizr.touch test only indicates if the browser supports
     *    touch events, which does not necessarily reflect a touchscreen
     *    device, as evidenced by tablets running Windows 7 or, alas,
     *    the Palm Pre / WebOS (touch) phones.
     *
     * Additionally, Chrome (desktop) used to lie about its support on this,
     *    but that has since been rectified: crbug.com/36415
     *
     * We also test for Firefox 4 Multitouch Support.
     *
     * For more info, see: modernizr.github.com/Modernizr/touch.html
     */

    tests['touch'] = function() {
        var bool;

        if(('ontouchstart' in window) || window.DocumentTouch && document instanceof DocumentTouch) {
          bool = true;
        } else {
          injectElementWithStyles(['@media (',prefixes.join('touch-enabled),('),mod,')','{#modernizr{top:9px;position:absolute}}'].join(''), function( node ) {
            bool = node.offsetTop === 9;
          });
        }

        return bool;
    };


    // geolocation is often considered a trivial feature detect...
    // Turns out, it's quite tricky to get right:
    //
    // Using !!navigator.geolocation does two things we don't want. It:
    //   1. Leaks memory in IE9: github.com/Modernizr/Modernizr/issues/513
    //   2. Disables page caching in WebKit: webk.it/43956
    //
    // Meanwhile, in Firefox < 8, an about:config setting could expose
    // a false positive that would throw an exception: bugzil.la/688158

    tests['geolocation'] = function() {
        return 'geolocation' in navigator;
    };


    tests['postmessage'] = function() {
      return !!window.postMessage;
    };


    // Chrome incognito mode used to throw an exception when using openDatabase
    // It doesn't anymore.
    tests['websqldatabase'] = function() {
      return !!window.openDatabase;
    };

    // Vendors had inconsistent prefixing with the experimental Indexed DB:
    // - Webkit's implementation is accessible through webkitIndexedDB
    // - Firefox shipped moz_indexedDB before FF4b9, but since then has been mozIndexedDB
    // For speed, we don't test the legacy (and beta-only) indexedDB
    tests['indexedDB'] = function() {
      return !!testPropsAll("indexedDB", window);
    };

    // documentMode logic from YUI to filter out IE8 Compat Mode
    //   which false positives.
    tests['hashchange'] = function() {
      return isEventSupported('hashchange', window) && (document.documentMode === undefined || document.documentMode > 7);
    };

    // Per 1.6:
    // This used to be Modernizr.historymanagement but the longer
    // name has been deprecated in favor of a shorter and property-matching one.
    // The old API is still available in 1.6, but as of 2.0 will throw a warning,
    // and in the first release thereafter disappear entirely.
    tests['history'] = function() {
      return !!(window.history && history.pushState);
    };

    tests['draganddrop'] = function() {
        var div = document.createElement('div');
        return ('draggable' in div) || ('ondragstart' in div && 'ondrop' in div);
    };

    // FF3.6 was EOL'ed on 4/24/12, but the ESR version of FF10
    // will be supported until FF19 (2/12/13), at which time, ESR becomes FF17.
    // FF10 still uses prefixes, so check for it until then.
    // for more ESR info, see: mozilla.org/en-US/firefox/organizations/faq/
    tests['websockets'] = function() {
        return 'WebSocket' in window || 'MozWebSocket' in window;
    };


    // css-tricks.com/rgba-browser-support/
    tests['rgba'] = function() {
        // Set an rgba() color and check the returned value

        setCss('background-color:rgba(150,255,150,.5)');

        return contains(mStyle.backgroundColor, 'rgba');
    };

    tests['hsla'] = function() {
        // Same as rgba(), in fact, browsers re-map hsla() to rgba() internally,
        //   except IE9 who retains it as hsla

        setCss('background-color:hsla(120,40%,100%,.5)');

        return contains(mStyle.backgroundColor, 'rgba') || contains(mStyle.backgroundColor, 'hsla');
    };

    tests['multiplebgs'] = function() {
        // Setting multiple images AND a color on the background shorthand property
        //  and then querying the style.background property value for the number of
        //  occurrences of "url(" is a reliable method for detecting ACTUAL support for this!

        setCss('background:url(https://),url(https://),red url(https://)');

        // If the UA supports multiple backgrounds, there should be three occurrences
        //   of the string "url(" in the return value for elemStyle.background

        return (/(url\s*\(.*?){3}/).test(mStyle.background);
    };



    // this will false positive in Opera Mini
    //   github.com/Modernizr/Modernizr/issues/396

    tests['backgroundsize'] = function() {
        return testPropsAll('backgroundSize');
    };

    tests['borderimage'] = function() {
        return testPropsAll('borderImage');
    };


    // Super comprehensive table about all the unique implementations of
    // border-radius: muddledramblings.com/table-of-css3-border-radius-compliance

    tests['borderradius'] = function() {
        return testPropsAll('borderRadius');
    };

    // WebOS unfortunately false positives on this test.
    tests['boxshadow'] = function() {
        return testPropsAll('boxShadow');
    };

    // FF3.0 will false positive on this test
    tests['textshadow'] = function() {
        return document.createElement('div').style.textShadow === '';
    };


    tests['opacity'] = function() {
        // Browsers that actually have CSS Opacity implemented have done so
        //  according to spec, which means their return values are within the
        //  range of [0.0,1.0] - including the leading zero.

        setCssAll('opacity:.55');

        // The non-literal . in this regex is intentional:
        //   German Chrome returns this value as 0,55
        // github.com/Modernizr/Modernizr/issues/#issue/59/comment/516632
        return (/^0.55$/).test(mStyle.opacity);
    };


    // Note, Android < 4 will pass this test, but can only animate
    //   a single property at a time
    //   daneden.me/2011/12/putting-up-with-androids-bullshit/
    tests['cssanimations'] = function() {
        return testPropsAll('animationName');
    };


    tests['csscolumns'] = function() {
        return testPropsAll('columnCount');
    };


    tests['cssgradients'] = function() {
        /**
         * For CSS Gradients syntax, please see:
         * webkit.org/blog/175/introducing-css-gradients/
         * developer.mozilla.org/en/CSS/-moz-linear-gradient
         * developer.mozilla.org/en/CSS/-moz-radial-gradient
         * dev.w3.org/csswg/css3-images/#gradients-
         */

        var str1 = 'background-image:',
            str2 = 'gradient(linear,left top,right bottom,from(#9f9),to(white));',
            str3 = 'linear-gradient(left top,#9f9, white);';

        setCss(
             // legacy webkit syntax (FIXME: remove when syntax not in use anymore)
              (str1 + '-webkit- '.split(' ').join(str2 + str1) +
             // standard syntax             // trailing 'background-image:'
              prefixes.join(str3 + str1)).slice(0, -str1.length)
        );

        return contains(mStyle.backgroundImage, 'gradient');
    };


    tests['cssreflections'] = function() {
        return testPropsAll('boxReflect');
    };


    tests['csstransforms'] = function() {
        return !!testPropsAll('transform');
    };


    tests['csstransforms3d'] = function() {

        var ret = !!testPropsAll('perspective');

        // Webkit's 3D transforms are passed off to the browser's own graphics renderer.
        //   It works fine in Safari on Leopard and Snow Leopard, but not in Chrome in
        //   some conditions. As a result, Webkit typically recognizes the syntax but
        //   will sometimes throw a false positive, thus we must do a more thorough check:
        if ( ret && 'webkitPerspective' in docElement.style ) {

          // Webkit allows this media query to succeed only if the feature is enabled.
          // `@media (transform-3d),(-webkit-transform-3d){ ... }`
          injectElementWithStyles('@media (transform-3d),(-webkit-transform-3d){#modernizr{left:9px;position:absolute;height:3px;}}', function( node, rule ) {
            ret = node.offsetLeft === 9 && node.offsetHeight === 3;
          });
        }
        return ret;
    };


    tests['csstransitions'] = function() {
        return testPropsAll('transition');
    };


    /*>>fontface*/
    // @font-face detection routine by Diego Perini
    // javascript.nwbox.com/CSSSupport/

    // false positives:
    //   WebOS github.com/Modernizr/Modernizr/issues/342
    //   WP7   github.com/Modernizr/Modernizr/issues/538
    tests['fontface'] = function() {
        var bool;

        injectElementWithStyles('@font-face {font-family:"font";src:url("https://")}', function( node, rule ) {
          var style = document.getElementById('smodernizr'),
              sheet = style.sheet || style.styleSheet,
              cssText = sheet ? (sheet.cssRules && sheet.cssRules[0] ? sheet.cssRules[0].cssText : sheet.cssText || '') : '';

          bool = /src/i.test(cssText) && cssText.indexOf(rule.split(' ')[0]) === 0;
        });

        return bool;
    };
    /*>>fontface*/

    // CSS generated content detection
    tests['generatedcontent'] = function() {
        var bool;

        injectElementWithStyles(['#',mod,'{font:0/0 a}#',mod,':after{content:"',smile,'";visibility:hidden;font:3px/1 a}'].join(''), function( node ) {
          bool = node.offsetHeight >= 3;
        });

        return bool;
    };



    // These tests evaluate support of the video/audio elements, as well as
    // testing what types of content they support.
    //
    // We're using the Boolean constructor here, so that we can extend the value
    // e.g.  Modernizr.video     // true
    //       Modernizr.video.ogg // 'probably'
    //
    // Codec values from : github.com/NielsLeenheer/html5test/blob/9106a8/index.html#L845
    //                     thx to NielsLeenheer and zcorpan

    // Note: in some older browsers, "no" was a return value instead of empty string.
    //   It was live in FF3.5.0 and 3.5.1, but fixed in 3.5.2
    //   It was also live in Safari 4.0.0 - 4.0.4, but fixed in 4.0.5

    tests['video'] = function() {
        var elem = document.createElement('video'),
            bool = false;

        // IE9 Running on Windows Server SKU can cause an exception to be thrown, bug #224
        try {
            if ( bool = !!elem.canPlayType ) {
                bool      = new Boolean(bool);
                bool.ogg  = elem.canPlayType('video/ogg; codecs="theora"')      .replace(/^no$/,'');

                // Without QuickTime, this value will be `undefined`. github.com/Modernizr/Modernizr/issues/546
                bool.h264 = elem.canPlayType('video/mp4; codecs="avc1.42E01E"') .replace(/^no$/,'');

                bool.webm = elem.canPlayType('video/webm; codecs="vp8, vorbis"').replace(/^no$/,'');
            }

        } catch(e) { }

        return bool;
    };

    tests['audio'] = function() {
        var elem = document.createElement('audio'),
            bool = false;

        try {
            if ( bool = !!elem.canPlayType ) {
                bool      = new Boolean(bool);
                bool.ogg  = elem.canPlayType('audio/ogg; codecs="vorbis"').replace(/^no$/,'');
                bool.mp3  = elem.canPlayType('audio/mpeg;')               .replace(/^no$/,'');

                // Mimetypes accepted:
                //   developer.mozilla.org/En/Media_formats_supported_by_the_audio_and_video_elements
                //   bit.ly/iphoneoscodecs
                bool.wav  = elem.canPlayType('audio/wav; codecs="1"')     .replace(/^no$/,'');
                bool.m4a  = ( elem.canPlayType('audio/x-m4a;')            ||
                              elem.canPlayType('audio/aac;'))             .replace(/^no$/,'');
            }
        } catch(e) { }

        return bool;
    };


    // In FF4, if disabled, window.localStorage should === null.

    // Normally, we could not test that directly and need to do a
    //   `('localStorage' in window) && ` test first because otherwise Firefox will
    //   throw bugzil.la/365772 if cookies are disabled

    // Also in iOS5 Private Browsing mode, attempting to use localStorage.setItem
    // will throw the exception:
    //   QUOTA_EXCEEDED_ERRROR DOM Exception 22.
    // Peculiarly, getItem and removeItem calls do not throw.

    // Because we are forced to try/catch this, we'll go aggressive.

    // Just FWIW: IE8 Compat mode supports these features completely:
    //   www.quirksmode.org/dom/html5.html
    // But IE8 doesn't support either with local files

    tests['localstorage'] = function() {
        try {
            localStorage.setItem(mod, mod);
            localStorage.removeItem(mod);
            return true;
        } catch(e) {
            return false;
        }
    };

    tests['sessionstorage'] = function() {
        try {
            sessionStorage.setItem(mod, mod);
            sessionStorage.removeItem(mod);
            return true;
        } catch(e) {
            return false;
        }
    };


    tests['webworkers'] = function() {
        return !!window.Worker;
    };


    tests['applicationcache'] = function() {
        return !!window.applicationCache;
    };


    // Thanks to Erik Dahlstrom
    tests['svg'] = function() {
        return !!document.createElementNS && !!document.createElementNS(ns.svg, 'svg').createSVGRect;
    };

    // specifically for SVG inline in HTML, not within XHTML
    // test page: paulirish.com/demo/inline-svg
    tests['inlinesvg'] = function() {
      var div = document.createElement('div');
      div.innerHTML = '<svg/>';
      return (div.firstChild && div.firstChild.namespaceURI) == ns.svg;
    };

    // SVG SMIL animation
    tests['smil'] = function() {
        return !!document.createElementNS && /SVGAnimate/.test(toString.call(document.createElementNS(ns.svg, 'animate')));
    };

    // This test is only for clip paths in SVG proper, not clip paths on HTML content
    // demo: srufaculty.sru.edu/david.dailey/svg/newstuff/clipPath4.svg

    // However read the comments to dig into applying SVG clippaths to HTML content here:
    //   github.com/Modernizr/Modernizr/issues/213#issuecomment-1149491
    tests['svgclippaths'] = function() {
        return !!document.createElementNS && /SVGClipPath/.test(toString.call(document.createElementNS(ns.svg, 'clipPath')));
    };

    /*>>webforms*/
    // input features and input types go directly onto the ret object, bypassing the tests loop.
    // Hold this guy to execute in a moment.
    function webforms() {
        /*>>input*/
        // Run through HTML5's new input attributes to see if the UA understands any.
        // We're using f which is the <input> element created early on
        // Mike Taylr has created a comprehensive resource for testing these attributes
        //   when applied to all input types:
        //   miketaylr.com/code/input-type-attr.html
        // spec: www.whatwg.org/specs/web-apps/current-work/multipage/the-input-element.html#input-type-attr-summary

        // Only input placeholder is tested while textarea's placeholder is not.
        // Currently Safari 4 and Opera 11 have support only for the input placeholder
        // Both tests are available in feature-detects/forms-placeholder.js
        Modernizr['input'] = (function( props ) {
            for ( var i = 0, len = props.length; i < len; i++ ) {
                attrs[ props[i] ] = !!(props[i] in inputElem);
            }
            if (attrs.list){
              // safari false positive's on datalist: webk.it/74252
              // see also github.com/Modernizr/Modernizr/issues/146
              attrs.list = !!(document.createElement('datalist') && window.HTMLDataListElement);
            }
            return attrs;
        })('autocomplete autofocus list placeholder max min multiple pattern required step'.split(' '));
        /*>>input*/

        /*>>inputtypes*/
        // Run through HTML5's new input types to see if the UA understands any.
        //   This is put behind the tests runloop because it doesn't return a
        //   true/false like all the other tests; instead, it returns an object
        //   containing each input type with its corresponding true/false value

        // Big thanks to @miketaylr for the html5 forms expertise. miketaylr.com/
        Modernizr['inputtypes'] = (function(props) {

            for ( var i = 0, bool, inputElemType, defaultView, len = props.length; i < len; i++ ) {

                inputElem.setAttribute('type', inputElemType = props[i]);
                bool = inputElem.type !== 'text';

                // We first check to see if the type we give it sticks..
                // If the type does, we feed it a textual value, which shouldn't be valid.
                // If the value doesn't stick, we know there's input sanitization which infers a custom UI
                if ( bool ) {

                    inputElem.value         = smile;
                    inputElem.style.cssText = 'position:absolute;visibility:hidden;';

                    if ( /^range$/.test(inputElemType) && inputElem.style.WebkitAppearance !== undefined ) {

                      docElement.appendChild(inputElem);
                      defaultView = document.defaultView;

                      // Safari 2-4 allows the smiley as a value, despite making a slider
                      bool =  defaultView.getComputedStyle &&
                              defaultView.getComputedStyle(inputElem, null).WebkitAppearance !== 'textfield' &&
                              // Mobile android web browser has false positive, so must
                              // check the height to see if the widget is actually there.
                              (inputElem.offsetHeight !== 0);

                      docElement.removeChild(inputElem);

                    } else if ( /^(search|tel)$/.test(inputElemType) ){
                      // Spec doesn't define any special parsing or detectable UI
                      //   behaviors so we pass these through as true

                      // Interestingly, opera fails the earlier test, so it doesn't
                      //  even make it here.

                    } else if ( /^(url|email)$/.test(inputElemType) ) {
                      // Real url and email support comes with prebaked validation.
                      bool = inputElem.checkValidity && inputElem.checkValidity() === false;

                    } else {
                      // If the upgraded input compontent rejects the :) text, we got a winner
                      bool = inputElem.value != smile;
                    }
                }

                inputs[ props[i] ] = !!bool;
            }
            return inputs;
        })('search tel url email datetime date month week time datetime-local number range color'.split(' '));
        /*>>inputtypes*/
    }
    /*>>webforms*/


    // End of test definitions
    // -----------------------



    // Run through all tests and detect their support in the current UA.
    // todo: hypothetically we could be doing an array of tests and use a basic loop here.
    for ( var feature in tests ) {
        if ( hasOwnProp(tests, feature) ) {
            // run the test, throw the return value into the Modernizr,
            //   then based on that boolean, define an appropriate className
            //   and push it into an array of classes we'll join later.
            featureName  = feature.toLowerCase();
            Modernizr[featureName] = tests[feature]();

            classes.push((Modernizr[featureName] ? '' : 'no-') + featureName);
        }
    }

    /*>>webforms*/
    // input tests need to run.
    Modernizr.input || webforms();
    /*>>webforms*/


    /**
     * addTest allows the user to define their own feature tests
     * the result will be added onto the Modernizr object,
     * as well as an appropriate className set on the html element
     *
     * @param feature - String naming the feature
     * @param test - Function returning true if feature is supported, false if not
     */
     Modernizr.addTest = function ( feature, test ) {
       if ( typeof feature == 'object' ) {
         for ( var key in feature ) {
           if ( hasOwnProp( feature, key ) ) {
             Modernizr.addTest( key, feature[ key ] );
           }
         }
       } else {

         feature = feature.toLowerCase();

         if ( Modernizr[feature] !== undefined ) {
           // we're going to quit if you're trying to overwrite an existing test
           // if we were to allow it, we'd do this:
           //   var re = new RegExp("\b(no-)?" + feature + "\b");
           //   docElement.className = docElement.className.replace( re, '' );
           // but, no rly, stuff 'em.
           return Modernizr;
         }

         test = typeof test == 'function' ? test() : test;

         if (typeof enableClasses !== "undefined" && enableClasses) {
           docElement.className += ' ' + (test ? '' : 'no-') + feature;
         }
         Modernizr[feature] = test;

       }

       return Modernizr; // allow chaining.
     };


    // Reset modElem.cssText to nothing to reduce memory footprint.
    setCss('');
    modElem = inputElem = null;

    /*>>shiv*/
    /**
     * @preserve HTML5 Shiv prev3.7.1 | @afarkas @jdalton @jon_neal @rem | MIT/GPL2 Licensed
     */
    ;(function(window, document) {
        /*jshint evil:true */
        /** version */
        var version = '3.7.0';

        /** Preset options */
        var options = window.html5 || {};

        /** Used to skip problem elements */
        var reSkip = /^<|^(?:button|map|select|textarea|object|iframe|option|optgroup)$/i;

        /** Not all elements can be cloned in IE **/
        var saveClones = /^(?:a|b|code|div|fieldset|h1|h2|h3|h4|h5|h6|i|label|li|ol|p|q|span|strong|style|table|tbody|td|th|tr|ul)$/i;

        /** Detect whether the browser supports default html5 styles */
        var supportsHtml5Styles;

        /** Name of the expando, to work with multiple documents or to re-shiv one document */
        var expando = '_html5shiv';

        /** The id for the the documents expando */
        var expanID = 0;

        /** Cached data for each document */
        var expandoData = {};

        /** Detect whether the browser supports unknown elements */
        var supportsUnknownElements;

        (function() {
          try {
            var a = document.createElement('a');
            a.innerHTML = '<xyz></xyz>';
            //if the hidden property is implemented we can assume, that the browser supports basic HTML5 Styles
            supportsHtml5Styles = ('hidden' in a);

            supportsUnknownElements = a.childNodes.length == 1 || (function() {
              // assign a false positive if unable to shiv
              (document.createElement)('a');
              var frag = document.createDocumentFragment();
              return (
                typeof frag.cloneNode == 'undefined' ||
                typeof frag.createDocumentFragment == 'undefined' ||
                typeof frag.createElement == 'undefined'
              );
            }());
          } catch(e) {
            // assign a false positive if detection fails => unable to shiv
            supportsHtml5Styles = true;
            supportsUnknownElements = true;
          }

        }());

        /*--------------------------------------------------------------------------*/

        /**
         * Creates a style sheet with the given CSS text and adds it to the document.
         * @private
         * @param {Document} ownerDocument The document.
         * @param {String} cssText The CSS text.
         * @returns {StyleSheet} The style element.
         */
        function addStyleSheet(ownerDocument, cssText) {
          var p = ownerDocument.createElement('p'),
          parent = ownerDocument.getElementsByTagName('head')[0] || ownerDocument.documentElement;

          p.innerHTML = 'x<style>' + cssText + '</style>';
          return parent.insertBefore(p.lastChild, parent.firstChild);
        }

        /**
         * Returns the value of `html5.elements` as an array.
         * @private
         * @returns {Array} An array of shived element node names.
         */
        function getElements() {
          var elements = html5.elements;
          return typeof elements == 'string' ? elements.split(' ') : elements;
        }

        /**
         * Returns the data associated to the given document
         * @private
         * @param {Document} ownerDocument The document.
         * @returns {Object} An object of data.
         */
        function getExpandoData(ownerDocument) {
          var data = expandoData[ownerDocument[expando]];
          if (!data) {
            data = {};
            expanID++;
            ownerDocument[expando] = expanID;
            expandoData[expanID] = data;
          }
          return data;
        }

        /**
         * returns a shived element for the given nodeName and document
         * @memberOf html5
         * @param {String} nodeName name of the element
         * @param {Document} ownerDocument The context document.
         * @returns {Object} The shived element.
         */
        function createElement(nodeName, ownerDocument, data){
          if (!ownerDocument) {
            ownerDocument = document;
          }
          if(supportsUnknownElements){
            return ownerDocument.createElement(nodeName);
          }
          if (!data) {
            data = getExpandoData(ownerDocument);
          }
          var node;

          if (data.cache[nodeName]) {
            node = data.cache[nodeName].cloneNode();
          } else if (saveClones.test(nodeName)) {
            node = (data.cache[nodeName] = data.createElem(nodeName)).cloneNode();
          } else {
            node = data.createElem(nodeName);
          }

          // Avoid adding some elements to fragments in IE < 9 because
          // * Attributes like `name` or `type` cannot be set/changed once an element
          //   is inserted into a document/fragment
          // * Link elements with `src` attributes that are inaccessible, as with
          //   a 403 response, will cause the tab/window to crash
          // * Script elements appended to fragments will execute when their `src`
          //   or `text` property is set
          return node.canHaveChildren && !reSkip.test(nodeName) && !node.tagUrn ? data.frag.appendChild(node) : node;
        }

        /**
         * returns a shived DocumentFragment for the given document
         * @memberOf html5
         * @param {Document} ownerDocument The context document.
         * @returns {Object} The shived DocumentFragment.
         */
        function createDocumentFragment(ownerDocument, data){
          if (!ownerDocument) {
            ownerDocument = document;
          }
          if(supportsUnknownElements){
            return ownerDocument.createDocumentFragment();
          }
          data = data || getExpandoData(ownerDocument);
          var clone = data.frag.cloneNode(),
          i = 0,
          elems = getElements(),
          l = elems.length;
          for(;i<l;i++){
            clone.createElement(elems[i]);
          }
          return clone;
        }

        /**
         * Shivs the `createElement` and `createDocumentFragment` methods of the document.
         * @private
         * @param {Document|DocumentFragment} ownerDocument The document.
         * @param {Object} data of the document.
         */
        function shivMethods(ownerDocument, data) {
          if (!data.cache) {
            data.cache = {};
            data.createElem = ownerDocument.createElement;
            data.createFrag = ownerDocument.createDocumentFragment;
            data.frag = data.createFrag();
          }


          ownerDocument.createElement = function(nodeName) {
            //abort shiv
            if (!html5.shivMethods) {
              return data.createElem(nodeName);
            }
            return createElement(nodeName, ownerDocument, data);
          };

          ownerDocument.createDocumentFragment = Function('h,f', 'return function(){' +
                                                          'var n=f.cloneNode(),c=n.createElement;' +
                                                          'h.shivMethods&&(' +
                                                          // unroll the `createElement` calls
                                                          getElements().join().replace(/[\w\-]+/g, function(nodeName) {
            data.createElem(nodeName);
            data.frag.createElement(nodeName);
            return 'c("' + nodeName + '")';
          }) +
            ');return n}'
                                                         )(html5, data.frag);
        }

        /*--------------------------------------------------------------------------*/

        /**
         * Shivs the given document.
         * @memberOf html5
         * @param {Document} ownerDocument The document to shiv.
         * @returns {Document} The shived document.
         */
        function shivDocument(ownerDocument) {
          if (!ownerDocument) {
            ownerDocument = document;
          }
          var data = getExpandoData(ownerDocument);

          if (html5.shivCSS && !supportsHtml5Styles && !data.hasCSS) {
            data.hasCSS = !!addStyleSheet(ownerDocument,
                                          // corrects block display not defined in IE6/7/8/9
                                          'article,aside,dialog,figcaption,figure,footer,header,hgroup,main,nav,section{display:block}' +
                                            // adds styling not present in IE6/7/8/9
                                            'mark{background:#FF0;color:#000}' +
                                            // hides non-rendered elements
                                            'template{display:none}'
                                         );
          }
          if (!supportsUnknownElements) {
            shivMethods(ownerDocument, data);
          }
          return ownerDocument;
        }

        /*--------------------------------------------------------------------------*/

        /**
         * The `html5` object is exposed so that more elements can be shived and
         * existing shiving can be detected on iframes.
         * @type Object
         * @example
         *
         * // options can be changed before the script is included
         * html5 = { 'elements': 'mark section', 'shivCSS': false, 'shivMethods': false };
         */
        var html5 = {

          /**
           * An array or space separated string of node names of the elements to shiv.
           * @memberOf html5
           * @type Array|String
           */
          'elements': options.elements || 'abbr article aside audio bdi canvas data datalist details dialog figcaption figure footer header hgroup main mark meter nav output progress section summary template time video',

          /**
           * current version of html5shiv
           */
          'version': version,

          /**
           * A flag to indicate that the HTML5 style sheet should be inserted.
           * @memberOf html5
           * @type Boolean
           */
          'shivCSS': (options.shivCSS !== false),

          /**
           * Is equal to true if a browser supports creating unknown/HTML5 elements
           * @memberOf html5
           * @type boolean
           */
          'supportsUnknownElements': supportsUnknownElements,

          /**
           * A flag to indicate that the document's `createElement` and `createDocumentFragment`
           * methods should be overwritten.
           * @memberOf html5
           * @type Boolean
           */
          'shivMethods': (options.shivMethods !== false),

          /**
           * A string to describe the type of `html5` object ("default" or "default print").
           * @memberOf html5
           * @type String
           */
          'type': 'default',

          // shivs the document according to the specified `html5` object options
          'shivDocument': shivDocument,

          //creates a shived element
          createElement: createElement,

          //creates a shived documentFragment
          createDocumentFragment: createDocumentFragment
        };

        /*--------------------------------------------------------------------------*/

        // expose html5
        window.html5 = html5;

        // shiv the document
        shivDocument(document);

    }(this, document));
    /*>>shiv*/

    // Assign private properties to the return object with prefix
    Modernizr._version      = version;

    // expose these for the plugin API. Look in the source for how to join() them against your input
    /*>>prefixes*/
    Modernizr._prefixes     = prefixes;
    /*>>prefixes*/
    /*>>domprefixes*/
    Modernizr._domPrefixes  = domPrefixes;
    Modernizr._cssomPrefixes  = cssomPrefixes;
    /*>>domprefixes*/

    /*>>mq*/
    // Modernizr.mq tests a given media query, live against the current state of the window
    // A few important notes:
    //   * If a browser does not support media queries at all (eg. oldIE) the mq() will always return false
    //   * A max-width or orientation query will be evaluated against the current state, which may change later.
    //   * You must specify values. Eg. If you are testing support for the min-width media query use:
    //       Modernizr.mq('(min-width:0)')
    // usage:
    // Modernizr.mq('only screen and (max-width:768)')
    Modernizr.mq            = testMediaQuery;
    /*>>mq*/

    /*>>hasevent*/
    // Modernizr.hasEvent() detects support for a given event, with an optional element to test on
    // Modernizr.hasEvent('gesturestart', elem)
    Modernizr.hasEvent      = isEventSupported;
    /*>>hasevent*/

    /*>>testprop*/
    // Modernizr.testProp() investigates whether a given style property is recognized
    // Note that the property names must be provided in the camelCase variant.
    // Modernizr.testProp('pointerEvents')
    Modernizr.testProp      = function(prop){
        return testProps([prop]);
    };
    /*>>testprop*/

    /*>>testallprops*/
    // Modernizr.testAllProps() investigates whether a given style property,
    //   or any of its vendor-prefixed variants, is recognized
    // Note that the property names must be provided in the camelCase variant.
    // Modernizr.testAllProps('boxSizing')
    Modernizr.testAllProps  = testPropsAll;
    /*>>testallprops*/


    /*>>teststyles*/
    // Modernizr.testStyles() allows you to add custom styles to the document and test an element afterwards
    // Modernizr.testStyles('#modernizr { position:absolute }', function(elem, rule){ ... })
    Modernizr.testStyles    = injectElementWithStyles;
    /*>>teststyles*/


    /*>>prefixed*/
    // Modernizr.prefixed() returns the prefixed or nonprefixed property name variant of your input
    // Modernizr.prefixed('boxSizing') // 'MozBoxSizing'

    // Properties must be passed as dom-style camelcase, rather than `box-sizing` hypentated style.
    // Return values will also be the camelCase variant, if you need to translate that to hypenated style use:
    //
    //     str.replace(/([A-Z])/g, function(str,m1){ return '-' + m1.toLowerCase(); }).replace(/^ms-/,'-ms-');

    // If you're trying to ascertain which transition end event to bind to, you might do something like...
    //
    //     var transEndEventNames = {
    //       'WebkitTransition' : 'webkitTransitionEnd',
    //       'MozTransition'    : 'transitionend',
    //       'OTransition'      : 'oTransitionEnd',
    //       'msTransition'     : 'MSTransitionEnd',
    //       'transition'       : 'transitionend'
    //     },
    //     transEndEventName = transEndEventNames[ Modernizr.prefixed('transition') ];

    Modernizr.prefixed      = function(prop, obj, elem){
      if(!obj) {
        return testPropsAll(prop, 'pfx');
      } else {
        // Testing DOM property e.g. Modernizr.prefixed('requestAnimationFrame', window) // 'mozRequestAnimationFrame'
        return testPropsAll(prop, obj, elem);
      }
    };
    /*>>prefixed*/


    /*>>cssclasses*/
    // Remove "no-js" class from <html> element, if it exists:
    docElement.className = docElement.className.replace(/(^|\s)no-js(\s|$)/, '$1$2') +

                            // Add the new classes to the <html> element.
                            (enableClasses ? ' js ' + classes.join(' ') : '');
    /*>>cssclasses*/

    return Modernizr;

})(this, this.document);
</script>
</head>
  <body>
    

 <!-- Header and Nav -->

  <div class="row">
    <div class="large-12 columns">
      <div class="panel">
        <h1>No Pendrive Directory Listing</h1>
      </div>
    </div>
  </div>

  <!-- End Header and Nav -->


  <div class="row">



 <!-- Nav Sidebar -->
    <!-- This is source ordered to be pulled to the left on larger screens -->
    <div class="large-3 columns ">
      <div class="panel">
        <a href="#"><img src="http://gdsol.in/desktop/LOGO.png" /></a>
        <h5><a href="http://www.gdsol.in">Gurupad Digital Solutions (GDSOL)</a></h5>
          <div class="section-container vertical-nav" data-section data-options="deep_linking: false; one_up: true">
          <section class="section">
            <h5 class="title"><a href="http://www.facebook.com/coolshankhandelwal">Shantanu Khandelwal</a></h5>
          </section>
          <section class="section">
            <h5 class="title"><a href="http://www.facebook.com/satts1">Satinder Singh</a></h5>
          </section>
          <section class="section">
            <h5 class="title"><a href="http://facebook.com/Shubh2210">Shubhra Upaphyay</a></h5>
          </section>
          
        </div>

      </div>
    </div>
    
    <!-- Main Feed -->
    <!-- This has been source ordered to come first in the markup (and on small devices) but to be to the right of the nav on larger screens -->
    <div class="large-6 columns">

      <!-- Feed Entry -->
      <div class="row">
        <div class="large-2 columns small-3"><img src="http://placehold.it/80x80&text=[img]" /></div>
        <div class="large-10 columns">
          <p><strong>Some Old Wise Man said:</strong> Trying To figure out what problem is what the problem is .<br> We at GDSol Believe in Easy way of Living .  <br> <br>
          Help Us Grow .. If You like this product please Like us on facecook <a href='http://www.facebook.com/gurupaddigitalsolutions'>GDSOL</a></p>
            
          </ul>


          
          </div>
        </div>
      </div>
      <!-- End Feed Entry -->

      <hr />




  '''
  
index_2=''' <footer class="row">
    <div class="large-12 columns">
      <hr />
      <div class="row">
        <div class="large-5 columns">
          <p>&copy; Copyright 2013 <a href='http://www.gdsol.in'>GDSOL</a> Team.</p>
        </div>
        <div class="large-7 columns">
          <ul class="inline-list right">
            <li><a href="http://www.facebook.com/coolshankhandelwal">Shantanu Khandelwal</a></li>
            <li><a href="http://www.facebook.com/satts1">Satinder Singh</a></li>
            <li><a href="https://www.facebook.com/Shubh2210">Shubhra Upaphyay</a></li>
          </ul>
        </div>
      </div>
    </div>
  </footer>
        <script>
      $(document).foundation();

      var doc = document.documentElement;
      doc.setAttribute('data-useragent', navigator.userAgent);
    </script>
  </body>
</html>  '''
fw=os.open("index.html",os.O_RDWR|os.O_CREAT )
os.write(fw,index_1)
listd=os.listdir("./")
for item in listd:
	if os.path.isdir(item):
		a='''<!-- Feed Entry -->
      <div class="row">
        <div class="large-2 columns small-3"><img src="http://placehold.it/80x80&text=[img]" /></div>
        <div class="large-10 columns">
          <p><strong>Directory '''+"</strong>"+item+"</p>"+'''<ul class="inline-list">
            <li><a href="'''+item+'''">Navigate</a></li>
            
          </ul>


          
          </div>
        </div>
      </div>
      
	</div>
<!-- End Feed Entry -->'''
		os.write(fw,a)
	elif os.path.isfile(item):
		a='''<!-- Feed Entry -->
      <div class="row">
        <div class="large-2 columns small-3"><img src="http://placehold.it/80x80&text=[img]" /></div>
        <div class="large-10 columns">
          <p><strong>File '''+"</strong>"+item+"</p>"+'''<ul class="inline-list">
            <li><a href="'''+item+'''" target="_blank">Download</a></li>
            
          </ul>


          
          </div>
        </div>
      </div>
      
	</div>
<!-- End Feed Entry -->'''
		os.write(fw,a)
	else:
		a='''<!-- Feed Entry -->
      <div class="row">
        <div class="large-2 columns small-3"><img src="http://placehold.it/80x80&text=[img]" /></div>
        <div class="large-10 columns">
          <p><strong>Unknown '''+"</strong>"+item+"</p>"+'''<ul class="inline-list">
            <li><a href='''+item+''' target='_blank'>Download</a></li>
            
          </ul>


          
          </div>
        </div>
      </div>
      
	</div>
<!-- End Feed Entry -->'''
		os.write(fw,a)
		
	
os.write(fw,index_2)
os.close(fw)

print "Open The Following URL on the destination computer"
print "\n" + str(get_lan_ip())+":"+str(PORT)+"\n\n\n"
try:
	tinurl=str("http://tinyurl.com/api-create.php?url=http://")+str(get_lan_ip())+":"+str(PORT)
	tinurlans=urllib2.urlopen(tinurl)
	print "\n"+tinurlans
except:
	print "The internet connection is not working"
	

print "\n Press Enter To continue\n"
pola=raw_input()
print 
try :
	httpd.serve_forever()
except KeyboardInterrupt:
	os.remove("index.html")
	exit(0)
