/*jslint browser: true*/
/*global $*/


$(document).ready(function () {
  $('#serverside_table').DataTable({
    bProcessing: true,
    bServerSide: true,
    sPaginationType: "full_numbers",
    lengthMenu: [[10, 25, 50, 100], [10, 25, 50, 100]],
    bjQueryUI: true,
    sAjaxSource: '/tables/serverside_table',
    columns: [
      {"data": "A"},
      {"data": "B"},
      {"data": "C"},
      {"data": "D"},
    ]
  });
});
