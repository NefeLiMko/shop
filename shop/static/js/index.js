var slideEl = $(".slide--parent");
var slideEl2 = $(".carousel");
slideEl.flickity({
	imagesLoaded: true,
	wrapAround: true,
	autoPlay: 3000,
	pauseAutoPlayOnHover: false,
	pageDots:true,
	prevNextButtons:false
}); 

slideEl2.flickity({
	imagesLoaded: true,
	wrapAround: true,
	autoPlay: false,
	pauseAutoPlayOnHover: false,
	pageDots:false,
	prevNextButtons:true,
	contain: false,
	draggable: true,
	

	
}); 