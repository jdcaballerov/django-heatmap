/**
 * @author Juan Diego Caballero
 * Run after loading
 */


function guardar(url,datos){
/*
	$.post(url, datos,function(data) {
     	//alert(data);
     });

*/
  $.ajax({
        url: url,
        type: "POST",
        data: datos,
    }).done(function(data) {
        if (result['error']) {
          alert('An error was encountered: ');
        }
        else {
		  alert('good');
        }
    });
}

$(document).mousedown(function(e) {

		var url = '/heatmap/save_click_event/';
		datos = {
		resx : screen.width,
		resy: screen.height,
		url: window.location.href,
		x: e.pageX,
		y: e.pageY,
		height: $(document).height(),
		width:  $(document).width(),
	};
	//alert(JSON.stringify(datos, null, 4));
	guardar(url, datos);
	return true;
});

