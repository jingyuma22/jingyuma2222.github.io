// Call the dataTables jQuery plugin

$(document).ready(function() {
    $('#dataTable').DataTable( {
        search: {
            return: true
        }
    } );
} );