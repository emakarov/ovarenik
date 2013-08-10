    $( function() {
    	onresize();    	
    });
    $(window).load(function() {
    	onresize();
    });
    $(window).resize(function() {
    	onresize();
    });
    $("#leftring").on('mouseover',function(){
      $("#wordnew").show();
    });
    $("#leftring").on('mouseout',function(){
      $("#wordnew").hide();
    });
    $("#rightring").on('mouseover',function(){
      $("#playbutton").show();
    });
    $("#rightring").on('mouseout',function(){
      $("#playbutton").hide();
    });
    
    var randomnumber=1+Math.floor(Math.random()*4)
    
    function onresize(){
	var maph = $(window).height();
//	var mapw = $(window).width();
	var mapw = $("#nvbarinner").width()+40;
	if (mapw<1024){mapw=1024;}
	var nvbinw = $("#nvbinnav").width();
    	$("#nvbin").show();
        $("#nvbinmobile").hide();
    	$('#bgimgdiv').css('background','url(static/images/background_'+randomnumber+'.jpg)');
    	$('#bgimgdiv').css('background-position', 'left 0px');
	$('#bgimgdiv').css('width',mapw+'px');
	$('#bgimgdiv').css('height',parseInt(3*mapw/4)+'px');
    	//$("#nvbin").css("left",Math.floor(mapw/2-nvbinw/2)-10+"px")
    	
    	var leftboxsize = Math.floor(140*mapw/1400);

    	$('#leftring').css("width",leftboxsize+'px');
    	$('#leftring').css("height",leftboxsize+'px');
    	$('#wordnew').css("width",leftboxsize+'px');

    	$('#rightring').css("width",leftboxsize+'px');
    	$('#rightring').css("height",leftboxsize+'px');
    	$('#playbutton').css("width",85*mapw/1400+'px');

    	
    	$('#leftring').css("left",Math.floor(168*mapw/1400)-Math.floor(leftboxsize/2)+'px');
    	$('#leftring').css("top",Math.floor(208*mapw/1400)-Math.floor(leftboxsize/2)+40+'px');

    	$('#rightring').css("left",mapw-Math.floor(168*mapw/1400)-Math.floor(leftboxsize/2)+20+'px');
    	$('#rightring').css("top",Math.floor(208*mapw/1400)-Math.floor(leftboxsize/2)+55+'px');

    	$('#imglogo1').css("left",Math.floor(mapw/2)-140+'px');
    	$('#imglogo1').css("top",Math.floor(208*mapw/1400)-Math.floor(leftboxsize/2)+250+'px');
    	$('#imglogo1').show();

    	$('#imglogo2').css("left",Math.floor(mapw/2)-100+'px');
    	$('#imglogo2').css("top",Math.floor(208*mapw/1400)-Math.floor(leftboxsize/2)+'px');
    	$('#imglogo2').show();

    	$('#imgfooter').css("top",Math.floor(1050*mapw/1400)+'px');
    	$('#imgfooter').css("left",Math.floor(mapw/2)-100+'px');
    	$('#imgfooter').show();


    	
    	/*
    	
    	if (detectipad() && maph>mapw){
    	  $('#bgimgdiv').css('background-position', '-220px 0px');
    	}
    	
    	if (detectmob() && maph<mapw){
    	  $("#nvbin").hide();
    	  $("#nvbinmobile").show();
	  var nvbinmobilew = $("#nvbinnavmobile").width();
    	  $("#nvbinmobile").css("left",Math.floor(mapw/2-nvbinmobilew/2)+"px")
    	  $('#bgimgdiv').css('background','url(images/main_bg_mobile_hor.jpg)');
       	  $('#bgimgdiv').css('background-size','cover');
       	  return 0;
    	}

    	if(maph/mapw<3/4){
  	  $('#bgimgdiv').css('width',mapw+'px');
  	  $('#bgimgdiv').css('width',3*mapw/4+'px');
    	  $('#bgimgdiv').css('background','url(images/main_bg_longscreen.jpg)');
    	} 
    	*/
    	
    	/*
    	if (mapw<480 || detectmob()){
    	  //$("#nvbin").css("left","20px")
    	  $("#nvbin").hide();
    	  $("#nvbinmobile").show();
	  var nvbinmobilew = $("#nvbinnavmobile").width();
    	  $("#nvbinmobile").css("left",Math.floor(mapw/2-nvbinmobilew/2)+"px")
    	  $('#bgimgdiv').css('background','url(images/main_bg_600.jpg)');
	  $('#bgimgdiv').css('height',mapw+'px');
	  $('#bgimgdiv').css('height',maph+'px');
    	}
    	*/
    	$('#bgimgdiv').css('background-size','cover');
    }
    
    function detectipad() {
    	if( navigator.userAgent.match(/iPad/i) ){
    		return true;
    	}
    	else {
    		return false;
    	}
    } 

    function detectmob() { 
    	if( navigator.userAgent.match(/Android/i)
    	|| navigator.userAgent.match(/webOS/i)
    	|| navigator.userAgent.match(/iPhone/i)
//    	|| navigator.userAgent.match(/iPad/i)
    	|| navigator.userAgent.match(/iPod/i)
    	|| navigator.userAgent.match(/BlackBerry/i)
    	|| navigator.userAgent.match(/Windows Phone/i)
    	){
    		return true;
    	}
    	else {
    		return false;
    	}
    }
        $(window).ready(function(){
         viewport.setAttribute('content','width='+$(window).width()+";initial-scale=1.0;maximum-scale=1;user-scalable=0;");
        });

