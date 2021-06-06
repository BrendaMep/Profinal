
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

var papantlaIcon = L.icon({
	iconUrl: 'images/papantla.png',
	iconSize: [18, 31],
});

var zempoIcon = L.icon({
	iconUrl: 'images/zempoala.png',
	iconSize: [18, 31],
});

var acayucanIcon = L.icon({
	iconUrl: 'images/acayucan.png',
	iconSize: [18, 31],
});

var aguaIcon = L.icon({
	iconUrl: 'images/agua.png',
	iconSize: [18, 31],
});

var alvaradoIcon = L.icon({
	iconUrl: 'images/alvarado.png',
	iconSize: [18, 31],
});

var bocaIcon = L.icon({
	iconUrl: 'images/boca.png',
	iconSize: [18, 31],
});

var coatzaIcon = L.icon({
	iconUrl: 'images/coatzacoalcos.png',
	iconSize: [18, 31],
});

var fortinIcon = L.icon({
	iconUrl: 'images/fortin.png',
	iconSize: [18, 31],
});

var huatuscoIcon = L.icon({
	iconUrl: 'images/huatusco.png',
	iconSize: [18, 31],
});

var huautlaIcon = L.icon({
	iconUrl: 'images/huautla.png',
	iconSize: [18, 31],
});

var joachinIcon = L.icon({
	iconUrl: 'images/joachin.png',
	iconSize: [18, 31],
});

var minaIcon = L.icon({
	iconUrl: 'images/minatitlan.png',
	iconSize: [18, 31],
});

var nigroIcon = L.icon({
	iconUrl: 'images/nigromante.png',
	iconSize: [18, 31],
});

var otaIcon = L.icon({
	iconUrl: 'images/otatitlan.png',
	iconSize: [18, 31],
});

var tecoIcon = L.icon({
	iconUrl: 'images/tecolutla.png',
	iconSize: [18, 31],
});

var tezIcon = L.icon({
	iconUrl: 'images/teziutlan.png',
	iconSize: [18, 31],
});

var tuxIcon = L.icon({
	iconUrl: 'images/tuxtla.png',
	iconSize: [18, 31],
});

var vegaIcon = L.icon({
	iconUrl: 'images/vega.png',
	iconSize: [18, 31],
});

var yangaIcon = L.icon({
	iconUrl: 'images/yanga.png',
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
	'Xalapa': {
		'titulo': 'Xalapa',
		'coordenadas': [19.54377, -96.91018],
		'icon': xalapaIcon //creaIcono('images/xalapaMarker.png', 18, 31)
	},
	'Zempoala': {
		'titulo': 'Zempoala',
		'coordenadas': [19.44688, -96.40507],
		'icon': zempoIcon
	},
	'Vega': {
		'titulo': 'Vega de Alatorre',
		'coordenadas': [20.03034, -96.65044],
		'icon': vegaIcon
	},
	'Acayucan': {
		'titulo': 'Acayucan',
		'coordenadas': [17.94919, -94.91459],
		'icon': acayucanIcon
	},
	'Coatzacualcos': {
		'titulo': 'Coatzacualcos',
		'coordenadas': [18.13447, -94.45898],
		'icon': coatzaIcon
	},
	'Agua': {
		'titulo': 'Agua Dulce',
		'coordenadas': [18.14259, -94.1436],
		'icon': aguaIcon
	},
	'Huautla': {
		'titulo': 'Huautla de Jiménez',
		'coordenadas': [18.13108, -96.84314],
		'icon':huautlaIcon
	},
	'Fortin ': {
		'titulo': 'Fortin de las Flores ',
		'coordenadas': [18.9017, -96.99896],
		'icon': fortinIcon
	},
	'Huatusco': {
		'titulo': ' Huatusco',
		'coordenadas': [19.14823, -96.96654],
		'icon': huatuscoIcon
	},
	'Joachin': {
		'titulo': ' Joachin',
		'coordenadas': [18.6407, -96.23095],
		'icon': joachinIcon
	},
	'Minatitlan': {
		'titulo': ' Minatitlan',
		'coordenadas': [17.99392, -94.5466],
		'icon': minaIcon
	},
	'Nigro ': {
		'titulo': ' El Nigromante',
		'coordenadas': [17.76323, -95.75574],
		'icon': nigroIcon
	},
	'Otatitlan': {
		'titulo': ' Otatitlan',
		'coordenadas': [18.18106, -96.03439],
		'icon': otaIcon
	},
	'Papantla': {
		'titulo': ' Papantla',
		'coordenadas': [20.45667, -97.31561],
		'icon': papantlaIcon
	},
	'Tuxtla': {
		'titulo': ' San Andres Tuxtla',
		'coordenadas': [18.44412, -95.21302],
		'icon': tuxIcon
	},
	'Tecolutla': {
		'titulo': ' Tecolutla',
		'coordenadas': [20.47955, -97.01012],
		'icon': tecoIcon
	},
	'Teziutlan': {
		'titulo': ' Teziutlan',
		'coordenadas': [19.81601, -97.35705],
		'icon': tezIcon
	},
	'Alvarado': {
		'titulo': ' Alvarado',
		'coordenadas': [18.76961, -95.75894],
		'icon': alvaradoIcon
	},
	'Yanga': {
		'titulo': ' Yanga',
		'coordenadas': [18.82928, -96.80027],
		'icon': yangaIcon
	},
	'Boca': {
		'titulo': ' Boca del Rio',
		'coordenadas': [19.10627, -96.10632],
		'icon': bocaIcon
	}
};

Object.entries(locations).forEach(site => pintaMarker(site));

function pintaMarker(item) {
	console.log(item);
	if (item[1].icon) {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo, icon: item[1].icon}).addTo(mymap);
	} else {
		var marker = L.marker(item[1].coordenadas, {'title': item[1].titulo}).addTo(mymap);
	}

}

// create a red polyline from an array of LatLng points

var ciudades = ['Xalapa','zempoala','boca','alvarado','tuxtla'];
var ruta1 = [];
function cordenada(ciudad){
	return locations[ciudad].coordenadas;
}

for(let i of ciudades){
	ruta1.push(cordenada(i))
}

var polyline = L.polyline(ruta1, {color: 'red'}).addTo(mymap);
console.log(mymap.distance(locations.Xalapa.coordenadas, locations.Zempoala.coordenadas) + ' metros');
