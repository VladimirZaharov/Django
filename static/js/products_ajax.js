$( document ).on( 'click', '.btn-outline-success', function(event) {
   if (event.target.hasAttribute('href')) {
       var link = event.target.href + 'ajax/';

       console.log(link)

       $.ajax({
           url: link,
           success: function (data) {
               $('.row').html(data.result);
           },
       });

       event.preventDefault();

   }
});

