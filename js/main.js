google.load("earth", "1");

var ge = null;

function init() {
	google.earth.createInstance("map3d", initCallback, failureCallback);
}

function initCallback(object) {
	ge = object;
	ge.getWindow().setVisibility(true);
	ge.getOptions().setStatusBarVisibility(true);
	ge.getNavigationControl().setVisibility(ge.VISIBILITY_AUTO);
	ge.getLayerRoot().enableLayerById(ge.LAYER_BORDERS, false);
	ge.getLayerRoot().enableLayerById(ge.LAYER_ROADS, false);
	ge.getLayerRoot().enableLayerById(ge.LAYER_BUILDINGS, true);
	ge.getLayerRoot().enableLayerById(ge.LAYER_TERRAIN, true);


	// Pull in sketchup model
	var placemark = ge.createPlacemark('');
	placemark.setName('model');
	var model = ge.createModel('');
	ge.getFeatures().appendChild(placemark);
	var loc = ge.createLocation('');
	model.setLocation(loc);
	var link = ge.createLink('');
	// A textured model created in Sketchup and exported as Collada.
	link.setHref('http://earth-api-samples.googlecode.com/svn/trunk/examples/static/splotchy_box.dae');
	model.setLink(link);

	placemark.setGeometry(model);

	console.log(ge);

	// var point = ge.createPoint('');
	// point.setLatitude(39.095);
	// point.setLongitude(-94.586);
	// placemark.setGeometry(point);

	// var lookAt = ge.createLookAt('');
	// lookAt.setLatitude(39.102951);
	// lookAt.setLongitude(-94.583061);
	// lookAt.setRange(10000.0);
	// lookAt.set(39.095, -94.586, 0, ge.ALTITUDE_RELATIVE_TO_GROUND, 15, 87, 500);
	// ge.getView().setAbstractView(lookAt);



	// // Create the placemark.
	// var placemark = ge.createPlacemark('');
	// placemark.setName("placemark");
	
	// // Define a custom icon.
	// var icon = ge.createIcon('');
	// icon.setHref('http://maps.google.com/mapfiles/kml/paddle/red-circle.png');
	// var style = ge.createStyle('');
	// style.getIconStyle().setIcon(icon);
	// style.getIconStyle().setScale(5.0);
	// placemark.setStyleSelector(style);

	// // Set the placemark's location.  
	// var point = ge.createPoint('');
	// point.setLatitude(39.095);
	// point.setLongitude(-94.586);
	// placemark.setGeometry(point);

	// // Add the placemark to Earth.
	// ge.getFeatures().appendChild(placemark);

	// var balloon = ge.createHtmlStringBalloon('');
	// balloon.setFeature(placemark);
	// balloon.setMinWidth(400);
	// balloon.setMaxHeight(400);
	// balloon.setCloseButtonEnabled(false);

	// Create a 3D model, initialize it from a Collada file, and place it
	// in the world.

}
	

function failureCallback(object) {
	alert('Didn\'t work!');
}



