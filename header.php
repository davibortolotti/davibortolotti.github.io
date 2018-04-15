
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
    <meta name="description" content="">
    <meta name="author" content="">

    <title><?php echo get_bloginfo( 'name' ); ?></title>

    <!-- Bootstrap core CSS -->
    <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.5/css/bootstrap.min.css" rel="stylesheet">

    <!-- Custom styles for this template -->
    <link href="<?php echo get_bloginfo('template_directory'); ?>/style.css" rel="stylesheet">
    <link href="https://fonts.googleapis.com/css?family=Raleway|Indie+Flower|Quicksand:500" rel="stylesheet">


    <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
    <!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
    <![endif]-->
    <?php wp_head();?>
  </head>

  <body>

    <header class="header">

        <nav class="blog-nav">
          <img class="header__logo" src="<?php echo get_template_directory_uri() ?>/img/artesurpresa-logo.png">
          <a class="blog-nav-item" href="<?php echo get_bloginfo( 'wpurl' );?>">Home</a>
          <a class="blog-nav-item" href="<?php echo get_permalink( woocommerce_get_page_id( 'shop' ) );?>">Loja</a>
          <a class="blog-nav-item" href="<?php echo get_permalink( woocommerce_get_page_id( 'myaccount' ) );?>">
            <?php if(is_user_logged_in()) { ?>Conta<?php } else { ?>Entrar<?php } ?></a>
        </nav>
        <nav class="page-nav">
          <a class="#"></a>
          <a class="#"></a>
        </nav>
    </header>
