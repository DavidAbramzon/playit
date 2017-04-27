'use strict';

/**
 * Config for the router
 */
app.config(['$stateProvider', '$urlRouterProvider',
function ($stateProvider, $urlRouterProvider) {


    // APPLICATION ROUTES
    // -----------------------------------
    // For any unmatched url, redirect to /app/dashboard
    $urlRouterProvider.otherwise("/home");
    //
    // Set up the states
    $stateProvider.state('home', {
        url: "/home",
        templateUrl: "/static/framework/views/HomeView/home.html"
    });

}]);