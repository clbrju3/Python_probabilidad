$(document).ready(function(){
    alert("casa")
    $.ajax({
        url: "datos.json",
        type:"GET",
        data: {
          zipcode: 97201
        },
     contentype:"JSON",
        success: function(result){
            console.log(result.items);
            for(i=0;i<result.length;i++)
        // $("#xs").append("<h1>"+result[i].nombre);
             $( "#xs" ).html( "<strong>" + result[i].nombre + "</strong> degrees" );
        }
      });
});
function a(){
    alert("jose")
}