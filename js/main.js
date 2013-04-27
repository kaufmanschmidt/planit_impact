$('.location').blur(function(){
	// console.log($('.location').val());
	var url = 'http://www.mapquestapi.com/geocoding/v1/address?key=';
	var api_key = 'Fmjtd%7Cluua2hutll%2Cra%3Do5-96axlu';
	url = url + api_key + '&location=';
	address = '"'+$('.location').val()+'"';
	url = url + address;

	console.log(url);
	$.getJSON(url, function(data) {
		var lat = data['results'][0]['locations'][0]['latLng']['lat'];
		var lng = data['results'][0]['locations'][0]['latLng']['lng'];
		$('#report').attr('href', 'report.html?lat='+ lat +'&lng='+lng);
	});

})