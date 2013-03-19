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
ge.getLayerRoot().enableLayerById(ge.LAYER_BORDERS, true);
ge.getLayerRoot().enableLayerById(ge.LAYER_ROADS, true);

var lookAt = ge.createLookAt('');
lookAt.setLatitude(39.102951);
lookAt.setLongitude(-94.583061);
lookAt.setRange(8000.0);
ge.getView().setAbstractView(lookAt);
}

function failureCallback(object) {
}

