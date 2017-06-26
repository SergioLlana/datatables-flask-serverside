/*jslint browser: true*/
/*global $*/


$(document).ready(function () {
  $.get('/tables/clientside_table', function (data) {
    $('#clientside_table').DataTable({
      data: data.data,
      paging: true,
      dom: 'frtipB',
      columns: [
        {"data": "A", "title": "Column A"},
        {"data": "B", "title": "Column B"},
        {"data": "C", "title": "Column C"},
        {"data": "D", "title": "Column D"},
      ]
    });
  });
});
