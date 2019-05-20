$(function(){
	var $slides = $('.slide_pics li');
	var len = $slides.length;
	var nowli = 0;
	var prevli = 0;
	var $prev = $('.prev');
	var $next = $('.next');
	var ismove = false;
	var timer = null;
	$slides.not(':first').css({left:1000});
	timer = setInterval(autoplay,3000);

	$('.slide').mouseenter(function() {
		clearInterval(timer);
	});

	$('.slide').mouseleave(function() {
		timer = setInterval(autoplay,3000);
	});
	function autoplay(){
		nowli++;
		move();
	}

	$prev.click(function() {
		if(ismove)
		{
			return;
		}		
		nowli--;
		move();

	});
	
	$next.click(function() {
		if(ismove)
		{
			return;
		}		
		nowli++;
		move();

	});


	function move(){

		ismove = true;

		if(nowli<0)
		{
			nowli=len-1;
			prevli = 0
			$slides.eq(nowli).css({left:-1000});
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo');
			$slides.eq(prevli).animate({left:1000},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;
			return;
		}

		if(nowli>len-1)
		{
			nowli = 0;
			prevli = len-1;
			$slides.eq(nowli).css({left:1000});
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo');
			$slides.eq(prevli).animate({left:-1000},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;
			return;
		}


		if(prevli<nowli)
		{
			$slides.eq(nowli).css({left:1000});			
			$slides.eq(prevli).animate({left:-1000},800,'easeOutExpo');
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;
			
		}
		else
		{			
			$slides.eq(nowli).css({left:-1000});			
			$slides.eq(prevli).animate({left:1000},800,'easeOutExpo');	
			$slides.eq(nowli).animate({left:0},800,'easeOutExpo',function(){
				ismove = false;
			});
			prevli=nowli;		
		}

	}
})