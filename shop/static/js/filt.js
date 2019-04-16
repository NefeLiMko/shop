$("#promo").on("click",function () {
	$('.promo').css({"display":"block"});
	$('.new').css({"display":"none"});
    $('.hit').css({"display":"none"});
});

$("#new").on("click",function () {
	$('.promo').css({"display":"none"});
	$('.new').css({"display":"block"});
    $('.hit').css({"display":"none"});
});

$("#hit").on("click",function () {
	$('.promo').css({"display":"none"});
	$('.new').css({"display":"none"});
    $('.hit').css({"display":"block"});
});
