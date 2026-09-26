<?php
/**
 * Plugin Name: Exowise Landing
 * Description: Sirve la landing estatica (index.html en la raiz) como portada y unifica www -> exowise.ai. Para volver a WordPress, borrar este archivo.
 *
 * Publicacion: subir los archivos por SFTP a html/ y luego vaciar el cache desde
 * wp-admin (barra superior: GoDaddy -> Flush Cache). Sin eso, el CDN sigue mostrando la version anterior.
 */

// www.exowise.ai -> https://exowise.ai (301)
add_action( 'init', function () {
    if ( is_admin() || wp_doing_ajax() || ( defined( 'WP_CLI' ) && WP_CLI ) ) { return; }
    $host = strtolower( $_SERVER['HTTP_HOST'] ?? '' );
    if ( $host === 'www.exowise.ai' ) {
        wp_redirect( 'https://exowise.ai' . ( $_SERVER['REQUEST_URI'] ?? '/' ), 301 );
        exit;
    }
}, 0 );

// Portada estatica
add_action( 'template_redirect', function () {
    if ( is_admin() || wp_doing_ajax() || ! ( is_front_page() || is_home() ) ) { return; }
    $file = ABSPATH . 'index.html';
    if ( ! is_readable( $file ) ) { return; }
    status_header( 200 );
    header( 'Content-Type: text/html; charset=utf-8' );
    header( 'Cache-Control: public, max-age=300' );
    readfile( $file );
    exit;
}, 0 );
