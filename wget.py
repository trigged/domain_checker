#coding=utf-8
from re import match
import re
from django.contrib.gis.geometry import regex

__author__ = 'trigged'
html = """

<!DOCTYPE HTML>
<html>



<head>

	<script src="../js/jquery-1.7.2.min.js"></script>
	<script src="../js/lightbox.js"></script>

	<script src="../js/custom-form-elements.js"></script>

	<link rel="shortcut icon" href="favicon.ico">
	<link rel="shortcut icon" href="favicon.jpg">

    <link href="../css/lightbox.css" rel="stylesheet" type="text/css" media="screen">
    	<link href="../css/normalize.css" rel="stylesheet" type="text/css" media="screen">
    <link href="../css/Styles.css" rel="stylesheet" type="text/css" media="screen"><link href="../css/form.css" rel="stylesheet" type="text/css" media="screen">

	<link href="../css/Print.css" rel="stylesheet" type="text/css" media="print">


    <meta http-equiv="Content-Language" content="en">
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
	<meta http-equiv="Content-Type" content="cache" />
	<meta name="robots" content="INDEX,FOLLOW" />
	<meta name="keywords" content="free erotic art glamour pictures nude models erotica topless babes beauty nudes girls met-art femjoy w4b domai ftv x-art zemani nubiles.net Hegre-Art sex escorts concupiscent coquettes coquetry" />
	<meta name="description" content="Concupiscent Coquettes presents Angelica in Introducing Angelica from X-Art" />
	<meta name="RATING" content="RTA-5042-1996-1400-1577-RTA" />


<!-- Begin Cookie Consent plugin by Silktide - http://silktide.com/cookieconsent -->
<link rel='stylesheet' type='text/css' href='../css/cookie.css'/>
<script type='text/javascript' src='../js/cookie.js'></script>
<script type='text/javascript'>
// <![CDATA[
cc.initialise({
	cookies: {
		analytics: {},
		necessary: {}
	},
	settings: {
		style: 'light',
		ignoreDoNotTrack: true
	}
});
// ]]>
</script>
<!-- End Cookie Consent plugin -->
	<title>Angelica in Introducing Angelica</title>




	<script>
   	function target_popup(form) {
    window.open('', 'formpopup', 'width=298,height=280,resizeable,scrollbars')
    //form.body.style.backgroundImage="url('popup.png')";
    form.target = 'formpopup'; }
    </script>

</head>

<body itemscope itemtype="http://schema.org/WebPage">

<div id='breadcrumb' itemprop='breadcrumb'> <a href='../index.php'>Home &gt; </a>  <a href='../html/p6.php'>Galleries &gt; <a href='gallery193.php'>Introducing Angelica</a></div>

<div id="wrapper">

	<div id="top">


<div id='top'>


	<div id='logo' class='g3-1'>
		<a href='http://www.concupiscent.co' class='trans'>
		<img src='../images/header_DWhite.png' alt='red_logo'/></a>
	</div>

	<div id='mid' class='g3-2'>
	</div>


	<div id='search' class='g3-3'>
		<div id='search_bg' class='silver'>
		<form name='search_tools' class='tools_buttons'>

			<input id='search_tools' class='button' type='button' value='Search Tools' name='SearchTools' onClick=
						" document.getElementById('sites').style.display = '';
						document.getElementById('l3').style.display = '';
						document.getElementById('close_tools').style.display = '';
						document.getElementById('top100').style.display = '';
						document.getElementById('l4').style.display = '';
						document.getElementById('model_search').style.display = '';" ;>
			<br>
			<input id='close_tools' class='button' type='button' value='Close Search' name='CloseSearchTools' onClick=
						" document.getElementById('sites').style.display = 'none';
						document.getElementById('l3').style.display = 'none';
						document.getElementById('close_tools').style.display = 'none';
						document.getElementById('top100').style.display = 'none';
						document.getElementById('l4').style.display = 'none';
						document.getElementById('model_search').style.display = 'none';" ;>
		</form>
		</div>
	</div>

	<br>

</div>

<br>
<div id='l1' class='line'> </div>
<br>
<div id='search_bg' class='silver'>
	<div id='sites'>
			<h2>Sites</h2>
			<span id='site1' class='span1'> <a href='../html/search_results_x-art.php' target='_blank' title='See all our galleries from X-Art'>X-Art</a></span>
			<span id='site2' class='span2'> <a href='../html/search_results_w4b.php' target='_blank' title='See all our galleries from Watch 4 Beauty'>W4B</a></span>
			<span id='site3' class='span2'> <a href='../html/search_results_ftv.php' target='_blank' title='See all our galleries from FTV Girls'>FTV Girls</a></span>
			<span id='site4' class='span2'> <a href='../html/search_results_metart.php' target='_blank' title='See all our galleries from MetArt'>MetArt</a></span>
			<span id='site5' class='span2'> <a href='../html/search_results_femjoy.php' target='_blank' title='See all our galleries from Femjoy'>Femjoy</a></span>
			<span id='site6' class='span2'> <a href='../html/search_results_domai.php' target='_blank' title='See all our galleries from Domai'>Domai</a></span>
			<span id='site7' class='span2'> <a href='../html/search_results_sexart.php' target='_blank' title='See all our galleries from SexArt'>SexArt</a></span>
			<span id='site8' class='span2'> <a href='../html/search_results_zemani.php' target='_blank' title='See all our galleries from Zemani'>Zemani</a></span>
			<span id='site9' class='span1'> <a href='../html/search_results_nubiles.php' target='_blank' title='See all our galleries from Nubiles'>Nubiles</a></span>
			<span id='site10' class='span3'> <a href='../html/search_results_torridart.php' target='_blank' title='See all our galleries from TorridArt'>TorridArt</a></span>
			<span id='site11' class='span3'> <a href='../html/search_results_tle.php' target='_blank' title='See all our galleries from The Life Erotic'>TLE</a></span>
			<span id='site12' class='span3'> <a href='../html/search_results_rylskyart.php' target='_blank' title='See all our galleries from Rylsky Art'> Rylsky Art</a></span>
			<span id='site13' class='span3'> <a href='../link/errotica_archives_main.php' target='_blank' title='See all our galleries from Errotica Archives'>Errotica A..</a></span>
			<span id='site14' class='span3'> <a href='../link/good_girls_main.php' target='_blank' title='See all our galleries from Good Girls'>Good Girls</a></span>
			<span id='site15' class='span3'> <a href='../html/search_results_hegre-art.php' target='_blank' title='See all our galleries from Hegre-Art'>Hegre-Art</a></span>
			<span id='site16' class='span3'> <a href='../link/erotic_beauty_main.php' target='_blank' title='See all our galleries from Erotic Beauty'>Erotic Beauty</a></span>
	</div>
</div>
<br>
<div id='l3' class='line'> </div>
<div id='search_bg' class='silver'>
	<div id='top100' >
		<div id='top'>
			<h2>Top 100</h2>
			<a href='../html/top_sets.php' id='top_galleries' class='button' target='_blank' title='Top 100 Galleries'> Galleries </a>
			<a href='../html/top_models.php' id='top_models' class='button' target='_blank' title='Top 100 Models'>  Models </a>
			<a href='../html/top_artists.php' id='top_artists' class='button' target='_blank' title='Top 100 Artists'>  Artists </a>
			<a href='../html/top_recent.php' id='top_recent' class='button' target='_blank' title='Top 100 Most recently added'> Recent </a>
			<a href='../html/top_new.php' id='top_new' class='button' target='_blank' title='Top 100 Newest by date'>  Newest </a>
			<a href='../html/top_vintage.php' id='top_vintage' class='button' target='_blank' title='Top 100 From yester year'>  Vintage </a>
			<a href='../html/top_nation.php?str=A B B' id='top_nation' class='button' target='_blank' title='Top 100 Nationalities'>  Nation </a>
			<a href='../html/top_random.php' id='top_random' class='button' target='_blank' title='Top 100 Artists'>  Random </a>
		</div>
	</div>
</div>
<div id='l4' class='line'> </div>
<div id='search_bg' class='silver'>
	<div id='model_search' >
		<h2>Models</h2>
		<form name='model_search' class='search_form' target='blank' action='../html/search_results.php' method='get' autocomplete='on' >

			<input id='txt' placeholder='Model name' type='text' maxlength='20' name='str'>

		</form>
	</div>
</div>
<div id='l3' class='line'> </div>
<script>
	document.getElementById('sites').style.display = 'none';
	document.getElementById('l3').style.display = 'none';
	document.getElementById('close_tools').style.display = 'none';
	document.getElementById('top100').style.display = 'none';
	document.getElementById('l4').style.display = 'none';
	document.getElementById('model_search').style.display = 'none';
</script>


	</div>


	<div id="content-wrapper">


		<div id="pod">


<div class='floatCentre400'><div id='model_names' style='text-align: center;'><a href='../html/search_results.php?str=Katherine A'style='display:inline-block;'>Katherine A</a></div></div><br><br><div id="about">

				<FORM>

						<INPUT id="button1" class="button" type="button" value="Gallery Info" name="button1" onClick=
						"document.getElementById('Gallery_info').style.display = '';
						 document.getElementById('Bio').style.display = 'none';
						 document.getElementById('Sets').style.display = 'none';
						 document.getElementById('Rate').style.display = 'none';
						 document.getElementById('button1').style.display = '';
						 document.getElementById('button2').style.display = '';
						 ">

						<INPUT id="button2" class="button" type="button" value="Model Bio" name="button2" onClick=
						"document.getElementById('Gallery_info').style.display = 'none';
						 document.getElementById('Bio').style.display = '';
						 document.getElementById('Sets').style.display = 'none';
						 document.getElementById('Rate').style.display = 'none';
						 document.getElementById('button2').style.display = '';
						 document.getElementById('button1').style.display = '';
						 ">

						 <INPUT id="button3" class="button" type="button" value="Other Galleries" name="button3" onClick=
						"document.getElementById('Sets').style.display = '';
						 document.getElementById('Gallery_info').style.display = 'none';
						 document.getElementById('Bio').style.display = 'none';
						 document.getElementById('Rate').style.display = 'none';
						">

						 <INPUT id="button4" class="button" type="button" value="Rate it" name="button4" onClick=
						"document.getElementById('Sets').style.display = 'none';
						 document.getElementById('Gallery_info').style.display = 'none';
						 document.getElementById('Bio').style.display = 'none';
						 document.getElementById('Rate').style.display = '';
						">


					</FORM>

					<div id="Gallery_info">
						<div id='story' itemscope itemtype='http://schema.org/ImageObject'><h1 itemprop='name'>Introducing Angelica</h1><p> By </p><h3><a href=../html/search_results_artist.php?str=Unknown_Artist target='_blank'>Unknown Artist</a></h3><p> From</P><h3 itemprop='publisher'><a href=../link/x-art_main.php target='_blank'>X-Art</a></h3><h6 itemprop='description'></h6></div><tr><td class='image_container'><div class='droppable2'><a href='../lib/x-art/introducing_angelica/cover.jpg' style='width: 230px; top: auto; display: inline-block;' rel='lightbox' target='_blank'><img src='../lib/x-art/introducing_angelica/cover.jpg' style='width: 230px;' alt='Cover image' itemprop='image' ></a></div></td></tr><br><h4 itemprop='description'></h4><br><div class='about'><a href=../link/x-art_main.php target='_blank'>See more... </a></div>

					</div>


					<div id="Bio">
						<h2>Model Bio</h2><br><div class='ridge'><div class='s2'><h3 itemprop='contributor'>Katherine A</h3></div><div class='s1'><p>Hair:&#32;</p><h6>Fair</h6></div><div class='s2'><p>Eye colour:&#32;</p><h6>Brown</h6></div><div class='s1'><p>Height (feet/in):&#32;</p><h6>5'8"</h6></div><div class='s2'><p>Height (cm):&#32;</p><h6>173cm</h6></div><div class='s1'><p>Vital Stats (in):&#32;</p><h6>30B-23-32</h6></div><div class='s2'><p>Vital Stats (cm):&#32;</p><h6>76-58-81</h6></div><div class='s1'><p>Age (now):&#32;</p><h6></h6></div><div class='s2'><p>DOB:&#32;</p><h6>14/04/1993</h6></div><div class='s1'><p>Country:&#32;</p><h6>Russia</h6></div><div class='s2'><p>CC Model rating:&#32;</p><h6>9.00</h6></div></div><br><h3>Model aka</h3><p>what sites does she appear and what names does she use</p><br><br><h5>&#32;Katherine A</h5><br><br><div><p>aka&#32;</p><h5>Snejanna</h5></div><br><div><p>aka&#32;</p><h5>Krystal Boyd</h5></div><br><div><p>Met-Art&#32;</p><h5>Katherine A</h5></div><br><div><p>Sex-Art&#32;</p><h5>Katherine A</h5></div><br><div><p>TLE&#32;</p><h5>Anjelica</h5></div><br><div><p>X-Art&#32;</p><h5>Angelica</h5></div><br><div><p>Femjoy&#32;</p><h5>Kathy I</h5></div><br><div><p>W4B&#32;</p><h5>Abby</h5></div><br><div><p>Nubiles&#32;</p><h5>Ebbi</h5></div>					</div>

					<div id="Sets">
						<br><p>Katherine A</p><br><tr><td class='image_container'><div class='droppable2'><a href='../lib/met-art/frontida/cover.jpg' style='width: 114px; top: auto; display: inline-block;' rel='lightbox' target='_blank'><img src='../lib/met-art/frontida/cover.jpg' style='width: 114px;' alt='Cover image'> </a></div></td><td><a href='../galleries/gallery131.php'>Frontida<br><br><p>06/09/2012</p><br><p> Set rating: &#32;<h5>8.50</h5></p></a></td></tr><tr><td class='image_container'><div class='droppable2'><a href='../lib/met-art/the_offer/cover.jpg' style='width: 114px; top: auto; display: inline-block;' rel='lightbox' target='_blank'><img src='../lib/met-art/the_offer/cover.jpg' style='width: 114px;' alt='Cover image'> </a></div></td><td><a href='../galleries/gallery159.php'>The Offer<br><br><p>07/06/2012</p><br><p> Set rating: &#32;<h5>8.50</h5></p></a></td></tr><tr><td class='image_container'><div class='droppable2'><a href='../lib/x-art/introducing_angelica/cover.jpg' style='width: 114px; top: auto; display: inline-block;' rel='lightbox' target='_blank'><img src='../lib/x-art/introducing_angelica/cover.jpg' style='width: 114px;' alt='Cover image'> </a></div></td><td><a href='../galleries/gallery193.php'>Introducing Angelica<br><br><p>26/11/2012</p><br><p> Set rating: &#32;<h5>8.00</h5></p></a></td></tr><tr><td class='image_container'><div class='droppable2'><a href='../lib/x-art/spilled_milk/cover.jpg' style='width: 114px; top: auto; display: inline-block;' rel='lightbox' target='_blank'><img src='../lib/x-art/spilled_milk/cover.jpg' style='width: 114px;' alt='Cover image'> </a></div></td><td><a href='../galleries/gallery247.php'>Spilled Milk<br><br><p>08/03/2013</p><br><p> Set rating: &#32;<h5>8.90</h5></p></a></td></tr><tr><td class='image_container'><div class='droppable2'><a href='../lib/met-art/rodopeta/cover.jpg' style='width: 114px; top: auto; display: inline-block;' rel='lightbox' target='_blank'><img src='../lib/met-art/rodopeta/cover.jpg' style='width: 114px;' alt='Cover image'> </a></div></td><td><a href='../galleries/gallery368.php'>Rodopeta<br><br><p>01/08/2013</p><br><p> Set rating: &#32;<h5>8.00</h5></p></a></td></tr>					</div>


					<div id="Rate">
						<br>
						<h5>Rate this model</h5>
						<br>

						<p>Katherine A</p><br><div><a href='../lib/x-art/introducing_angelica/thumb.jpg' style='width: 168px; margin-left:2px; top: auto; display: inline-block;' rel='lightbox' title='model' target='_blank'><img src='../lib/x-art/introducing_angelica/thumb.jpg' style='width: 168px; margin-left:2px' alt='Model image' /></a></div><div class='float-left'>
						<form name='rate_model' action='../sql/post_model_rating.php' target='model_vote' method='post' onsubmit='target_popup(this)'>
							<INPUT id='radio1a' class='styled' type='radio' value='01_103' name='radioA' ><a>1</a><br>
							<INPUT id='radio2a' class='styled' type='radio' value='02_103' name='radioA' ><a>2</a><br>
							<INPUT id='radio3a' class='styled' type='radio' value='03_103' name='radioA' ><a>3</a><br>
							<INPUT id='radio4a' class='styled' type='radio' value='04_103' name='radioA' ><a>4</a><br>
							<INPUT id='radio5a' class='styled' type='radio' value='05_103' name='radioA' ><a>5</a><br>
							<INPUT id='radio6a' class='styled' type='radio' value='06_103' name='radioA' ><a>6</a><br>
							<INPUT id='radio7a' class='styled' type='radio' value='07_103' name='radioA' ><a>7</a><br>
							<INPUT id='radio8a' class='styled' type='radio' value='08_103' name='radioA' ><a>8</a><br>
							<INPUT id='radio9a' class='styled' type='radio' value='09_103' name='radioA' ><a>9</a><br>
							<INPUT id='radio10a' class='styled' type='radio' value='10_103' name='radioA' ><a>10</a><br>
							<INPUT id='model_rate_button' class='button' type='submit' value='Vote' style='width:44px; float:right'>
						</form>
					</div>
					<div>
						<h5>Rate this set</h5>
						<br>

						<div><a href='../lib/x-art/introducing_angelica/cover.jpg' style='width: 168px; margin-left:2px; top: auto; display: inline-block;' rel='lightbox' title='model' target='_blank'><img src='../lib/x-art/introducing_angelica/cover.jpg' style='width: 168px; margin-left:2px' alt='Model image' /></a></div>
					</div>

					<div class="float-left" >
						<form name="rate_set" action="../sql/post_set_rating.php" method="post" target="_blank" onsubmit="target_popup(this)">
							<INPUT id="radio1b" class="styled" type="radio" value="1 193" name="radioB" ><a>1 </a><br>
							<INPUT id="radio2b" class="styled" type="radio" value="2 193" name="radioB" ><a>2</a><br>
							<INPUT id="radio3b" class="styled" type="radio" value="3 193" name="radioB" ><a>3</a><br>
							<INPUT id="radio4b" class="styled" type="radio" value="4 193" name="radioB" ><a>4</a><br>
							<INPUT id="radio5b" class="styled" type="radio" value="5 193" name="radioB" ><a>5</a><br>
							<INPUT id="radio6b" class="styled" type="radio" value="6 193" name="radioB" ><a>6</a><br>
							<INPUT id="radio7b" class="styled" type="radio" value="7 193" name="radioB" ><a>7</a><br>
							<INPUT id="radio8b" class="styled" type="radio" value="8 193" name="radioB" ><a>8</a><br>
							<INPUT id="radio9b" class="styled" type="radio" value="9 193" name="radioB" ><a>9</a><br>
							<INPUT id="radio10b" class="styled" type="radio" value="10 193" name="radioB" ><a>10</a><br>
							<INPUT id="set_rate_button" class="button" type="submit" value="Vote" style="width:44px; float:right">
						</form>
					</div>


					<script>
						document.getElementById('Bio').style.display = 'none';
						document.getElementById('Sets').style.display = 'none';
						document.getElementById('Rate').style.display = 'none';
						document.getElementById('button2').style.display = '';
						document.getElementById('button1').style.display = '';
						document.getElementById('button3').style.display = '';
						document.getElementById('button4').style.display = '';
					</script>

					</div>

				<br>

				</div>


		</div>


			<table id="grid">

				<!-- droppable = lightbox -->
				<tr>
					<td class="image_container"><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica1.jpg" style="width: 345px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica1.jpg" style="width: 345px;" alt="Angelica 1" /></a></div></td>


					<td class="image_container"><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica2.jpg" style="width: 345px; top:auto; display:inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica2.jpg" style="width: 345px;" alt="Angelica 2" /></a></div></td>

					<td class="image_container"><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica3.jpg" style="width: 345px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica3.jpg" style="width: 345px;" alt="Angelica 3" /></a></div></td>
				</tr>

				<tr>
					<td class="image_container"><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica4.jpg" style="width: 230px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica4.jpg" style="width: 230px;" alt="Angelica 4" /></a></div></td>

					<td class="image_container"><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica5.jpg" style="width: 345px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica5.jpg" style="width: 345px;" alt="Angelica 5" /></a></div></td>

					<td class="image_container"><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica6.jpg" style="width: 345px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica6.jpg" style="width: 345px;" alt="Angelica 6" /></a></div></td>
				</tr>

				<tr>

					<td class="image_container" ><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica7.jpg" style="width: 230px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica7.jpg" style="width: 230px;" alt="Angelica 7" /></a></div></td>


					<td class="image_container" ><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica8.jpg" style="width: 345px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica8.jpg" style="width: 345px;" alt="Angelica 8" /></a></div></td>


					<td class="image_container" ><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica9.jpg" style="width: 230px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica9.jpg" style="width: 230px;" alt="Angelica 9" /></a></div></td>
				</tr>

				<tr>

					<td class="image_container" ><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica10.jpg" style="width: 230px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica10.jpg" style="width: 230px;" alt="Angelica 10" /></a></div></td>


					<td class="image_container" ><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica11.jpg" style="width: 230px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica11.jpg" style="width: 230px;" alt="Angelica 11" /></a></div></td>


					<td class="image_container" ><div class="droppable">
						<a href="../lib/x-art/introducing_angelica/introducing_angelica12.jpg" style="width: 230px; top: auto; display: inline-block;" rel="lightbox[Angelica]" title="Angelica" target="_blank">
						<img src="../lib/x-art/introducing_angelica/introducing_angelica12.jpg" style="width: 230px;" alt="Angelica 12" /></a></div></td>
				</tr>

			</table>

		</div>


		<div id="images">

			<h3>Gallery images</h3>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica1.jpg" rel="lightbox" title="Angelica" target="_blank">1</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica2.jpg" rel="lightbox" title="Angelica" target="_blank">2</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica3.jpg" rel="lightbox" title="Angelica" target="_blank">3</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica4.jpg" rel="lightbox" title="Angelica" target="_blank">4</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica5.jpg" rel="lightbox" title="Angelica" target="_blank">5</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica6.jpg" rel="lightbox" title="Angelica" target="_blank">6</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica7.jpg" rel="lightbox" title="Angelica" target="_blank">7</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica8.jpg" rel="lightbox" title="Angelica" target="_blank">8</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica9.jpg" rel="lightbox" title="Angelica" target="_blank">9</a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica10.jpg" rel="lightbox" title="Angelica" target="_blank"> 10 </a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica11.jpg" rel="lightbox" title="Angelica" target="_blank"> 11 </a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica12.jpg" rel="lightbox" title="Angelica" target="_blank"> 12 </a>
			<br>
			<h3>Bonus images...</h3>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica13.jpg" rel="lightbox[Angelica]" title="Angelica" target="_blank"> 13 </a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica14.jpg" rel="lightbox[Angelica]" title="Angelica" target="_blank"> 14 </a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica15.jpg" rel="lightbox[Angelica]" title="Angelica" target="_blank"> 15 </a>
			<a href="../lib/x-art/introducing_angelica/introducing_angelica16.jpg" rel="lightbox[Angelica]" title="Angelica" target="_blank"> 16 </a>

			<a href="../lib/x-art/introducing_angelica/introducing_angelica.mp4" target="_blank"> Video </a>
		</div>

		<div id="horizontalbanner">

			<a href="../link/x-art_banner.php" target="_blank">
			<img src="../lib/x-art/x-art_banner.jpg" alt="Click for offer"/></a>

		</div>



	<div id="footer">

		<ul>
			<ul>
<li> <a href='../html/p1.php' target='_blank'>PICTURES</a></li>
<li> <a href='../html/video_results.php' target='_blank'>VIDEOS</a></li>
<li> <a href='../html/potd.php' target='_blank'>POTD</a></li>
<li> <a href='../html/votd.php' target='_blank'>VOTD</a></li>
<li> <a href='../html/site_review.php' target='_blank'>REVIEWS</a></li>
<li> <a href='../html/search_offers.php' target='_blank'>OFFERS</a></li>
<li> <a href='../php/under_construction.php' target='_blank'>SHOP</a></li>
<li> <a href='../galleries/lucky.php' target='_blank'>I FEEL LUCKY</a></li>
<li> <a href='http://www.concupiscentcoquette.co/wordpress' target='_blank'>BLOG</a></li>
</ul>
		</ul>
	</div>

	<div id="alinks">


<div id='friends'>
	<h2> Friendly links of an erotic nature  </h2>

	<div class='links'>
		<div class='odd'>
			<h6>Our favourite sites</h6>
			<ul>
				<li> <a href='../link/lovehoney_main.php' target='_blank' title='Love Honey'>Love Honey</a><br><p> - £10 sale items And 20% off!</p><br></li>
				<li> <a href='http://www.spaceandmotion.com/vintage-nude-women-erotica.htm' target='_blank' title='Space and Motion '>Space and Motion </a><br><p> - Vintage nudes, Fetish, Philosophy of sex etc.</p><br></li>
				<li> <a href='http://www.vintagelovelies.com' target='_blank' title='Vintage Lovelies'>Vintage Lovelies</a><br><p> - Vintage and retro erotica</p><br></li>
				<li> <a href='http://www.erotic-art-photos.com/' target='_blank' title='Erotic Art Photos'>Erotic Art Photos</a><br><p> A Directory of the Web&rsquo;s most sensual Erotic Art Photography</p><br></li>
				<li> <a href='http://www.sexandcensorship.org/' target='_blank' title='Sex & Censorship'>Sex & Censorship</a><br><p> Great articles and info about the increase of internet censorship</p><br></li>
			</ul>
		</div>
	</div>
	<div class='links'>
		<div class='even'>
			<h6>Erotic Art galleries &amp; reviews</h6>
			<ul>
				<li> <a href='http://www.porndirectory.com/Babe/' target='_blank' title='Porn directory'>Porn directory</a><br><p> - A comprehensive adult directory</p><br></li>
				<br><br>
				<li> <a href='http://www.RateXpics.com/disclaimer.cfm?TopString=9782' target='_blank'>RateXpics </a><br><p> - Rate naked pics</p><br></li>
				<br><br>
				<li> <a href='http://www.nudetimes.net' target='_blank'>Nude Times</a><br><p>- Great artistic nudes</p><br></li>
				<br><br>
				<li> <a href='http://www.godsartnudes.com' target='_blank'>God&rsquo;s Art Nudes</a><br><p> - Free Nudes and Erotica</p><br></li>
				<br><br>
				<li> <a href='http://www.bustyful.com' target='_blank'>Bustyful</a><br><p> - is beautiful</p><br></li>
				<br><br>
				<li> <a href='http://www.thefreeadultdirectory.com/' target='_blank'>The Free Adult Directory</a><br><p>Just about every kind of adult site</p><br></li>
				<br><br>
				<li> <a href='http://www.freshnudes.net' target='_blank'>Fresh Nudes</a><br><p>Nude Models &amp; Photographers</p><br></li>
			</ul>
		</div>
	</div>
	<div class='links'>
		<div class='odd'>
			<h6>Erotic Art links</h6>
			<ul>
				<li> <a href='http://thenude.eu' target='_blank'>theNUDE.eu</a><br><p>- The largest and most complete database of cover models</p><br></li>
				<br><br>
				<li> <a href='http://www.pornteengirl.com' target='_blank'>PornTeenGirl.com</a><br><p>- Free Porn pictures and video</p><br></li>
				<br><br>
				<li> <a href='http://www.freeones.co.uk' target='_blank'>Free Porn</a><br><p>- FreeOnes - the ultimate babe site since 1998</p><br></li>
				<br><br>
				<li> <a href='http://www.erotic-photos.net/' target='_blank'>Erotic photos net</a><br><p>- Nudity erotica &amp; porn</p><br></li>
				<br><br>
				<li> <a href='http://www.art-erotica.com/' target='_blank'>Art Erotica</a><br><p>- Fine art erotica with beautiful teens</p><br></li>
			</ul>
		</div>
	</div>
	<br>
	<a href='../html/traffic.php'>Webmasters</a>
</div>
<br>

   </div>



	<div id="statement">
		<p> &copy; Copyright 2012. ConcupiscentCoquette.co All rights reserved.</p>
		<p>All models appearing on this website are over the age of 18.</p>
		<p>18 U.S.C. 2257 Compliance Statement</p>
		<a href="http://www.rtalabel.org" target="_blank">
		<img src="../images/120x60_RTA-5042-1996-1400-1577-RTA_c.gif" alt="RTA"></a>
	</div>
</div>

</body>


<!-- Start of StatCounter Code for Default Guide -->
<script type='text/javascript'>
var sc_project=8356053;
var sc_invisible=1;
var sc_security='f4e2a31e';
</script>
<script type='text/javascript'
src='http://www.statcounter.com/counter/counter.js'></script>
<noscript><div class='statcounter'><a title='click tracking'
href='http://statcounter.com/' target='_blank'><img
class='statcounter'
src='http://c.statcounter.com/8356053/0/f4e2a31e/1/'
alt='click tracking'></a></div></noscript>
<!-- End of StatCounter Code for Default Guide -->
</html><!-- Web Site By GeoSIS - www.geosis.co.uk -->

<!-- This work is licensed under the MIT License - http://www.opensource.org/licenses/mit-license.php -->

"""

data_regex = """<a href="(..\/.*)" target="_blank">\d+<\/a>"""
img_regex = "/.*(jpg|png)"
domain = "http://www.concupiscent.co/"
urls = []

html = html.replace("\n", "")
html = html.replace("\r", "")
print "0-----0"
data = re.search("""<div id="images">.*</div>""", html).group()
# print data

for url in re.findall(data_regex, data):
    # print "url: ",urls
    value = re.search(img_regex, url).group()
    # print "value :", value
    if value:
        urls.append(domain + value)
print urls,len(urls)