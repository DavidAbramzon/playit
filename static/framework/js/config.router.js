'use strict';

/**
 * Config for the router
 */
app.config(['$stateProvider', '$urlRouterProvider',
function ($stateProvider, $urlRouterProvider) {


    // APPLICATION ROUTES
    // -----------------------------------
    // For any unmatched url, redirect to /app/dashboard
    $urlRouterProvider.otherwise("/app/dashboard");
    //
    // Set up the states
    $stateProvider.state('home', {
        url: "/",
        templateUrl: "/static/framework/views/HomeView/home.html"
    }).state('app.dashboard', {
        url: "/dashboard",
        templateUrl: "/static/views/dashboard.html",
        resolve: loadSequence('d3', 'ui.knob', 'countTo', 'dashboardCtrl'),
        title: 'Dashboard',
        ncyBreadcrumb: {
            label: 'Dashboard'
        }
    });

}]);