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
        controller:"JoinGameController",
        url: "/create-game",
        templateUrl: "/static/framework/views/JoinGameView/join-game.html",
        params: { shouldCreate: true}
    }).state('join-game', {
        controller:"JoinGameController",
        url: "/join-game",
        templateUrl: "/static/framework/views/JoinGameView/join-game.html",
        params: { shouldCreate: false}
    }).state('before-start', {
        controller:"BeforeStartController",
        url: "/before-start",
        templateUrl: "/static/framework/views/BeforeStartView/before-start.html"
    }).state('show-question', {
        controller:'ShowQuestionController',
        url: "/show-question",
        templateUrl: "/static/framework/views/ShowQuestionView/show-question.html"
    }).state('round-summary', {
        url: "/round-summary",
        templateUrl: "/static/framework/views/RoundSummaryView/round-summary.html"
    });;
    $urlRouterProvider.otherwise("/home");
    $locationProvider.html5Mode({
        enabled: true,
        requireBase: false
    });

}]);