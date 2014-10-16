API
===

This part of the documentation covers all resources (routes) provided by
plone.jsonapi.routes. It also covers all the request parameters that can be
applied to these resources to refine the results.


Concept
-------

The API aims to be **as fast as possible**. So the concept of the API is to
postpone *expensive operations* until the user really requests it. To do so,
the API was built with a **two step architecture**.

An *expensive operation* is basically given, when the API needs to wake up an
object to retrieve all its field values.

The *two step architecture* retrieves only the fields of the catalog results
in the first step. Only if the user requests the API URL of a specific object,
the object will be loaded and all the fields of the object will be returned.


.. note:: Since version 0.3, you can add a `complete=yes` paramter to bypass
          the two step behavior and retrieve the full object data immediately.


Base URL
--------

After installation, the Plone API routes are available below the
plone.jsonapi.core root URL (``@@API``) with the base ``/plone/api/1.0``.

Example: ``http://localhost:8080/Plone/@@API/plone/api/1.0/api.json``

.. note:: Please see the documentation of plone.jsonapi.core for the root URL.


There is also an overview of the registered routes, e.g.

``http://localhost:8080/Plone/@@API/plone/api/1.0/api.json``


Operations
----------

The API understands the basic `CRUD <http://en.wikipedia.org/wiki/CRUD>`_
operations on the *content resources*.  Only the VIEW operation is accessible
via a HTTP GET request. All other operations have to be sent via a HTTP POST
request.

+-----------+---------------------------------------------+--------+
| OPERATION | URL                                         | METHOD |
+===========+=============================================+========+
| VIEW      | <BASE URL>/<RESOURCE>/<uid:optional>        | GET    |
+-----------+---------------------------------------------+--------+
| CREATE    | <BASE URL>/<RESOURCE>/create/<uid:optional> | POST   |
+-----------+---------------------------------------------+--------+
| UPDATE    | <BASE URL>/<RESOURCE>/update/<uid:optional> | POST   |
+-----------+---------------------------------------------+--------+
| DELETE    | <BASE URL>/<RESOURCE>/delete/<uid:optional> | POST   |
+-----------+---------------------------------------------+--------+


Resources
---------

:URL Schema: ``<BASE URL>/<RESOURCE>/<OPERATION>/<uid:optional>``

The API registers the routes to the resources during the Plone startup
process. Each of the following resources is bound to a distinct *portal type*
within Plone. So the *folders* resource will only return content informations
of *Folders*.

+-------------+--------------------------------------------------+
| Resource    | Description                                      |
+=============+==================================================+
| folders     | Resource for all Folder contents                 |
+-------------+--------------------------------------------------+
| documents   | Resource for all Page contents                   |
+-------------+--------------------------------------------------+
| events      | Resource for all Event contents                  |
+-------------+--------------------------------------------------+
| files       | Resource for all File contents                   |
+-------------+--------------------------------------------------+
| images      | Resource for all Image contents                  |
+-------------+--------------------------------------------------+
| links       | Resource for all Link contents                   |
+-------------+--------------------------------------------------+
| newsitems   | Resource for all News Item contents              |
+-------------+--------------------------------------------------+
| topics      | Resource for all Collection (old style) contents |
+-------------+--------------------------------------------------+
| collections | Resource for all Collection contents             |
+-------------+--------------------------------------------------+

.. note:: Please see the section `Parameters` on how to refine the returned
          results


Special Resources
-----------------

:URL Schema: ``<BASE URL>/<RESOURCE>/<ACTION:optional>``

Beside the *content resources*, there are some special resources available.

+----------+------------------+--------------------------+
| Resource | Action           | Description              |
+==========+==================+==========================+
| users    | username/current | Resource for Plone Users |
+----------+------------------+--------------------------+
| version  |                  | Get the current Version  |
+----------+------------------+--------------------------+


Parameters
----------

:URL Schema: ``<BASE URL>/<RESOURCE>?<KEY>=<VALUE>&<KEY>=<VALUE>``

All content resources accept to be filtered by request parameters.

+----------+----------------+------------------------------------------------------------------------+
| Key      | Value          | Description                                                            |
+==========+================+========================================================================+
| q        | searchterm     | Search the SearchableText index for the given query string             |
+----------+----------------+------------------------------------------------------------------------+
| path     | /physical/path | Specifiy a physical path to only return results below it.              |
|          |                | See how to `Query by path`_ in the `Plone docs`_ for details.          |
+----------+----------------+------------------------------------------------------------------------+
| depth    | 0..n           | Specify the depth of a path query. Only relevant when using            |
|          |                | the path parameter.                                                    |
+----------+----------------+------------------------------------------------------------------------+
| limit    | 1..n           | Limit the results to the given `limit` number.                         |
|          |                | This will return batched results with `x` pages and `n` items per page |
+----------+----------------+------------------------------------------------------------------------+
| complete | yes/y/1/True   | Flag to return the full object results immediately.                    |
|          |                | Bypasses the *two step* behavior of the API                            |
+----------+----------------+------------------------------------------------------------------------+

It is also possible to use Plone Catalog Indexes directly. At the moment, the
API only supports really basic index types. So date type indexes aren't
supported yet. Also 

Below is a list of the most relevant catalog indexes and the current state if
they're supported or not.

+----------------+----------------+-------------+
| Index Name     | Index type     | Supported   |
+================+================+=============+
| Creator        | FieldIndex     | Y           |
+----------------+----------------+-------------+
| Description    | ZCTextIndex    | Y           |
+----------------+----------------+-------------+
| SearchableText | ZCTextIndex    | N (use `q`) |
+----------------+----------------+-------------+
| Subject        | KeywordIndex   | Y           |
+----------------+----------------+-------------+
| Title          | ZCTextIndex    | Y           |
+----------------+----------------+-------------+
| UID            | UUIDIndex      | Y           |
+----------------+----------------+-------------+
| id             | FieldIndex     | Y           |
+----------------+----------------+-------------+
| review_state   | FieldIndex     | Y           |
+----------------+----------------+-------------+
| Date           | DateIndex      | N           |
+----------------+----------------+-------------+
| created        | DateIndex      | N           |
+----------------+----------------+-------------+
| modified       | DateIndex      | N           |
+----------------+----------------+-------------+
| effective      | DateIndex      | N           |
+----------------+----------------+-------------+
| start          | DateIndex      | N           |
+----------------+----------------+-------------+
| end            | DateIndex      | N           |
+----------------+----------------+-------------+
| effectiveRange | DateRangeIndex | N           |
+----------------+----------------+-------------+
| expires        | DateIndex      | N           |
+----------------+----------------+-------------+


.. note:: Custom added indexes can also be used, as long as they accept a
          single string value as query.



.. _`Plone docs`: http://docs.plone.org/develop/plone/searching_and_indexing/query.html#query-by-path
.. _`Query by path`: http://docs.plone.org/develop/plone/searching_and_indexing/query.html#query-by-path

.. vim: set ft=rst ts=4 sw=4 expandtab tw=78 :