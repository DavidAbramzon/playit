/**
 * Created by user on 4/27/2017.
 */
app.controller('RoundSummaryController', ['$stateParams', '$timeout', '$scope', 'ApiService', '$location', '$localStorage', '$sessionStorage',
    function ($stateParams, $timeout, $scope, ApiService, $location,
              $localStorage, $sessionStorage) {
        var apiRequest = ApiService.ApiRequest;
        $scope.gameId = sessionStorage.getItem("gameId");
        apiRequest('/get_round_summary/', 'GET', "",
                "", "", "").then(function (data) {
                $scope.players = data;
            })
        $timeout(nextRound, 8000);
        function nextRound() {
            $location.path('/show-question');
        };

    }]);
