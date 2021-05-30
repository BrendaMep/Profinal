
var mymap = L.map('mapid').setView([19.046250, -96.259722], 7);

var apiKey = ''

L.tileLayer(`https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=${apiKey}`, {
	maxZoom: 18,
	attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
		'<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
		'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
	id: 'mapbox/streets-v11',
	tileSize: 512,
	zoomOffset: -1
}).addTo(mymap);


var xalapaIcon = L.icon({
	iconUrl: 'images/xalapaMarker.png',
	iconSize: [18, 31], 
});

/*function creaIcono(ruta, width, height) {
	var icono = L.icon({
		iconUrl: ruta,
		iconSize: [width, height], 
	});
	return icono;
}*/

var locations = {
	'xalapa': {
		'titulo': 'Xalapa',
		'coordenadas': [19.54377, -96.91018],
		'icon': xalapaIcon //creaIcono('images/xalapaMarker.png', 18, 31)
	},
	'zempoala': {
		'titulo': 'Zempoala',
		'coordenadas': [19.44688, -96.40507]
	},
	'vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044]
	},
	'vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044]
	},
	'acayucan': {
		'titulo': 'Acayucan',
		'coordenadas': [17.94919, -94.91459]
	},
	'coatzacualcos': {
		'titulo': 'Coatzacualcos',
		'coordenadas': [18.13447, -94.45898]
	},
	' agua': {
		'titulo': 'Agua Dulce',
		'coordenadas': [18.14259, -94.1436]
	},
	' huautla': {
		'titulo': 'Huautla de Jiménez',
		'coordenadas': [18.13108, -96.84314]
	},
	'fortin ': {
		'titulo': 'Fortin de las Flores ',
		'coordenadas': [18.9017, -96.99896]
	},
	' huatusco': {
		'titulo': ' Huatusco',
		'coordenadas': [19.14823, -96.96654]
	},
	' joachin': {
		'titulo': ' Joachin',
		'coordenadas': [18.6407, -96.23095]
	},
	' minatitlan': {
		'titulo': ' Minatitlan',
		'coordenadas': [17.99392, -94.5466]
	},
	'nigro ': {
		'titulo': ' El Nigromante',
		'coordenadas': [17.76323, -95.75574]
	},
	' otatitlan': {
		'titulo': ' Otatitlan',
		'coordenadas': [18.18106, -96.03439]
	},
	' papantla': {
		'titulo': ' Papantla',
		'coordenadas': [20.45667, -97.31561]
	},
	'tuxtla ': {
		'titulo': ' San Andres Tuxtla',
		'coordenadas': [18.44412, -95.21302]
	},
	' tecolutla': {
		'titulo': ' Tecolutla',
		'coordenadas': [20.47955, -97.01012]
	},
	' teziutlan': {
		'titulo': ' Teziutlan',
		'coordenadas': [19.81601, -97.35705]
	},
	' alvarado': {
		'titulo': ' Alvarado',
		'coordenadas': [18.76961, -95.75894]
	},
	' yanga': {
		'titulo': ' Yanga',
		'coordenadas': [18.82928, -96.80027]
	},
	' boca': {
		'titulo': ' Boca del Rio',
		'coordenadas': [19.10627, -96.10632]
	}
};

Object.entries(locations).forEach(site => pintaMarker(site));

function pintaMarker(item) {
	//console.log(item);
	if (item[1].icon) {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo, icon: item[1].icon}).addTo(mymap);
	} else {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo}).addTo(mymap);
	}

}

// create a red polyline from an array of LatLng points
var ruta1 = [
	locations.xalapa.coordenadas,
	locations.zempoala.coordenadas,
	locations.vega.coordenadas,
];

var polyline = L.polyline(ruta1, {color: 'red'}).addTo(mymap);

console.log(mymap.distance(locations.xalapa.coordenadas, locations.zempoala.coordenadas) + ' metros');