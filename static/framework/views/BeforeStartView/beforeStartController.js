/**
 * Created by user on 4/27/2017.
 */
app.controller('BeforeStartController', ['$stateParams', '$timeout', '$scope', 'ApiService', '$location', '$localStorage', '$sessionStorage',
    function ($stateParams, $timeout, $scope, ApiService, $location,
              $localStorage, $sessionStorage) {
        var apiRequest = ApiService.ApiRequest;

        $scope.gameId = sessionStorage.getItem("gameId");
        $scope.data = [];

        (function tick() {

            apiRequest('/get_players/', 'GET', "",
                "", "", "").then(function (data) {
                $scope.players = data;
            })
             apiRequest('/game/', 'GET', {"pin_code":$scope.gameId},
                "", "", "").then(function (data) {
                if(data.game_started){
                    $location.path('/show-question');
                }
                else{
                    $timeout(tick, 1000);
                }
            })
        })();

        $scope.startGame = function () {
            apiRequest('/start_game/', 'POST', "", {"pin_code":2}, "", "").then(function (data)
            {
                $location.path('/show-question');
            })
            ;
        }


    }]);
