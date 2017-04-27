/**
 * Created by user on 4/27/2017.
 */
app.controller('CreateGameController', ['$scope', '$http',
    function ($scope, $http) {
        var req = {
            method: 'POST',
            url: '/api/create_game/',
            data: { 'game_type_id': 1 }
        };

        $http(req).then(function (response) {
            $scope.gameId = response.data.pin_code;
        });
    }]);
