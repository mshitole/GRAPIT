""" constants

All markup for reporting.
"""

HEADER = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            body{
                padding:10px;
            }
            .pure-table{
                empty-cells: show;
                border: 1px solid #cbcbcb;
            }
            .pure-table, table {
                border-collapse: collapse;
                border-spacing: 0;
            }
            .pure-table thead {
                background-color: #e0e0e0;
                color: #000;
                text-align: left;
                vertical-align: bottom;
            }
            .pure-table th, .pure-table td {
                padding: 0.5em 1em;
            }
            .pure-table td, .pure-table th {
                border-left: 1px solid #cbcbcb;
                border-width: 0 0 0 1px;
                font-size: inherit;
                margin: 0;
                overflow: visible;
                padding: .5em 1em;
            }
            tbody {
                display: table-row-group;
                vertical-align: middle;
                border-color: inherit;
            }
            tr {
                display: table-row;
                vertical-align: inherit;
                border-color: inherit;
            }
            p span{
                padding-left:10px;
            }
            h3{
                margin-bottom: 5px;
            }
        </style>
    </head>
"""

BODY = """
<body>
    <h3>REST API Test Report</h3>
    <p>
        <span>Total API &nbsp;&nbsp;&nbsp;</span>: %s </br>
        <span>API Passed</span>&nbsp;: %s (%s%%)</br>
        <span>API Failed</span>&nbsp;&nbsp;: %s (%s%%)</br>
    </p>
"""

TABLE_PART_1= """
    <h3>%s</h3>
    <table class="pure-table">
        <thead>
            <tr>
                <th>No</td>
                <th>URL</td>
                <th>Method</td>
                <th>Status</td>
            </tr>
        </thead>
        <tbody>
"""

TABLE_PART_2="""
    <tr>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
        <td>%s</td>
    </tr>
"""

TABLE_PART_3 = "</tbody></table>"

FOOTER = """
    </body>
</html>
"""