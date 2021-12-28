"""
* Assignment: Pandas Read XSLT Plants
* Complexity: medium
* Lines of code: 4 lines
* Time: 5 min

English:
    1. Read data from `DATA` as `result: pd.DataFrame`
    2. Use XSLT transformation
    3. Make sure that columns and indexes are named properly
    4. Calculate average cost of flower
    5. Run doctests - all must succeed

Polish:
    1. Wczytaj dane z `DATA` jako `result: pd.DataFrame`
    2. Użyj transformaty XSLT
    3. Upewnij się, że nazwy kolumn i indeks są dobrze ustawione
    4. Wylicz średni koszt kwiatów
    5. Uruchom doctesty - wszystkie muszą się powieść

Hints:
    * `pip install --upgrade lxml`

Tests:
    >>> import sys; sys.tracebacklimit = 0

    >>> type(result) is pd.DataFrame
    True
    >>> len(result) > 0
    True
    >>> result
         English Name              Latin Name   Cost
    0       Bloodroot  Sanguinaria canadensis  $2.44
    1       Columbine    Aquilegia canadensis  $9.37
    2  Marsh Marigold        Caltha palustris  $6.81
    3         Cowslip        Caltha palustris  $9.90
"""

import pandas as pd
from io import StringIO
from lxml.etree import XML, XSLT, parse

DATA = """
    <CATALOG>
        <PLANT>
            <COMMON>Bloodroot</COMMON>
            <BOTANICAL>Sanguinaria canadensis</BOTANICAL>
            <ZONE>4</ZONE>
            <LIGHT>Mostly Shady</LIGHT>
            <PRICE>$2.44</PRICE>
            <AVAILABILITY>031599</AVAILABILITY>
        </PLANT>
        <PLANT>
            <COMMON>Columbine</COMMON>
            <BOTANICAL>Aquilegia canadensis</BOTANICAL>
            <ZONE>3</ZONE>
            <LIGHT>Mostly Shady</LIGHT>
            <PRICE>$9.37</PRICE>
            <AVAILABILITY>030699</AVAILABILITY>
        </PLANT>
        <PLANT>
            <COMMON>Marsh Marigold</COMMON>
            <BOTANICAL>Caltha palustris</BOTANICAL>
            <ZONE>4</ZONE>
            <LIGHT>Mostly Sunny</LIGHT>
            <PRICE>$6.81</PRICE>
            <AVAILABILITY>051799</AVAILABILITY>
        </PLANT>
        <PLANT>
            <COMMON>Cowslip</COMMON>
            <BOTANICAL>Caltha palustris</BOTANICAL>
            <ZONE>4</ZONE>
            <LIGHT>Mostly Shady</LIGHT>
            <PRICE>$9.90</PRICE>
            <AVAILABILITY>030699</AVAILABILITY>
        </PLANT>
    </CATALOG>
"""

TEMPLATE = """
    <html xsl:version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
        <table>
            <thead>
                <tr>
                    <th>English Name</th>
                    <th>Latin Name</th>
                    <th>Cost</th>
                </tr>
            </thead>

            <xsl:for-each select="CATALOG/PLANT">
                <tr>
                    <td><xsl:value-of select="COMMON"/></td>
                    <td><xsl:value-of select="BOTANICAL"/></td>
                    <td><xsl:value-of select="PRICE"/></td>
                </tr>
            </xsl:for-each>

        </table>
    </html>
"""


# pd.DataFrame: XSLT transformed DATA
result = ...
