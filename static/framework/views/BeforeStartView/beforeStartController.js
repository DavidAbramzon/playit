/**
 * Created by user on 4/27/2017.
 */
app.controller('BeforeStartController', ['$stateParams','$timeout', '$scope', 'ApiService', '$location', '$localStorage', '$sessionStorage',
    function ($stateParams,$timeout, $scope, ApiService, $location,
              $localStorage, $sessionStorage) {
        var apiRequest = ApiService.ApiRequest;

        $scope.gameId = sessionStorage.getItem("gameId");
            $scope.data = [];

            (function tick() {
                apiRequest('is')
                apiRequest('/get_players/', 'GET', "",
            "", "", "").then(function (data) {
            $scope.players = data;
            $timeout(tick, 1000);
        })})();



    }]);
