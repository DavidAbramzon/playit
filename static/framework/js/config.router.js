'use strict';

/**
 * Config for the router
 */
app.config(['$stateProvider', '$urlRouterProvider','$locationProvider',
function ($stateProvider,$urlRouterProvider,$locationProvider ) {


    // APPLICATION ROUTES
    // -----------------------------------
    // For any unmatched url, redirect to /app/dashboard

    //
    // Set up the states
    $stateProvider.state('/home', {
        url: "/home",
        templateUrl: "/static/framework/views/HomeView/home.html"
    }).state('create-game', {
        controller:"CreateGameController",
        url: "/create-game",
        templateUrl: "/static/framework/views/JoinGameView/join-game.html"
    }).state('join-game', {
        url: "/join-game",
        templateUrl: "/static/framework/views/JoinGameView/join-game.html"
    }).state('before-start', {
        url: "/before-start",
        templateUrl: "/static/framework/views/BeforeStartView/before-start.html"
    }).state('show-question', {
        url: "/show-question",
        templateUrl: "/static/framework/views/ShowQuestionView/show-question.html"
    });
    $urlRouterProvider.otherwise("/home");
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });

}]);