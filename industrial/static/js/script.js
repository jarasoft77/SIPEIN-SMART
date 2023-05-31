$(document).ready(function () {
    $('.tablareferencia').DataTable({
        dom: 'Bfrtilp',
        buttons: [
            {
                extend: 'excelHtml5',
                text: "<i class='bi bi-file-earmark-excel'></i>",
                titleAttr: 'Exportar a Excel',
                className: 'btn btn-success',
            },
            {
                extend: 'pdfHtml5',
                text: "<i class='bi bi-file-pdf-fill'></i>",
                titleAttr: 'Exportar a PDF',
                className: 'btn btn-danger',
            },
            {
                extend: 'print',
                text: "<i class='bi bi-printer-fill'></i>",
                titleAttr: 'Imprimir',
                className: 'btn btn-info',
            },
        ],
        pageLength: 13,
    });
});

