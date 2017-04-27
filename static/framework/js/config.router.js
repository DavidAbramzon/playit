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
    }).state('create-game', {
        url: "/create-game",
        templateUrl: "/static/framework/views/CreateGameView/create-game.html"
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

}]);