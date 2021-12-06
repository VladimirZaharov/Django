$( document ).on( 'click', '.nav-link', function(event) {
   if (event.target.hasAttribute('href')) {
       var link = event.target.href + 'ajax/';
       var link_array = link.split('/');
       console.log(link_array)
       if (link_array[4] == 'products') {
           $.ajax({
               url: link,
               success: function (data) {
                   $('.row').html(data.result);
               },
           });

           event.preventDefault();
       }
   }
});

