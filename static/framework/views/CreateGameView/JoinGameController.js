/**
 * Created by user on 4/27/2017.
 */
app.controller('JoinGameController', ['$stateParams', '$scope', 'ApiService', '$location', '$localStorage', '$sessionStorage',
    function ($stateParams, $scope, ApiService, $location, $localStorage, $sessionStorage) {
        var apiRequest = ApiService.ApiRequest;
        if ($stateParams.shouldCreate) {
            apiRequest('/create_game/', 'POST', "",
                {'game_type_id': 1}, "", "").then(function (data) {
                $scope.gameId = data.pin_code;
            });
        }
        $scope.joinGame = function () {

            apiRequest('/join_game/', 'POST', "", {
                'pin_code': $scope.gameId,
                'nickname': $scope.nickname
            }, "", "").then(function (data) {
                sessionStorage.setItem("gameId", $scope.gameId);
                $location.path('/before-start');
            }, function (data) {
                alert("error");
            });
        }
    }]);
