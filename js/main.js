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

	var lookAt = ge.createLookAt('');
	// lookAt.setLatitude(39.102951);
	// lookAt.setLongitude(-94.583061);
	// lookAt.setRange(10000.0);
	lookAt.set(39.095, -94.586, 0, ge.ALTITUDE_RELATIVE_TO_GROUND, 15, 87, 500);
	ge.getView().setAbstractView(lookAt);
}

function failureCallback(object) {
}

