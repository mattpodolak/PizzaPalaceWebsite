<?php
	header('Content-type: text/html; charset=utf-8');
	session_start();

?>

<!DOCTYPE html>
<html>

<head>
	<meta http-equiv="Content-Type" content="text/html; charset=utf-8" /> 
	<title>Pizza Palace - Cart</title>
	<link rel="stylesheet" href="assets/bootstrap/css/bootstrap.min.css">
	<link rel="stylesheet" href="assets/fonts/font-awesome.min.css">
	<link rel="stylesheet" href="assets/fonts/ionicons.min.css">
	<link rel="stylesheet" href="assets/css/styles.css">
	<link rel="stylesheet" href="assets/css/intext.css">
	<link rel="stylesheet" href="assets/css/pizzafooter.css">
	<link rel="stylesheet" href="assets/css/pizzamenu.css">
	<link rel="stylesheet" href="assets/css/Pretty-Footer.css">
	<link rel="stylesheet" href="assets/css/Pretty-Registration-Form.css">
	<link rel="stylesheet" href="assets/css/styles2.css">
	<link rel="stylesheet" href="assets/css/user.css">
	<link rel="stylesheet" href="assets/css/animate.css">
	
	<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-108406738-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-108406738-1');
</script>
    
    <script>
window['_fs_debug'] = false;
window['_fs_host'] = 'fullstory.com';
window['_fs_org'] = '83YEG';
window['_fs_namespace'] = 'FS';
(function(m,n,e,t,l,o,g,y){
    if (e in m) {if(m.console && m.console.log) { m.console.log('FullStory namespace conflict. Please set window["_fs_namespace"].');} return;}
    g=m[e]=function(a,b){g.q?g.q.push([a,b]):g._api(a,b);};g.q=[];
    o=n.createElement(t);o.async=1;o.src='https://'+_fs_host+'/s/fs.js';
    y=n.getElementsByTagName(t)[0];y.parentNode.insertBefore(o,y);
    g.identify=function(i,v){g(l,{uid:i});if(v)g(l,v)};g.setUserVars=function(v){g(l,v)};
    g.identifyAccount=function(i,v){o='account';v=v||{};v.acctId=i;g(o,v)};
    g.clearUserCookie=function(c,d,i){if(!c || document.cookie.match('fs_uid=[`;`]*`[`;`]*`[`;`]*`')){
    d=n.domain;while(1){n.cookie='fs_uid=;domain='+d+
    ';path=/;expires='+new Date(0).toUTCString();i=d.indexOf('.');if(i<0)break;d=d.slice(i+1)}}};
})(window,document,window['_fs_namespace'],'script','user');
</script>
</head>

<body>
    <div class="container borderlr">
     <nav class="navbar navbar-default" id="header">
        <div class="container-fluid">
            <div class="navbar-header"><a class="navbar-brand navbar-link" href="#"><i class="icon ion-pizza"></i> Pizza Palace</a>
                <button class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navcol-1"><span class="sr-only">Toggle navigation</span><span class="icon-bar"></span><span class="icon-bar"></span><span class="icon-bar"></span></button>
            </div>
            <div class="collapse navbar-collapse" id="navcol-1">
                <ul class="nav navbar-nav">
                    <li role="presentation"><a href="index.php">MAIN MENU</a></li>
                    <li role="presentation"><a href="deals.php">DEALS </a></li>
                    <li role="presentation"><a href="specialtypizza.php">SPECIALTY PIZZA</a></li>
                    <li role="presentation"><a href="wings.php">WINGS </a></li>
                    <li role="presentation"><a href="sandwiches.php">SANDWICHES </a></li>
                    <li role="presentation"><a href="sides.php">SIDES </a></li>
                    <li class = "active" role="presentation"><a href="cart.php"><i class="fa fa-shopping-cart fa-lg" aria-hidden="true"></i> &nbsp;CART </a></li>
                </ul>
            </div>
        </div>
    </nav>
        <div class="row register-form buffer animated fadeIn">
            <div class="col-md-8 col-md-offset-2">
                <form class="form-horizontal custom-form add-height">
                
                <!-- beginning of your div -->
		<div id="cart_stuffs">
		<div class = "order-confirm-top">
		<script type="text/javascript">
			var d = new Date();
			d = d.toLocaleTimeString().replace(/:\d+ /, ' ');
			document.write('Placed order at ' + d + ".");
		</script>
		<BR>Congratulations! Your order has been sent! It will be ready in around 30-45 minutes.
		</div>
		<div class = "order-text">
		Order #
		</div>
		<div class = "order-text order-number">
		<?php echo $_SESSION['user_id']?>
		</div>
		<!-- customer info -->
		<div>
		<script type="text/javascript">
			var customer_id = <?php echo json_encode($_SESSION['user_id'])?>;
			if(emptyCatcher(customer_id) == 1){
				alert('If your order number appears blank, it is because it has already been sent!');
			}
			
			function emptyCatcher(arg1){
				if(typeof arg1 == 'undefined' || arg1 == null){
					return 1;
				}
			}
		</script>
		</div>
		<div class="cont-order rtrn-main">
			<hr class = "short">
                        <a href="index.php">
                        Return to Main Menu
                        </a>
                    </div>
		</div>
		<!-- end of your div -->
		
                   
                </form>
            </div>
            </div>
            <div class="col-md-12 footerdiv">
                <footer>
                    <div class="row">
                        <div class="col-md-6 col-sm-6 footer-contacts">
                            <div><span class="fa fa-map-marker footer-contacts-icon"> </span>
                                <p style="color:black">181 Livingstone Street East<br> Barrie, Ontario</p>
                            </div>
                            <div><i class="fa fa-phone footer-contacts-icon"></i>
                                <p style="color:black">(705) 503-3131</p>

                            </div>
                            <div><i class="fa fa-envelope footer-contacts-icon"></i>
                                <p> <a href="#" target="_blank">info@pizzapalaceandwings.com</a></p>
                            </div>
                        </div>
                        <div class="clearfix visible-sm-block"></div>
                        <div class="col-md-6 col-sm-4 footer-about">
                            <p> </p>
                            <p> </p>
                            <p> Pricing is subject to change and taxes are not included. Images are indicative of the quality and style of the specification and may not represent wholly the finished product. </p>
                            <strong class ="footer-text-novus"> Website Developed by </strong><a href ="https://novusweb.ca">Novus</a>
                        </div>
                    </div>
                </footer>
            </div>
        </div>
    </div>
    <script src="assets/js/jquery.min.js"></script>
    <script src="assets/bootstrap/js/bootstrap.min.js"></script>
    <script src="assets/js/menu_items.js"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.0/jquery.min.js"></script>
<?php
	session_unset();
?>
</body>
</html>