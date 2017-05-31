<?php
//purpose: hold specific login data and make database connections for read-only actions
//security: the directory where this file lives must have .htaccess file allowing only calls from php files to have read access to it.

$connectLinkedpeople = new mysqli('localhost','ADD-DB-USER','ADD-DB-PASSWORD', 'linked_people');
$connectLinkedpeople->set_charset('utf8');

if ($connectLinkedpeople->connect_errno) {
  die('Unable to connect to libstaff database [' . $connectLinkedpeople->connect_error . ']');
}

?>
